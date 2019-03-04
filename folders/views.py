from pathlib import Path
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, CreateView, UpdateView


path='C:/Users/NagaDurga/Documents/'

def dirstruc(request):
	list_dirc=os.listdir(path)
	return render(request,'form.html',{'list_dirc':list_dirc})


def subfoldes(request):
	sub_fold = request.GET.get('id', None)
	sub_folders=os.listdir(path+str(sub_fold))
	print(sub_folders)
	return render(request,'form1.html',{'sub_folders':sub_folders})


def display_list(ListView,subfoldes,dirstruc):
	print(list_dirc)
	context_object_name = 'people'







