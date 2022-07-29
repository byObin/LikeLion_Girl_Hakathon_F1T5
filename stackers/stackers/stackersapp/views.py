from django.shortcuts import render

# Create your views here.
def home(request):
    # 블로그 글을 모두 띄우는 코드 (DB의 블로그 객체들을 모두 가져옴)
    # posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('-date') # 내가 가져오고자 하는 정보를 필터링 해서 가져옴 / order_by: 정렬
    return render(request, 'index.html', {'posts' : posts})

def detail(request, blog_id):
    # develop_id 번째 게시글을 DB로부터 가져와서
    develop_detail = get_object_or_404(Develop, pk=develop_id)

    # comment_form = CommentForm()

    # develop_id 번째 블로그 글을 detail.html로 띄우는 코드
    return render(request, 'detail.html', {'develop_detail' : develop_detail})