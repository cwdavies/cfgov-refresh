from __future__ import print_function

import importlib
import itertools
import logging
import os
import re
import subprocess
import sys

from django.apps import apps
from django.conf import settings
from django.db import connection
from django.db.migrations.loader import MigrationLoader
from django.test import RequestFactory
from django.test.runner import DiscoverRunner, is_discoverable
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from mock import Mock

from scripts import initial_data, test_data


class OptionalAppsMixin(object):
    def build_suite(self, test_labels=None, extra_tests=None, **kwargs):
        if not test_labels:
            app_names = set(itertools.chain(*(
                optional_app['apps']
                for optional_app in settings.OPTIONAL_APPS
            )))

            discoverable_app_names = filter(is_discoverable, app_names)

            test_labels = list(discoverable_app_names) + ['.']

        return super(OptionalAppsMixin, self).build_suite(
            test_labels=test_labels,
            extra_tests=extra_tests,
            **kwargs
        )


class TestDataTestRunner(OptionalAppsMixin, DiscoverRunner):
    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        # Disable logging below CRITICAL during tests.
        logging.disable(logging.CRITICAL)

        return super(TestDataTestRunner, self).run_tests(
            test_labels,
            extra_tests,
            **kwargs
        )

    def setup_databases(self, **kwargs):
        dbs = super(TestDataTestRunner, self).setup_databases(**kwargs)

        # Ensure that certain key data migrations are always run, even if
        # tests are being run without migrations, e.g. through use of
        # settings.test_nomigrations.
        self.run_required_data_migrations()

        # Set up additional required test data that isn't contained in data
        # migrations, for example an admin user.
        initial_data.run()

        return dbs

    def run_required_data_migrations(self):
        migration_methods = (
            (
                'wagtail.wagtailcore.migrations.0002_initial_data',
                'initial_data'
            ),
            (
                'wagtail.wagtailcore.migrations.0025_collection_initial_data',
                'initial_data'
            ),
        )

        loader = MigrationLoader(connection)

        for migration, method in migration_methods:
            if not self.is_migration_applied(loader, migration):
                print('applying migration {}'.format(migration))
                module = importlib.import_module(migration)
                getattr(module, method)(apps, None)

    @staticmethod
    def is_migration_applied(loader, migration):
        parts = migration.split('.')
        migration_tuple = (parts[-3], parts[-1])
        return migration_tuple in loader.applied_migrations


class AcceptanceTestRunner(TestDataTestRunner):
    def run_suite(self, **kwargs):
        gulp_command = ['gulp', 'test:acceptance:protractor']
        SPECS_KEY = 'specs'
        specs = ''.join(sys.argv[2:])

        if (SPECS_KEY in specs):
            gulp_command.append('--' + ''.join(specs))
        try:
            subprocess.check_call(gulp_command)
        except subprocess.CalledProcessError:
            sys.exit(1)
        finally:
            self.teardown()

    def set_env_test_url(self):
        server_thread = StaticLiveServerTestCase.server_thread
        os.environ['TEST_HTTP_HOST'] = server_thread.host
        os.environ['TEST_HTTP_PORT'] = str(server_thread.port)

    def setup_databases(self, **kwargs):
        dbs = super(AcceptanceTestRunner, self).setup_databases(**kwargs)
        test_data.run()
        return dbs

    def teardown(self):
        self.teardown_databases(self.dbs)
        self.teardown_test_environment()
        StaticLiveServerTestCase.tearDownClass()

    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        # Disable logging below CRITICAL during tests.
        logging.disable(logging.CRITICAL)

        self.setup_test_environment()
        self.dbs = self.setup_databases()

        # Create a static server, it should start immediately.
        StaticLiveServerTestCase.setUpClass()

        # Set the environment variables used by Protractor.
        self.set_env_test_url()

        self.run_suite()

        return


class HtmlMixin(object):
    def assertHtmlRegexpMatches(self, s, r):
        s_no_right_spaces = re.sub('>\s*', '>', s)
        s_no_left_spaces = re.sub('\s*([<"])', r'\1', s_no_right_spaces)
        s_no_extra_spaces = re.sub('\s+', ' ', s_no_left_spaces)

        self.assertIsNotNone(
            re.search(r, s_no_extra_spaces.strip(), flags=re.DOTALL),
            '{} did not match {}'.format(s_no_extra_spaces, r)
        )

    def assertPageIncludesHtml(self, page, s):
        request = RequestFactory().get('/')
        request.user = Mock()

        rendered_html = page.serve(request).render()
        try:
            self.assertHtmlRegexpMatches(str(rendered_html), s)
        except AssertionError:
            self.fail('rendered page HTML did not match {}'.format(s))
