from django.shortcuts import render,redirect
from .forms import DocumentMdelForm
from .models import Document

# Create your views here.
def document_upload_view(request):
    if request.method=='POST':
        form=DocumentMdelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=DocumentMdelForm()
    return render(request,'Fileupload/newfileupload.html',{'form':
    form})

def document_show(request):
    file=Document.objects.all()
    template_name='Fileupload/showfile.html'
    context={'file':file}
    return render(request,template_name,context)

