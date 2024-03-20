from rest_framework.generics import RetrieveUpdateDestroyAPIView
from todo.api.serializers import TodoSerializer
from todo.models import Todo


class TodoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

