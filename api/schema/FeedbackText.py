import graphene
from graphene_django import DjangoObjectType
from api import models


class FeedbackTextType(DjangoObjectType):
    class Meta:
        model = models.FeedbackText


class Query(graphene.ObjectType):
    all_feedbacks_text = graphene.List(FeedbackTextType)

    def resolve_all_feedbacks_text(root, info):
        return models.FeedbackText.objects.order_by('ordering')


class Mutation(
    graphene.ObjectType
):
    pass
