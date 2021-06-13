from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.conf import settings
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    # posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts_list = Post.objects.filter(status="published")
    paginator = Paginator(posts_list, 3)  # change this to accommodate number of posts per page
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'page': page
    }

    return render(request, 'blog/post_list.html', context, )
    #  {'base_dir': settings.BASE_DIR,})


def author_post_list(request):
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(posts_list, 2)  # change this to accommodate number of posts per page
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'page': page
    }

    return render(request, 'blog/author_post_list.html', context, )
    # {'base_dir': settings.BASE_DIR})


def category(request, slug):
    cat = Category.objects.get(slug=slug)

    context = {
        'category': cat,
    }

    return render(request, 'blog/category.html', context)
    #   {'base_dir': settings.BASE_DIR,})


def blog_post(request, slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug, status='published')

    context = {
        'post': post
    }

    return render(request, 'blog/blog_post.html', context)

# Individual Post
# breadcrumb links
# Recent Articles
# Add Category to Model and then to Blog roll and single article page
    # Category links
    # Category flatpages
# ensure links works link from blog roll, from blog_post
# Author Page
# link from blog roll, from blog_post
# replace existing author name with user and image - DONE
# own model?
# Meta description and title updated to match page / post
# SEARCH: https://www.codesnail.com/building-a-search-functionality-django-blog-9/
# SITEMAP: https://www.codesnail.com/adding-a-sitemap-to-the-website-django-blog-10/


# MODELS:
# Author Model can have one to many relation to posts - DONE
    # Twitter, LinkedIn, Website, Instagram, YouTube, Bio, author-slug, name, picture
    # Create Author Bio component
    # Add to template files
# Tag model can have one to many relation to posts
# tag name, tag-slug


# website
# Breadcrumbs
# add the rest of the flatpages
# Mailchimp
# Main Menu from all flatpages
