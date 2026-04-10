from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# 🔥 SITEMAP
from django.contrib.sitemaps.views import sitemap
from news.sitemap import ArticleSitemap

# 🤖 ROBOTS
from django.views.generic import TemplateView

sitemaps = {
    'articles': ArticleSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),

    # 🔥 SITEMAP
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),

    # 🤖 ROBOTS
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain"
    )),
]

# 📸 MEDIA
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)