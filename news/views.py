from django.shortcuts import render, get_object_or_404
from .models import Article, Category


# 🏠 HOME
def home(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    articles = Article.objects.all().order_by('-published_at')
    categories = Category.objects.all()

    # 🔍 SEARCH
    if query:
        articles = articles.filter(title__icontains=query)

    # 📂 CATEGORY
    if category_id:
        articles = articles.filter(category_id=category_id)

    # 👁 VIEW COUNT (har user 1 marta)
    for article in articles:
        key = f'viewed_article_{article.id}'

        if not request.session.get(key):
            article.views += 1
            article.save()
            request.session[key] = True

    return render(request, 'news/home.html', {
        'articles': articles,
        'categories': categories,
        'query': query,
        'selected_category': str(category_id) if category_id else None,
    })


# 📰 DETAIL (optional)
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    key = f'viewed_article_{article.id}'

    if not request.session.get(key):
        article.views += 1
        article.save()
        request.session[key] = True

    return render(request, 'news/detail.html', {'article': article})