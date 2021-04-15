from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from news.views import index, blog, post, about, gallery, search, post_create, post_update, post_delete, madrassah, library, library_detail, project_list, project_detail, admission, letters, family


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('post/<id>/', post, name='post-detail'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('about/', about),
    path('gallery/', gallery),
    path('tinymce/', include('tinymce.urls')),
    path('madrassah/', madrassah),
    path('library/', library),
    path('library_detail/<id>/', library_detail, name='library-detail'),
    path('project_list/', project_list),
    path('project_detail/<id>/', project_detail, name='project-detail'),
    path('admission/', admission),
    path('letters/', letters),
    path('family/', family),


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Mayfair Academy AdminPanel"
admin.site.site_title = "Mayfair Academy App Admin"
admin.site.site_index_title = "Welcome To Mayfair Academy Admin Panel"

