from django.urls import path

from .views import AboutPageView, HomePageView, ContactPageView, LinksPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('links/', LinksPageView.as_view(), name='links'),
]
