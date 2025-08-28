from django.http import HttpResponse

def post_list(request):
    return HttpResponse("这是博客文章列表")
