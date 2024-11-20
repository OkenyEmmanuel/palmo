from django.shortcuts import render, HttpResponse
from .models import Student, Category,Subcategory,Landing,Logo,VideoBanner

from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Category
# Create your views here.
def index(request):
    dests = Category.objects.all()
    land = Landing.objects.all()[:7] 
    logo = Logo.objects.first()
    vid = VideoBanner.objects.first()
    return render(request, 'josh.html', {'dests': dests, 'land': land, 'logo':logo, 'vid':vid})


class CategoryDetailView(View):
    template_name = 'category.html'

    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        subcategories = category.categories.all()
        return render(request, self.template_name, {'category': category, 'subcategories': subcategories})

def register(request):
    if request.method == "POST":
        name =request.POST['name']
        tel =request.POST['telephone']
        email = request.POST['email'] 
        place = request.POST['place']
        gen = request.POST['gender']
        status = request.POST['employment']
        obj=Student()
        obj.name=name
        obj.tel=tel
        obj.email=email
        obj.place=place
        obj.gen=gen
        obj.status=status
        obj.save()
        return HttpResponse("<h2>Thank you For Registering With Jonjo Fashions</h2>")
    return render(request, 'index.html')