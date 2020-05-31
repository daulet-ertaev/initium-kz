from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Donation
import stripe

stripe.api_key = "sk_test_xXD6TM1XxNLYoJXPSrpeUZZU00M248MJdD"

def home(request):
    context = {
        'posts': Post.objects.all().order_by('-publish')[:3]
    }
    return render(request, 'post/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'post/posts.html'
    context_object_name = 'posts'
    category = ''


    #paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'post/user-posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-created')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'body','category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'post/about.html', {'title': 'About'})

def donationPage(request):
    return render(request,'post/donationPage.html')

def charge(request):

    if request.method == 'POST':
        amount = request.POST['amount']
        amount = int(amount)
        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.user,
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='usd',
            description='Donation',
        )

    return redirect(reverse('success', args=[amount]))

def success(request, args):
    amount = args
    return render(request,'post/success.html', {'amount':amount})

def paypal(request, args, pk, pid):
    if request.method=="POST":
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n\n\n\n\n\n\n\n")
    return render(request, 'post/PayPal.html',{'amount':args, "pk":pk, "pid":pid})

def showPost(request, args):
    posts = Post.objects.filter(category=args,status='published')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    # try:
    #     postsPages = paginator.page(page)
    # except PageNotAnInteger:
    #     postsPages = paginator.page(1)
    # except EmptyPage:
    #     postsPages = paginator.page(paginator.num_pages)

    return render(request,'post/posts.html', {'category':args, 'posts': posts})

def posts(request):
    posts = Post.objects.all()
    return render(request, 'post/posts.html', {'posts': posts})

def paypalCharge(request, pk,pid):
    if request.method == 'POST':
        amount = request.POST['amount']
        amount = int(amount)
    return redirect(reverse('paypal', args=[amount, pk, pid]))

def paypalAmount(request,pk,pid):
    return render(request, 'post/paypalAmount.html',{"pk":pk,"pid":pid})

def test(request):
    return render(request, 'post/pp.html')

def history(request, pk):
    print("aksjdnakjsdnkajsdnkjansdkjnaksdnakjsd",pk)
    donations = Donation.objects.filter(post=pk)

    return render(request, 'post/history.html',{'donations':donations})