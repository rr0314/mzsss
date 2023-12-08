from django.db import models

# Create your models here.

class candidate(models.Model):
    cname=models.CharField(max_length=50,null='empty')
    cemail=models.CharField(max_length=100,null='empty')
    cphone=models.CharField(max_length=20,null='empty')
    dob=models.DateField(max_length=20,null='empty')
    cfile=models.FileField(upload_to="cand_img",null='empty')
    cadress=models.CharField(max_length=500,null='empty')
    qualification=models.TextField(null='empty')
    exp=models.CharField(max_length=50,null='empty')
    addskill=models.CharField(max_length=200,null='empty')
    mrg=models.CharField(max_length=50,null='empty')
    job1=models.CharField(max_length=50,null='empty')
    job2=models.CharField(max_length=50,null='empty')
    resume=models.FileField(upload_to="cand_resume",null='empty')


class employer(models.Model):
    fname=models.CharField(max_length=200,null='empty')
    femail=models.CharField(max_length=200,null='empty')
    fphone=models.CharField(max_length=200,null='empty')
    fweb=models.CharField(max_length=200,null='empty')
    orgen=models.CharField(max_length=200,null='empty')
    secen=models.CharField(max_length=200,null='empty')
    job_file=models.FileField(upload_to="employer_file",null='empty')
    ename=models.CharField(max_length=200,null='empty')
    desig=models.CharField(max_length=200,null='empty')
    connum=models.CharField(max_length=200,null='empty')
    conemail=models.CharField(max_length=200,null='empty')
    