from django.shortcuts import redirect, render
from .models import AdminMessage

def showAdd(request):
    data=AdminMessage.objects.all()
    return render(request,'viewsAdmin.html',{'data':data})




def addAd(request):
    print('test')
    if request.method=='POST':
        AdminMessage.objects.create(nom_ad=request.POST.get('nom_ad'),prenom_ad=request.POST.get('prenom_ad'),pass_ad=request.POST.get('pass_ad'))
        return redirect('showAdd')
    return render(request,'formulaireAdd_ad.html')


def searchId(request,id_ad):
    data=AdminMessage.objects.get(pk=id_ad)
    return render(request,'formChange_ad.html',{'data':data})

def changeAd(request):
    
    if request.method=='POST':
        id=request.POST.get('id_ad')
        utilisateur=AdminMessage.objects.get(pk=id)
        if request.method=='POST':
            utilisateur.nom_ad=request.POST.get('nom_ad')
            utilisateur.prenom_ad=request.POST.get('prenom_ad')
            utilisateur.pass_ad=request.POST.get('pass_ad')
            utilisateur.save()
            return redirect('showAdd')
    return render(request,'formChange_ad.html')


    
def deleteAd(request,id_ad):
    print('hrfhfjgej')
    id=AdminMessage.objects.get(pk=id_ad)
    id.delete()
    return redirect('showAdd')
