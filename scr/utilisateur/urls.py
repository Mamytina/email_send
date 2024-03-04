from django.urls import path
from adminMessage.views import showAdd
from .views import *

urlpatterns = [
    path('',login_user,name='login'),
    path('logout_out',logout_out,name='logout_out'),
    path('showUtil',showUtil,name='showUtlisateur'),
    path('addUtil',addUtil,name='addUtil'),
    path('addUtil_u',addUtil_u,name='addUtil_u'),
    path('formChange/<int:id_util>',searchId,name='formChange'),
    path('changeUtil',changeUtil,name='changeUtil'),
    path('runToPage',runToPage,name='runToPage'),
    path('deleteUtil/<int:id_util>',deleteUtil,name='deleteUtil'),
    path('sendEmail',sendEmail,name='sendEmail'),
    path('showAdd',showAdd,name='showAdd'),

]