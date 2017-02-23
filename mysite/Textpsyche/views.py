from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm
from .fileforms import UploadFileForm


# Create your views here.

def homeIndex(request):
    return render(request,'Pages/index.html')

def PasteText(request):
    return render(request,'Pages/PasteText.html')

def AboutUs(request):
    return render(request,'Pages/AboutUs.html')

def Contact(request):
    return render(request,'Pages/ContactUs.html')

def upload_file(request):
    msg = "File Uploaded"
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print ("inside POST method")
        if form.is_valid():
            print ("inside valid")
            handle_uploaded_file(request.FILES['file'])
            #return HttpResponseRedirect('/success/url/')
            return render(request,'Pages/Thanks.html',{'posts': msg})
        else :
            print form.errors
    else:
        form = UploadFileForm()
    #return render(request, 'upload.html', {'form': form})
    return render(request,'Pages/Thanks.html',{'posts': msg})

def handle_uploaded_file(f):
    with open('C:\\Users\\Harikrishnan\\Django-Project\\mysite\\Textpsyche/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def getText(request):
    msg = "hi"
    print ("Starting")
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        print ("Checking validity")
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print ("It is valid")
            #print(form.cleaned_data['hello'])
            msg = form.cleaned_data.get('for_analysis')
            print (msg)
        else:
            print form.errors


            # ...
            # redirect to a new URL:
            return render(request,'Pages/Thanks.html',{'posts': msg})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        #msg = form.cleaned_data['text_toB_Analyzed']

    return render(request,'Pages/Thanks.html',{'posts': msg})
    #return HttpResponse('<h2>'+form.text_toB_Analyzed+'</h2>')
    #return HttpResponseRedirect(request, 'Pages/ContactUs.html')
