from rest_framework.generics import ListCreateAPIView

from todo.api.serializers import TodoSerializer
from todo.models import Todo


class TodoList(ListCreateAPIView):
    serializer_class = TodoSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            todo = serializer.save()
            todo.user = request.user
            todo.save()
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
