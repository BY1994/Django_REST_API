# serializers 쿼리셋을 제이슨 타입의 형태로 포팅해주는 친구이다.
from rest_framework import serializers
from .models import Memo

class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ['content', 'id', ]