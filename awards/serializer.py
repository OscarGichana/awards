from rest_framework import serializers
from .models import MoringaMerch,AwardsProject

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoringaMerch
        fields = ('id','first_name', 'pic', 'email', 'bio')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardsProject
        fields = ('id','title', 'pic', 'description', 'link')
