from django.contrib import admin
from django.urls import path, include   # 引入 include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # blog 路由交给 blog/urls.py
]
