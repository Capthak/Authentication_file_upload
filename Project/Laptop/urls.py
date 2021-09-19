from django.urls import path
from .views import LaptopRegister_view,LaptopShow_view


urlpatterns=[
    path('lapreg/',LaptopRegister_view,name='lapreg'),
     path('lapShow/',LaptopShow_view,name='lapShow'),

]

# I'll highly suggest to check if your object is having that particulart 
# {% if object.image_field %}
# <img src={{object.image_field.url}}>
# {% else %}
# <p>No image for this object</p>
# {% endif %}
