from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class LogIn(LoginView):
    template_name = 'base_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')



class Register_now(FormView):
    template_name = 'base_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(Register_now,self).form_valid(form)
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Register_now,self).get(*args,**kwargs)
    



class TaskList(LoginRequiredMixin,ListView):
    model = Task 
    context_object_name = 'tasks'
    template_name = 'base_app/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context
        

class TaskDetails(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base_app/task_details.html'
    
    def __str__(self):
        return self.title 

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','complete']
    template_name = 'base_app/task_edit.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)
    

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','complete']
    template_name = 'base_app/task_edit.html'
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')
    template_name = 'base_app/task_confirm_delete.html'

