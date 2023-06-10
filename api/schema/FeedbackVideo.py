import graphene
from graphene_django import DjangoObjectType
from api import models


class FeedbackVideoType(DjangoObjectType):
    class Meta:
        model = models.FeedbackVideo


class Query(graphene.ObjectType):
    all_feedbacks_video = graphene.List(FeedbackVideoType)

    def resolve_all_feedbacks_video(root, info):
        return models.FeedbackVideo.objects.order_by('ordering')


class Mutation(
    graphene.ObjectType
):
    pass
