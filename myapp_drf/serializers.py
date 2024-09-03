from rest_framework import serializers
from .models import student

# Serialization 

# class studentSerializer(serializers.Serializer):
#     # id = serializers.IntegerField()
#     # name = serializers.CharField(max_length=100)
#     # age = serializers.IntegerField()


#     # def create(self, validated_data):
#     #     return student.objects.create(**validated_data)
    
#     # def update(self, instance, validated_data):
#     #     """
#     #     Update and return an existing `Snippet` instance, given the validated data.
#     #     """
#     #     instance.name = validated_data.get('name', instance.name)
#     #     instance.age = validated_data.get('age', instance.age)
#     #     instance.save()
    #     return instance


# HyperlinkedModelSerializer and Routers ViewSet

class studentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = student
        fields = '__all__'