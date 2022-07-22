
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from listings.models import Band, Listing

from listings.forms import ContactUsForm
from django.core.mail import send_mail 

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',
    {'bands': bands});


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html',
    {'band':band}) #nous passons l'id au template


def about(request):
    return render(request, 'listings/about.html');

def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html',
    {'listings': listings});

def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, 'listings/listing_detail.html',
    {'listing':listing})

def contact(request):
    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )

        return redirect('email-sent')
    # if the form is not valid, we let execution continue to the return
    # statement below, and display the form again (with errors).

    else:
        # this must be a GET request, so create an empty form
        form = ContactUsForm()

    return render(request,
            'listings/contact.html',
            {'form': form})