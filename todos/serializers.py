from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        # указываем, какую модель использовать
        model = Todo
        # какие поля в ней мы хотим предоставить
        fields = ('id', 'title', 'body')
