from django.urls import paths


from profiles_api import views


urlspatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
