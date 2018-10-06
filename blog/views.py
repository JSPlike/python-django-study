from django.shortcuts import render

from django.views.generic import ListView, DetailView
from blog.models import Blog


# Create your views here.

#--- ListView
class BlogLV(ListView):
	model = Blog
		

#--- DetailView
class BlogDV(DetailView):
	model = Blog