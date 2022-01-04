from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
@login_required
def admin(request):
    if request.user.is_staff:
        
        messages = Contact.objects.all().order_by('-id')
        # paginating messages from the contact model
        paginator = Paginator(messages, 4)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # feedbacks
        feedbacks = Feedback.objects.all().order_by('-id')
            # paginating feedbacks from the Feedback model
        paginator = Paginator(feedbacks, 4)

        page_number = request.GET.get('page')
        feedback_obj = paginator.get_page(page_number)

        # paginate projects table
        item_list = Projects.objects.all().order_by('-id')
        page = request.GET.get('page', 1)

        paginator = Paginator(item_list, 15)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        form = ProjectsForm()

        if request.method == "POST":
            form = ProjectsForm(request.POST, request.FILES)
            files = request.FILES.getlist('more_project_images')
            if form.is_valid():
                project = form.save()
                for f in files:
                    project_image = ProjectImages(project=project, image=f)
                    project_image.save()

                return redirect('admin')    
        context = {
            'page_obj': page_obj,
            'feedback_obj':feedback_obj,
            'form': form,
            'items':items
        }
        return render(request, 'admin.html', context)
    messages.danger(request, "You can't access the admin panel because you are not the admin ")
    return redirect('home')  


def home(request):
    partners = Partners.objects.all().order_by('-id')
    testimonies = Feedback.objects.all().order_by('-id')
    projects = Projects.objects.all().order_by('-id')[:9]
    carousel = [Projects.objects.latest('id')][:3]

    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home') 
    context= {
        'carousel':carousel,
        'partners':partners,
        'testimonies':testimonies,
        'projects':projects,
        'form': form
    }
    return render (request, 'home.html', context)

def allProjects(request):
    carousel = [Projects.objects.latest('id')][:3]
    projects = Projects.objects.all().order_by('-id')

    context = {
        'projects':projects,
        'carousel':carousel
    }
    return render(request, 'allprojets.html', context)    

def allServices(request):
    return render(request, 'allprojets.html')     

def feedback(request):
    form = FeedbackForm()

    if request.method == "POST":
        form = FeedbackForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')    
    context ={
        "form": form
    }
    return render(request, 'feedback.html', context)    


def project_details(request, id):

    projects = Projects.objects.filter(id=id)
    context = {
        'projects': projects
    }
    return render(request, 'project-details.html', context)

def delete_message(request, id):
    message = Contact.objects.get(id=id)
    message.delete()
    return redirect('admin')   


def delete_project(request, id):
    project = Projects.objects.get(id=id)
    project.delete()

    return redirect ('admin')

def delete_feedback(request, id):
    feedback = Feedback.objects.get(id=id)
    feedback.delete()

    return redirect ('admin')    


def updateProject(request, id):
    project = Projects.objects.get(id=id)
    form = ProjectsForm(instance=project)

    if request.method == "POST":
        form = ProjectsForm(request.POST or None, request.FILES, instance=project)

        if form.is_valid():
            
            form.save()
            return redirect('admin')
    context ={
        'project': project,
        'form': form

    }
    return render(request, 'admin-update-projects.html', context)
@login_required
def adminPartners(request):
    companies = Partners.objects.all().order_by('-id')
            # paginating feedbacks from the Feedback model
    paginator = Paginator(companies, 4)

    page_number = request.GET.get('page')
    company_obj = paginator.get_page(page_number)

    partners = PartnersForm()  
    if request.method == "POST":
        partners = PartnersForm(request.POST, request.FILES)
        if partners.is_valid():
            partners.save()

        return redirect('adminpartners') 
    context ={
        'partners': partners,
        'company_obj':company_obj

    }
    return render(request, 'admin-partners.html', context)       

def deletePartner(request, id):
    partner = Partners.objects.get(id=id)
    partner.delete()

    return redirect ('adminpartners')


# def update_blog(request, id):
#     blog = Blog().objects.get(id=id)
#     form = BlogForm()(request.POST or None, instance=item)
#     if form.is_valid():
#         form.save()
#         return redirect('admin')
#     context ={
#         'blog': blog,
#         'form': form

#     }
#     return render(request, 'admin-update-blog.html', context)    
