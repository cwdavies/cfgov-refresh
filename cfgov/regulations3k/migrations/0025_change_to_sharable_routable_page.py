# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-24 20:15
from __future__ import unicode_literals

from django.db import migrations
import v1.atomic_elements.organisms
import v1.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('regulations3k', '0024_add_standard_notification_regs_landing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regulationlandingpage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('notification', wagtail.wagtailcore.blocks.StructBlock((('message', wagtail.wagtailcore.blocks.CharBlock(help_text='The main notification message to display.', required=True)), ('explanation', wagtail.wagtailcore.blocks.TextBlock(help_text='Explanation text appears below the message in smaller type.', required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False)))), help_text='Links appear on their own lines below the explanation.', required=False))))), ('full_width_text', wagtail.wagtailcore.blocks.StreamBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock(icon='edit')), ('content_with_anchor', wagtail.wagtailcore.blocks.StructBlock((('content_block', wagtail.wagtailcore.blocks.RichTextBlock()), ('anchor_link', wagtail.wagtailcore.blocks.StructBlock((('link_id', wagtail.wagtailcore.blocks.CharBlock(help_text='\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label='ID for this content block', required=False)),)))))), ('heading', wagtail.wagtailcore.blocks.StructBlock((('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#the-icons">See full list of icons</a>', required=False))), required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailcore.blocks.StructBlock((('upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.wagtailcore.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))))), ('image_width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('full', 'full'), (470, '470px'), (270, '270px'), (170, '170px')])), ('image_position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('right', 'right'), ('left', 'left')], help_text='Does not apply if the image is full-width')), ('text', wagtail.wagtailcore.blocks.RichTextBlock(label='Caption', required=False)), ('is_bottom_rule', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='Check to add a horizontal rule line to bottom of inset.', label='Has bottom rule line', required=False))))), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('quote', wagtail.wagtailcore.blocks.StructBlock((('body', wagtail.wagtailcore.blocks.TextBlock()), ('citation', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('is_large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('cta', wagtail.wagtailcore.blocks.StructBlock((('slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('button', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False)), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')])))))))), ('related_links', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False))))))))), ('reusable_text', v1.blocks.ReusableTextChooserBlock('v1.ReusableText')), ('email_signup', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('gd_code', wagtail.wagtailcore.blocks.CharBlock(help_text='Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label='GovDelivery code', required=False)), ('disclaimer_page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))))), ('regulations_list', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(help_text='Regulations list heading', required=False)), ('more_regs_page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text='Link to more regulations')), ('more_regs_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Text to show on link to more regulations', required=False))))))))), blank=True),
        ),
        migrations.AlterField(
            model_name='regulationlandingpage',
            name='header',
            field=wagtail.wagtailcore.fields.StreamField((('hero', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(help_text='For complete guidelines on creating heroes, visit our <a href="https://cfpb.github.io/design-manual/global-elements/heroes.html">Design Manual</a>.<ul class="help">Character counts (including spaces) at largest breakpoint:<li>&bull; 41 characters max (one-line heading)</li><li>&bull; 82 characters max (two-line heading)</li></ul>', required=False)), ('body', wagtail.wagtailcore.blocks.RichTextBlock(help_text='<ul class="help">Character counts (including spaces) at largest breakpoint:<li>&bull; 165-186 characters (after a one-line heading)</li><li>&bull; 108-124 characters (after a two-line heading)</li></ul>', label='Sub-heading', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='When saving illustrations, use a transparent background. <a href="https://cfpb.github.io/design-manual/global-elements/heroes.html#style">See image dimension guidelines.</a>', label='Large image', required=False)), ('small_image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='<b>Optional.</b> Provides an alternate image for small displays when using a photo or bleeding hero. Not required for the standard illustration. <a href="https://cfpb.github.io/design-manual/global-elements/heroes.html#style">See image dimension guidelines.</a>', required=False)), ('background_color', wagtail.wagtailcore.blocks.CharBlock(help_text='Specify a hex value (with the # sign) from our <a href="https://cfpb.github.io/design-manual/brand-guidelines/color-principles.html">official color palette</a>.', required=False)), ('is_overlay', wagtail.wagtailcore.blocks.BooleanBlock(help_text='<b>Optional.</b> Uses the large image as a background under the entire hero, creating the "Photo" style of hero (see <a href="https://cfpb.github.io/design-manual/global-elements/heroes.html">Design Manual</a> for details). When using this option, make sure to specify a background color (above) for the left/right margins that appear when screens are wider than 1200px and for the text section when the photo and text stack at mobile sizes.', label='Photo', required=False)), ('is_white_text', wagtail.wagtailcore.blocks.BooleanBlock(help_text='<b>Optional.</b> Turns the hero text white. Useful if using a dark background color or background image.', label='White text', required=False)), ('is_bleeding', wagtail.wagtailcore.blocks.BooleanBlock(help_text='<b>Optional.</b> Select if you want the illustration to bleed vertically off the top and bottom of the hero space.', label='Bleed', required=False))))),), blank=True),
        ),
        migrations.AlterField(
            model_name='regulationpage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('info_unit_group', wagtail.wagtailcore.blocks.StructBlock((('format', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('50-50', '50/50'), ('33-33-33', '33/33/33'), ('25-75', '25/75')], help_text='Choose the number and width of info unit columns.', label='Format')), ('heading', wagtail.wagtailcore.blocks.StructBlock((('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#the-icons">See full list of icons</a>', required=False))), required=False)), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(help_text='If this field is not empty, the Heading field must also be set.', required=False)), ('link_image_and_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text="Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", required=False)), ('has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of info unit group.', required=False)), ('lines_between_items', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Check this to show horizontal rule lines between info units.', label='Show rule lines between items', required=False)), ('info_units', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailcore.blocks.StructBlock((('upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.wagtailcore.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))))), ('heading', wagtail.wagtailcore.blocks.StructBlock((('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#the-icons">See full list of icons</a>', required=False))), default={'level': 'h3'}, required=False)), ('body', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False)))), required=False)))))), ('sharing', wagtail.wagtailcore.blocks.StructBlock((('shareable', wagtail.wagtailcore.blocks.BooleanBlock(help_text='If checked, share links will be included below the items.', label='Include sharing links?', required=False)), ('share_blurb', wagtail.wagtailcore.blocks.CharBlock(help_text='Sets the tweet text, email subject line, and LinkedIn post text.', required=False)))))))), ('full_width_text', wagtail.wagtailcore.blocks.StreamBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock(icon='edit')), ('content_with_anchor', wagtail.wagtailcore.blocks.StructBlock((('content_block', wagtail.wagtailcore.blocks.RichTextBlock()), ('anchor_link', wagtail.wagtailcore.blocks.StructBlock((('link_id', wagtail.wagtailcore.blocks.CharBlock(help_text='\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label='ID for this content block', required=False)),)))))), ('heading', wagtail.wagtailcore.blocks.StructBlock((('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#the-icons">See full list of icons</a>', required=False))), required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailcore.blocks.StructBlock((('upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.wagtailcore.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))))), ('image_width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('full', 'full'), (470, '470px'), (270, '270px'), (170, '170px')])), ('image_position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('right', 'right'), ('left', 'left')], help_text='Does not apply if the image is full-width')), ('text', wagtail.wagtailcore.blocks.RichTextBlock(label='Caption', required=False)), ('is_bottom_rule', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='Check to add a horizontal rule line to bottom of inset.', label='Has bottom rule line', required=False))))), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('quote', wagtail.wagtailcore.blocks.StructBlock((('body', wagtail.wagtailcore.blocks.TextBlock()), ('citation', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('is_large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('cta', wagtail.wagtailcore.blocks.StructBlock((('slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('button', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False)), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')])))))))), ('related_links', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False))))))))), ('reusable_text', v1.blocks.ReusableTextChooserBlock('v1.ReusableText')), ('email_signup', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('gd_code', wagtail.wagtailcore.blocks.CharBlock(help_text='Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label='GovDelivery code', required=False)), ('disclaimer_page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))))))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='regulationpage',
            name='header',
            field=wagtail.wagtailcore.fields.StreamField((('text_introduction', wagtail.wagtailcore.blocks.StructBlock((('eyebrow', wagtail.wagtailcore.blocks.CharBlock(help_text='Optional: Adds an H5 eyebrow above H1 heading text. Only use in conjunction with heading.', label='Pre-heading', required=False)), ('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False)))), required=False)), ('has_rule', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Check this to add a horizontal rule line to bottom of text introduction.', label='Has bottom rule', required=False))))),), blank=True),
        ),
    ]
