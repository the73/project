from canidates import views
from django.urls import path

urlpatterns = [
    path('home/', views.CustmerHome.as_view(), name="custhome"),
    path("account/signup", views.SignupView.as_view(), name="singnup"),
    path("account/signin", views.SigninView.as_view(), name="singnip"),
    path('booked/<int:id>', views.Booked.as_view(), name="booked"),
    path('bookeditems', views.BookedItems.as_view(), name="Bookedtitem"),

]
