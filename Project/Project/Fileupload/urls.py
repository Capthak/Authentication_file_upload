from django.urls import path
from .views import document_upload_view,document_show


urlpatterns=[
    path('docupload/',document_upload_view,name='docupload'),
    path('docshow/',document_show,name='docshow')
]

