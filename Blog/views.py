from django.shortcuts import render,HttpResponse,redirect
from .models import Post as PostD
from django.contrib import messages

# Create your views here.

def Blog(r):
     Posts = PostD.objects.all().reverse() 
     if Posts.count() > 2:
          fb = ''
     else:
          fb = 'fixed-bottom'
     return render(r,'Blog/Blog.html',{'Posts':Posts,'Fb':fb}) 


def Add(r):
     if r.user.is_authenticated:
          if r.method == 'POST':
               title =  r.POST['title']
               content = r.POST['content']
               author = r.user.username
               print(author)
               p = PostD(Title=title,Content=content,Author=author)
               p.save()
          return render(r,'Blog/AddPost.html')
     else:
          messages.info(r,'First Login Please')
          return redirect('/Auth/Login')
     

def Post(r,Sno):
    Post = PostD.objects.filter(Sno=Sno).first()
    if not Post:
         return render(r,'Blog/PostNotAvalable.html',{'Fb':'fixed-bottom'})

    else:    
         if len(Post.Content) < 2419:
              fb = 'fixed-bottom'
         else:
              fb = '' 

         return render(r,'Blog/Post.html', {"post": Post,'Fb':fb})
         
    
    