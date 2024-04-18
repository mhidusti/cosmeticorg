from rest_framework import serializers
from ...models import *

class ProductSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField()
    content = serializers.ReadOnlyField()
    attributes =  serializers.ReadOnlyField()

    class Meta:
        model = Products
        fields = ["title", "price", "content", "category", "image", 'status']


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category, many=True).data
        request = self.context.get('request')
        kwargs = request.parser_context.get('kwargs')
        if kwargs.get('pk') is not None:
            rep.pop('content')
        return rep
    
    def create(self, validated_data):
        validated_data['content'] = 'for this product'
        return super().create(validated_data)

    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

        
