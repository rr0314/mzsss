from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


def home(request):
	return render(request,'index.html')


from django.shortcuts import render, redirect
from .models import candidate, employer

def cform(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        cemail = request.POST.get('cemail')
        cphone = request.POST.get('cphone')
        dob = request.POST.get('dob')
        cfile = request.FILES['cfile']
        cadress = request.POST.get('cadress')
        qualification = request.POST.get('qualification')
        exp = request.POST.get('exp')
        addskill = request.POST.get('addskill')
        mrg = request.POST.get('mrg')
        job1 = request.POST.get('job1')
        job2 = request.POST.get('job2')
        resume = request.FILES['resume']

        # Save candidate information to the database
        candidate_obj = candidate(
            cname=cname,
            cemail=cemail,
            cphone=cphone,
            dob=dob,
            cfile=cfile,
            cadress=cadress,
            qualification=qualification,
            exp=exp,
            addskill=addskill,
            mrg=mrg,
            job1=job1,
            job2=job2,
            resume=resume,
        )
        candidate_obj.save()

        return redirect('/success/')

    context = {}
    return render(request, 'cform.html', context)

def emform(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        femail = request.POST.get('femail')
        fphone = request.POST.get('fphone')
        fweb = request.POST.get('fweb')
        orgen = request.POST.get('orgen')
        secen = request.POST.get('secen')
        job_file = request.FILES['job_file']
        ename = request.POST.get('ename')
        desig = request.POST.get('desig')
        connum = request.POST.get('connum')
        conemail = request.POST.get('conemail')

        # Save employer information to the database
        employer_obj = employer(
            fname=fname,
            femail=femail,
            fphone=fphone,
            fweb=fweb,
            orgen=orgen,
            secen=secen,
            job_file=job_file,
            ename=ename,
            desig=desig,
            connum=connum,
            conemail=conemail
        )
        employer_obj.save()

        return redirect('/success/')

    context = {}
    return render(request, 'emform.html', context)

def success(request):
    return render(request, 'success.html', {})



def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def faq(request):
    return render(request, 'faq.html')

def eform(request):
    return render(request, 'eform.html')
def gallery(request):
    return render(request, 'gallery.html')

def incform(request):
    return render(request, 'incform.html')

def mal(request):
    return render(request, 'mal.html')

def members(request):
    return render(request, 'members.html')

def service(request):
    return render(request, 'service.html')