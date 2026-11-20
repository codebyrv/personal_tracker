from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
    def get(self,request):
        return render(request,'dashboard.html') 
    
    
    

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Category, Task


# Home Dashboard
class HomeView(TemplateView):

    def get(self, request):
        return render(request, 'dashboard.html')


# Category Management
class CategoryView(TemplateView):

    def get(self, request):
        categories = Category.objects.all()

        return render(request, 'category.html', {
            'categories': categories
        })

    def post(self, request):

        name = request.POST.get('name')
        description = request.POST.get('description')
        color = request.POST.get('color')

        if name:
            Category.objects.create(
                name=name,
                description=description,
                color=color
            )

        return redirect('category')
    
    
    

class TaskView(TemplateView):

    def get(self, request):

        tasks = Task.objects.all()
        categories = Category.objects.all()

        return render(request, 'tracker/task.html', {
            'tasks': tasks,
            'categories': categories
        })

    def post(self, request):

        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '')
        priority = request.POST.get('priority')
        category_id = request.POST.get('category')
        due_date = request.POST.get('due_date') or None

        if title and priority in ['Low', 'Medium', 'High']:

            category = Category.objects.filter(
                id=category_id
            ).first() if category_id else None

            Task.objects.create(
                title=title,
                description=description,
                priority=priority,
                category=category,
                due_date=due_date
            )

        return redirect('task')
