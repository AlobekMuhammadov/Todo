from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rejalar),
    # path('rejalar/', rejalar),
    # path('bajarilmagan/', bajarilmagan),
    # path('bitiruvchilar/', bitiruvchi),
    path('reja_ochir/<int:son>/', reja_ochir),
]
