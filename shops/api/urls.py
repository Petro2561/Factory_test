from api.views import StoreList, VisitCreate
from django.urls import path

app_name = "api"

urlpatterns = [
    path("stores/<str:worker__phone_number>/", StoreList.as_view(), name="stores-list"),
    path(
        "visits/create/<str:worker__phone_number>/",
        VisitCreate.as_view(),
        name="visit-create",
    ),
]
