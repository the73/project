from owner import views
from django.urls import path

urlpatterns = [
    path("vaccination/list", views.LocationList.as_view(), name="location"),
    path("vaccination/add", views.Addlocation.as_view(), name="addlocation"),
    path("vaccination/<int:id>", views.LocationDetail.as_view(), name="locationdetail"),
    path("vaccination/edit/<int:id>", views.Locationedit.as_view(), name="locationedit"),
    path("vaccination/delete/<int:id>", views.LocationDelete.as_view(), name="locationdelete"),

]
