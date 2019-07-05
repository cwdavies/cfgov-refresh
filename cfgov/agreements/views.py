from django.core.paginator import (
    EmptyPage, InvalidPage, PageNotAnInteger, Paginator
)
from django.http import Http404
from django.shortcuts import render

from agreements import RESULTS_PER_PAGE
from agreements.models import Agreement, Entity, Issuer, Prepaid


def index(request):
    return render(request, 'agreements/index.html', {
        'agreement_count': Agreement.objects.all().count(),
        'pagetitle': 'Credit card agreements',
    })


def issuer_search(request, issuer_slug):
    issuers = Issuer.objects.filter(slug=issuer_slug)

    if not issuers.exists():
        raise Http404

    agreements = Agreement.objects.filter(issuer__in=issuers)

    if agreements.exists():
        issuer = agreements.latest('pk').issuer
    else:
        issuer = issuers.latest('pk')

    pager = Paginator(
        agreements.order_by('file_name'),
        RESULTS_PER_PAGE
    )

    try:
        page = pager.page(request.GET.get('page'))
    except PageNotAnInteger:
        page = pager.page(1)
    except EmptyPage:
        page = pager.page(pager.num_pages)

    return render(request, 'agreements/search.html', {
        'page': page,
        'issuer': issuer,
    })


def validate_page_number(request, paginator):
    """
    A utility for parsing a pagination request,
    catching invalid page numbers and always returning
    a valid page number, defaulting to 1.
    """
    raw_page = request.GET.get('page', 1)
    try:
        page_number = int(raw_page)
    except ValueError:
        page_number = 1
    try:
        paginator.page(page_number)
    except InvalidPage:
        page_number = 1
    return page_number


def prepaid(request):
    products = Prepaid.objects.exclude(issuer_name__contains='**')
    total_count = len(products)
    paginator = Paginator(products, 20)
    page_number = validate_page_number(request, paginator)
    page = paginator.page(page_number)
    return render(request, 'agreements/prepaid.html', {
        'current_page': page_number,
        'results': page,
        'total_count': total_count,
        'paginator': paginator,
        'issuers': Entity.objects.exclude(
            name__contains='**').order_by('name'),
        'current_count': '',
        'query': ''
    })
