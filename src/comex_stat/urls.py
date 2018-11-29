from django.contrib import admin
from django.urls import path
from comex_stat import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from graphene_django.views import GraphQLView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('', views.homepage),
]
urlpatterns += staticfiles_urlpatterns()
