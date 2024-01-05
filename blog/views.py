from .models import Content
from rest_framework import serializers, permissions, generics


# permissions: -> in file:
class IsAuthorORIsAdminForModify(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser or Content.objects.filter(
            id=request.parser_context['kwargs']['pk'],
            author=request.user
        ).exists()


# serializer: -> in file
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Content
        read_only_fields = ('author',)

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class ContentListCreateApi(generics.ListCreateAPIView):
    # permission => GET => Any - POST => isAuthenticate
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer_class()
    #     if (serializer := serializer(data=request.data)).is_valid():
    #         content = serializer.data
    #         content.author = request.user
    #         Content.object.create()
    #         return response.Response(serializer.data, 201)
    #     return response.Response(serializer.errors)


class ContentModify(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorORIsAdminForModify]
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
