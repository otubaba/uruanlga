from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm
from .models import Department


def contact_page(request):

    departments = Department.objects.all()

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Your message has been submitted successfully.'
            )

            return redirect('contact')

    else:

        form = ContactForm()

    return render(
        request,
        'contact/contact.html',
        {
            'form': form,
            'departments': departments
        }
    )