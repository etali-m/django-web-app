
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from listings.models import Band, Listing

from listings.forms import BandForm, ContactUsForm, ListingForm
from django.core.mail import send_mail 

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',
    {'bands': bands});


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html',
    {'band':band}) #nous passons l'id au template

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            #create a new band and save it in the db
            band = form.save()
            #redirect to the detail page of the band we just created
            #we can provide the url pattern argument as arguments to redirect function
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
        
    return render(request, 
    'listings/band_create.html',
    {'form': form})


def band_update(request, band_id):
    band = Band.objects.get(id=band_id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_update.html',
    {'form':form})


def about(request):
    return render(request, 'listings/about.html');

def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html',
    {'listings': listings});


def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()

            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()

    return render(request, 
    'listings/listing_create.html',
    {'form':form})

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