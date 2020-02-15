from rest_framework.viewsets import ModelViewSet
from info.models import InfoModel
from info.serializers import InfoModelSerializer
from rest_framework.permissions import IsAdminUser, AllowAny


class InfoViewSet(ModelViewSet):
    serializer_class = InfoModelSerializer
    queryset = InfoModel.objects.all()
    permission_classes = [AllowAny, ]

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAdminUser, ]
        return super(InfoViewSet, self).get_permissions()
