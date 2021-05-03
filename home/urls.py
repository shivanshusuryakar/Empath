from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path("",views.index,name="index"),
    path("model",views.modelform,name="model"),
    path("result",views.result,name="result"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)