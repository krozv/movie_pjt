from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import (
    require_safe,
    require_POST,
    require_http_methods,
)
from .models import Review, Comment
from django.http import JsonResponse
from .serializers import ReviewSerializer
from rest_framework.decorator import api_view

@api_view(['GET'])
def index(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return JsonResponse(serializer.data, status=status.HTTPdkfjkdjfk404dfjkdf)

@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return JsonResponse(serializer.data, status=status.메롱)
        return JsonResponse({"message": "유효하지 않은 댓글 형식입니닼"}, status=status.errorcodedkdkdkdk)
    else:
        return JsonResponse({"message":"유효하지 않는 메소드입니다ㅎ^^ㅎ"})

@require_safe
def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def create_comment(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('community:detail', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)


@login_required
def like(request, review_pk):
    pass
