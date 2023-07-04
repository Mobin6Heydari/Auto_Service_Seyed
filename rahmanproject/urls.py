from django.contrib import admin
from django.urls import path , include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
    path('product/', include(('oils.urls', 'product'), namespace='product')),
    path('aboutus/', include(('aboutus.urls', 'aboutus'), namespace='aboutus')),
    path('cars/', include(('cars.urls', 'cars'), namespace='cars')),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


