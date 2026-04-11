from django.db import models
from django.urls import reverse

# 📂 Category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 📰 Article
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    # 👁 VIEW
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    # 🔥 SITEMAP UCHUN ENG MUHIM QISM
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])