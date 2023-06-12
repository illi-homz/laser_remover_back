import graphene
from graphene_django import DjangoObjectType
from api import models


class QuestionsType(DjangoObjectType):
    class Meta:
        model = models.Questions


class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionsType)

    def resolve_all_questions(root, info):
        return models.Questions.objects.order_by('ordering')


class Mutation(
    graphene.ObjectType
):
    pass
