from django.shortcuts import render, redirect

from .models import Blog
from .forms import BlogForm

def update(request, update_id):
    akun_update = Blog.objects.get(id=update_id)
    data = {
        'nama_depan'    : akun_update.nama_depan,
        'nama_belakang' : akun_update.nama_belakang,
        'username'      : akun_update.username,
    }
    akun_form = BlogForm(request.POST or None, initial=data, instance=akun_update)
    
    if request.method == 'POST':
        if akun_form.is_valid():
            akun_form.save()
        return redirect('blog:list')

    context = {
        'page_title':'Akun Update',
        'akun_form':akun_form,
    }
    return render(request, 'blog/create.html', context)

def delete(request, delete_id):
    Blog.objects.filter(id=delete_id).delete()
    return redirect('blog:list')

def create (request):
    akun_form = BlogForm(request.POST or None)
    if request.method == 'POST':
        if akun_form.is_valid():
            akun_form.save()
        return redirect('blog:list')

    context = {
        'page_title':'Tambah',
        'akun_form':akun_form,
    }
    return render(request, 'blog/create.html', context)

def list(request):
    semua_akun = Blog.objects.all()
    
    context = {
        'page_title':'Sosial media',
        'semua_akun': semua_akun,
    }
    return render (request, 'blog/list.html', context)