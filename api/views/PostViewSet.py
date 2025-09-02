from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from api.models import Post
from api.serializers import PostSerializer

class PostViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.PartialUpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    http_method_names = ["get","post","patch","delete"]
