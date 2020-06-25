import re

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from customer.models import Customer, PaymentRecord, Bin


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    '''
    Splits the query string in invidual keywords, getting rid of unecessary spaces and grouping quoted words together.
    Example:
    >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    '''

    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    '''
    Returns a query, that is a combination of Q objects.
    That combination aims to search keywords within a model by testing the given search fields.
    '''

    query = None  # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


@login_required
def dashboard(request):
    all_customers = Customer.objects.all().order_by('-id')
    all_employees = get_user_model().objects.all().order_by('-id').count()
    all_bins = Bin.objects.all().order_by('-id').count()
    all_payment_records = PaymentRecord.objects.all()
    total_revenue = 0
    for record in all_payment_records:
        total_revenue = total_revenue + record.amount_paid

    num_of_customers = all_customers.count()
    some_customers = all_customers[:20]
    args = {
        'customers': some_customers,
        'num_of_customers': num_of_customers,
        'all_employees': all_employees,
        'all_bins': all_bins,
        'total_revenue': total_revenue,
    }
    return render(request, "customer/dashboard.html", args)


@login_required
def customers(request):
    all_customers = Customer.objects.all()
    args = {'customers': all_customers}
    return render(request, "customer/customers.html", args)


@login_required
def payment_records(request):
    all_payments = PaymentRecord.objects.all()
    args = {'payments': all_payments}
    return render(request, "customer/payment_record.html", args)


@login_required
def bins(request):
    all_bins = Bin.objects.all()
    args = {'bins': all_bins}
    return render(request, "customer/bins.html", args)


@login_required
def employees(request):
    args = {'form': ""}
    return render(request, "customer/tables.html", args)


@login_required
def maps(request):
    args = {'form': ""}
    return render(request, "customer/maps.html", args)
