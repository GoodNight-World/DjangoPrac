from django.shortcuts import render
from .models import Post
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView

post_list = ListView.as_view(model=Post)
# 밑의 post_list 함수에서 검색 기능만을 빼고 동일한 기능을 함
# 장고에 내재된 클래스 기반 뷰

# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q','')
#     # request.POST
#     # request.FILES
    
#     if q:
#         qs = qs.filter(message__icontains=q)
        
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })

def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello World!")
    return response

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")
    