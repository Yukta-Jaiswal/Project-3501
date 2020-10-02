from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs of the blog app
    path('', include('blog.urls')),
]
