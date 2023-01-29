from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.views.generic.base import ContextMixin

from .models import Post, Tag, Category
from .form import ContactForm, PostForm, PostCategoryForm
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def main_view(request):
    posts=Post.objects.all()
    paginator=Paginator(posts, 2)
    # posts = Post.objects.filter(is_active=True)
    # Posts = Post.active_objects.all()
    # paginator = Paginator(posts, 5)
    page=request.GET.get('page')
    try:
        posts=paginator.page(1)
    exept PageNotAnInteger
        posts = paginator.page(1)
    exept EmptyPage
        posts=paginator.page(paginator.num_pages)

    title="главная страница"
    # title=title.capitalize()
    return render (request, 'blogapp/index.html', context={'posts': posts, "title": title})

    return render(request,"blogapp/index.html", context={'posts':posts})

def contact_view (request):
    if request.method == "POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            message=form.cleaned_data['message']
            email=form.cleaned_data['email']
            send_mail(
                'Contact message',
                f'ваше сообщение {message} приянто,
                'from@example.com',
                [email],

                fail_silently=True,
            )
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            return render(request, "blogapp/contact.html", context={'form': form})
    else:
        form = ContactForm()
        return render(request, "blogapp/contact.html", context={'form':form})

@user_passes_test(lambda u: u.is_superuser)
def post(request,id):
    post=get_object_or_404(Post, id=id)
    post=Post.objects.get(id=id)
    return render(request, "blogapp/post.html", context={'post': post})


@login_required
def create_post(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "blogapp/create.html", context={'post': form})
    else:
        form=PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            return render(request, "blogapp/create.html", context={'form': form})

        class NameContextMixin(ContextMixin):
            def get_context_data(self, *args, **kwargs):

                context = super().get_context_data(*args, **kwargs)
                context['name'] = "Теги"
                return context


        class TagListView(ListView, NameContextMixin):
            model= Tag
            template_name = "blogapp/tag_list.html"
            context_object_name ="tags"
            paginate_by = 5



            def get_queryset(self):

                # return Tag.objects.all()
                return Tag.objects.filter(is_active=True)
                return Tag.active.objects.all()

        class TagDetailView (UserPassesTestMixin,DetailView, NameContextMixin):
            model = Tag
            template_name = "blogapp/tag_detail.html"

            def test_func(self):
                return self.request.user.is_supruser
            

        def get(self, request, *args, **kwargs):
            self.tag_id=kwargs['pk']
            return super().get(request, *args, **kwargs)


        def get_context_data(self, *args, **kwargs):
            contex =super().get_context_data(*args,**kwargs)
            context['name'] = 'Теги'
            return contex

        def get_object(self, queryset=None):
            return get_object_or_404(Tag,pk=self.tag_id)

        class TagCreateView(LoginRequiredMixin, CreateView, NameContextMixin):
# form_class=
        fields = '__all__'
        model=Tag
        success_url=reverse_lazy("blog:tag_list")
        template_name="blogapp/tag_create.html"

        def post(self,request, *args, **kwargs):
            return super().post(request, *args, **kwargs)


        def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)


        class TagUpDateView(UpDateView):
            fields = '__all__'
            model = Tag
            success_url = reverse_lazy("blog:tag_list")
            template_name = "blogapp/tag_create.html"

        class TagDeleteView(DeleteView):
            template_name="blogapp/tag_delete.confirm.html"
            model = Tag
            success_url = reverse_lazy("blog:tag_list")


        class CategoryDetailView(DetailView):
            template_name="blogapp/category_detail.html"
            model=Category

            def get_context_data(self, **kwargs):
                context=super().get_context_data(**kwargs)
                context=PostCategoryForm()
                return context

class PostCategoryCreateView(CreateView):
    model = Post
    template_name ="blogapp/category_detail.html"
    success_url = reverse_lazy("")
    form_class = PostCategoryForm

    def Post(self, request, *args, **kwargs):
        self.category_pk=kwargs['pk']
        return super().Post(request, *args, **kwargs)


    def form_valid(self, form):
        user=self.request.user
        form.instance.user=user
        category=get_object_or_404(Category, pk=self.category_pk)
        form.instance.category=category
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:category_detail', kwargs={'pk': self.category_pk})




