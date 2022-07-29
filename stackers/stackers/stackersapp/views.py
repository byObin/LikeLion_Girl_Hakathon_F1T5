from django.shortcuts import render
from .forms import DevelopModelForm
from .models import Develop, QnA
from .models import Brief
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
def home(request):
    # 블로그 글을 모두 띄우는 코드 (DB의 블로그 객체들을 모두 가져옴)
    # posts = Blog.objects.all()
    posts = Develop.objects.filter().order_by('-date') # 내가 가져오고자 하는 정보를 필터링 해서 가져옴 / order_by: 정렬
    return render(request, 'index.html', {'posts' : posts})

def detail(request, develop_id):
    # develop_id 번째 게시글을 DB로부터 가져와서
    develop_detail = get_object_or_404(Develop, pk=develop_id)

    # comment_form = CommentForm()

    # develop_id 번째 블로그 글을 detail.html로 띄우는 코드
    return render(request, 'detail.html', {'develop_detail' : develop_detail})

def brief_home(request):
    # 블로그 글을 모두 띄우는 코드 (DB의 블로그 객체들을 모두 가져옴)
    # posts = Blog.objects.all()
    posts = Brief.objects.filter().order_by('-date') # 내가 가져오고자 하는 정보를 필터링 해서 가져옴 / order_by: 정렬
    return render(request, 'brief_index.html', {'posts' : posts})

def brief_detail(request, brief_id):
    # develop_id 번째 게시글을 DB로부터 가져와서
    brief_detail = get_object_or_404(Brief, pk=brief_id)

    # comment_form = CommentForm()

    # develop_id 번째 블로그 글을 detail.html로 띄우는 코드
    return render(request, 'brief_detail.html', {'brief_detail' : brief_detail})


def modelformcreate(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = DevelopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html 갖다주기
        form = DevelopModelForm()
    return render(request, 'form_create.html', {'form' :form})

def qna(request):
    # 블로그 글을 모두 띄우는 코드 (DB의 블로그 객체들을 모두 가져옴)
    # posts = Blog.objects.all()
    posts = QnA.objects.filter().order_by('-date') # 내가 가져오고자 하는 정보를 필터링 해서 가져옴 / order_by: 정렬
    return render(request, 'qna.html', {'posts' : posts})

def qna_detail(request, qna_id):
    # qna_id 번째 게시글을 DB로부터 가져와서
    qna_detail = get_object_or_404(QnA, pk=qna_id)

    # comment_form = CommentForm()

    # qna_id 번째 블로그 글을 detail.html로 띄우는 코드
    return render(request, 'qna_detail.html', {'qna_detail' : qna_detail})
