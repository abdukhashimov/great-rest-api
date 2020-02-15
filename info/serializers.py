from rest_framework.serializers import ModelSerializer
from info.models import InfoModel


class InfoModelSerializer(ModelSerializer):

    class Meta:
        model = InfoModel
        fields = ('name', 'information')
