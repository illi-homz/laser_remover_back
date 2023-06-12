from django.urls import path
# from django.views.decorators.csrf import csrf_exempt
# from graphene_django.views import GraphQLView
# from api.schema import schema
from . import views

urlpatterns = [
    path("api/sendFormToTelegram", views.send_form_to_telegram),
]
