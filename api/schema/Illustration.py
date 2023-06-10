import graphene
from graphene_django import DjangoObjectType
from api import models

def getTypes(types):
    formated_types = []

    for idx in range(0, len(types)):
        [key, text] = types[idx]
        formated_types.append({
            'id': str(idx),
            'name': text,
            'value': key
        })

    return formated_types


types = getTypes(models.Illustration.ILLUSTRATIONS_TYPES)

class IllustrationType(DjangoObjectType):
    class Meta:
        model = models.Illustration
        convert_choices_to_enum = False

class TypeType(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    value = graphene.String()

class IllustrationResponseType(graphene.ObjectType):
    items=graphene.List(IllustrationType)
    types=graphene.List(TypeType)

class Query(graphene.ObjectType):
    all_illustrations = graphene.Field(IllustrationResponseType)

    def resolve_all_illustrations(root, info):
        return {
            'items': models.Illustration.objects.order_by('ordering'),
            'types': types
        }


class Mutation(
    graphene.ObjectType
):
    pass
