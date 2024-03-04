
from sys import modules
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from adminMessage.models import AdminMessage
from utilisateur.models import Utilisateur
from django.views.decorators.cache import never_cache



def showUtil(request):
    data=Utilisateur.objects.all()
    return render(request,'viewsUtilisateur.html',{'data':data})



def addUtil(request):
    if request.method=='POST':
        Utilisateur.objects.create(nom_util=request.POST.get('nom_util'),prenom_util=request.POST.get('prenom_util'),pass_util=request.POST.get('pass_util'),mail_util=request.POST.get('mail_util'))
        return redirect('showUtlisateur')
    return render(request,'formulaireAddUtil.html')


def addUtil_u(request):
    if request.method=='POST':
        Utilisateur.objects.create(nom_util=request.POST.get('nom_util'),prenom_util=request.POST.get('prenom_util'),pass_util=request.POST.get('pass_util'),mail_util=request.POST.get('mail_util'))
        return redirect('login')
    return render(request,'formulaireAddUtil.html')

def searchId(request,id_util):
    data=Utilisateur.objects.get(pk=id_util)
    return render(request,'formulairechangeUtil.html',{'data':data})

def changeUtil(request):
    
    if request.method=='POST':
        id=request.POST.get('id_util')
        utilisateur=Utilisateur.objects.get(pk=id)
        if request.method=='POST':
            utilisateur.nom_util=request.POST.get('nom_util')
            utilisateur.prenom_util=request.POST.get('prenom_util')
            utilisateur.pass_util=request.POST.get('pass_util')
            utilisateur.mail_util=request.POST.get('mail_util')
            utilisateur.save()
            return redirect('showUtlisateur')
    return render(request,'formulairechangeUtil.html')

def deleteUtil(request,id_util):
    id=Utilisateur.objects.get(pk=id_util)
    id.delete()
    return redirect('showUtlisateur')
    


def runToPage(request):
    if verifier_login(request):
        data=Utilisateur.objects.all()
        return render(request,'pageUtil.html',{'data':data})
    else:
        return redirect('login')

def login_user(request):
   if request.method=='POST': 
       nom_util=request.POST.get('nom_util')
       pass_util=request.POST.get('pass_util')
       
       try:
           user=Utilisateur.objects.get(nom_util=nom_util,pass_util=pass_util)
            
       except Utilisateur.DoesNotExist:
           user=None
           
       try:
            adm=AdminMessage.objects.get(nom_ad=nom_util,pass_ad=pass_util)    
       except AdminMessage.DoesNotExist:
           adm=None
              
       if user is not None:
            
            data = Utilisateur.objects.filter(nom_util=nom_util)
            id_util=[util.pk for util in data]
            nom_util=[util.nom_util for util in data]
            prenom_util=[util.prenom_util for util in data]
            mail_util=[util.mail_util for util in data] 
            
            request.session['id_util']=id_util
            request.session['nom_util']=nom_util
            request.session['prenom_util']=prenom_util
            request.session['mail_util']=mail_util
            print(request.session['nom_util'])
            return redirect('runToPage')
            
            
       elif adm is not None:
         return redirect('showUtlisateur')
       else:
            print("non")
   
   return render(request,'formulaireLogin.html',)


def sendEmail(request):
    if request.method=="POST":
        titre=request.POST.get('titre')
        contenu=request.POST.get('contenu')
        destinataire=request.POST.get('destinataire')
        try:
            send_mail(
                
                titre,
                contenu,
                settings.EMAIL_HOST_USER,
                [destinataire],
                fail_silently=True
            )
            print('coucou')
        except Exception as e:
            print(e)
    return render(request,'pageUtil.html')



@never_cache
def logout_out(request):
    if request.method == 'GET':
        logout(request)
        request.session.flush()
        request.session['id_util']=0
    return redirect('login')

def verifier_login(request):
    if request.session['id_util']==0 :
        print(request.session['id_util'])
        return False
    else:
        return True