import graphene
from graphene_django import DjangoObjectType
from api import models
from . import Illustration, FeedbackText, FeedbackVideo, Questions, Service


class Query(
    Illustration.Query,
    FeedbackText.Query,
    FeedbackVideo.Query,
    Questions.Query,
    Service.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    graphene.ObjectType
):
    pass
