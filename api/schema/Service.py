import graphene
from graphene_django import DjangoObjectType
from api import models


class ServicesType(DjangoObjectType):
    class Meta:
        model = models.Service


class Query(graphene.ObjectType):
    all_services = graphene.List(ServicesType)

    def resolve_all_services(root, info):
        return models.Service.objects.order_by('ordering')


class Mutation(
    graphene.ObjectType
):
    pass
