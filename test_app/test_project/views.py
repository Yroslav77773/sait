from django.shortcuts import render, redirect
from .forms import TestForm

def my_form_view(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():

            text_field_value = form.cleaned_data['text_field']
            age_field_value = form.cleaned_data['age_field']

            print("Text:", text_field_value)
            print("Age:", age_field_value)


            return redirect('myform')

    else:
        form = TestForm()
    return render(request, 'test.html', {'form': form})


