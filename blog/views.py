from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail

# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/index.html')
    

class LandscapeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/landscape.html')
    

class PortraitView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/portrait.html')
    

class BlogView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by('-id')
        return render(request, 'blog/blog.html', {'post_data': post_data})

class Post_detailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'blog/post_detail.html', {'post_data': post_data})

class Post_newView(View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        return render(request, 'blog/post_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post()
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.text = form.cleaned_data['text']
            if request.FILES:
                post_data.image = request.FILES.get('image')
            post_data.save()
            return redirect('post_detail', post_data.id)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

class Post_editView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = PostForm(
            request.POST or None,
            initial = {
                'title': post_data.title,
                'text': post_data.text,
                'image': post_data.image,
            }
        )
        return render(request, 'blog/post_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post.objects.get(id=self.kwargs['pk'])
            post_data.title = form.cleaned_data['title']
            post_data.text = form.cleaned_data['text']
            if request.FILES:
                post_data.image = request.FILES.get('image')
            post_data.save()
            return redirect('post_detail', self.kwargs['pk'])
        else:
            form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})

class Post_deleteView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'blog/post_delete.html', {'post_data': post_data})

    def post(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        return redirect('blog')

    
        


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        return render(request, 'blog/contact.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ContactForm(request.POST)

            if form.is_valid():
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                sender = []
                sender.append(form.cleaned_data['sender'])
                myself = form.cleaned_data['myself']
                recipients = [settings.EMAIL_HOST_USER]

                if myself:
                    recipients.append(sender)
                try:
                    send_mail(subject, message, sender, recipients)
                except BadHeaderError:
                    return HttpResponse('無効なヘッダーが見つかりました。')
                return redirect('contact_complete')
        else:
            form = ContactForm()
        return render(request, 'blog/contact.html', {'form': form})

class Contact_completeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/contact_complete.html')




class AboutmeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/aboutme.html')
    