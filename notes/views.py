from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Memo
from .serializers import MemoSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def create_and_list(request):
    if request.method == 'POST':
        serializer = MemoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    else:
        memos = Memo.objects.all()
        serializer = MemoSerializer(memos, many=True)
    return Response(serializer.data)
    
@api_view(['DELETE'])
def delete(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()
    # return Response({"message": "삭제되었습니다!"})
    memos = Memo.objects.all()
    serializer = MemoSerializer(memos, many=True)
    return Response(serializer.data)