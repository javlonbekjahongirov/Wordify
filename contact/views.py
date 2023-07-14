from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request succesfully accepted')
            return redirect('.')

    ctx = {
        'form': form
    }

    return render(request, 'contact/contact.html', ctx)