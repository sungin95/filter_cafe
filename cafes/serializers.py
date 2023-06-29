from rest_framework.serializers import ModelSerializer

from filters.models import BallotBox, Filter, FilterScore
from users.models import User

from .models import Cafe, Review


class CafesSerializer(ModelSerializer):
    class Meta:
        model = Cafe
        fields = (
            "pk",
            "name",
            "city",
            "address",
            "business_hours",
        )


# class CafeCreateSerializer(ModelSerializer):
#     class Meta:
#         model = C
