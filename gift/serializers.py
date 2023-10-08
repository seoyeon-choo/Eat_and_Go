from rest_framework import serializers
from .models import Gift

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = '__all__'

    def create(self, validated_data):
        # 현재 로그인한 사용자를 giver로 설정
        validated_data['giver'] = self.context['request'].user

        # Gift 모델 인스턴스 생성
        gift = Gift.objects.create(**validated_data)
        return gift
