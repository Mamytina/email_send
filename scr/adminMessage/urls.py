

from django.urls import  path
from .views import *

urlpatterns = [
      path('showAdd',showAdd,name="showAdd"),
      path('addAd',addAd,name="add_ad"),
      path('formChange_ad/<int:id_ad>',searchId,name='formChange_ad'),
      path('changeAd',changeAd,name='changeAd'),
      path('deleteAd/<int:id_ad>',deleteAd,name='deleteAd'),
]
