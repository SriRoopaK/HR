from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
import mimetypes
import fpdf


sample_text = "No text " *100


def convertTextToDoc(text):
    file = open("temporary.txt", 'w')
    file.writelines(text)
    file.close()

def convertTextToPdf(text):
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.write(5, text)
    pdf.ln()
    pdf.output("temporary.pdf")

# Create your views here.
class IndexView(View):

    def get(self, request):
        form = IndexForm()
        return render(request, 'handwriting_recognition/index.html', {'form': form})

    def post(self, request):
        form = IndexForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/processing/')


def img_to_text():
    pass


def processing(request):
    #img_to_text()
    context = dict()
    context['text'] = "Processing"
    return render(request, 'handwriting_recognition/processing.html', context)


def show_output(request, text_data="No text"):
    context = dict()
    context['text'] = text_data
    return render(request, 'handwriting_recognition/output.html', context)

def savingDOC(request, text=sample_text):
    convertTextToDoc(text)
    fl_path = "C:\PythonCourse\\finalproject\\finalproject\\temporary.txt"
    filename = 'file.txt'
    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def savingPDF(request, text=sample_text):
    convertTextToPdf(text)
    fl_path = "C:\PythonCourse\\finalproject\\finalproject\\temporary.pdf"
    filename = 'file.pdf'

    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


