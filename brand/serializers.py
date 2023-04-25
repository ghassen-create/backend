from rest_framework import serializers

from .models import Brand, ClothingItem


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ClothingItemSerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField()

    class Meta:
        model = ClothingItem
        fields = "__all__"

    @staticmethod
    def get_brand_name(obj):
        return obj.brand_name
