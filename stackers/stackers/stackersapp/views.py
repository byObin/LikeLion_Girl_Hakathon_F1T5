from django.shortcuts import render
from .forms import DevelopModelForm
from .models import Develop, QnA
from .models import Brief
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
def home(request):
    # ��α� ���� ��� ���� �ڵ� (DB�� ��α� ��ü���� ��� ������)
    # posts = Blog.objects.all()
    posts = Develop.objects.filter().order_by('-date') # ���� ���������� �ϴ� ������ ���͸� �ؼ� ������ / order_by: ����
    return render(request, 'index.html', {'posts' : posts})

def detail(request, develop_id):
    # develop_id ��° �Խñ��� DB�κ��� �����ͼ�
    develop_detail = get_object_or_404(Develop, pk=develop_id)

    # comment_form = CommentForm()

    # develop_id ��° ��α� ���� detail.html�� ���� �ڵ�
    return render(request, 'detail.html', {'develop_detail' : develop_detail})

def brief_home(request):
    # ��α� ���� ��� ���� �ڵ� (DB�� ��α� ��ü���� ��� ������)
    # posts = Blog.objects.all()
    posts = Brief.objects.filter().order_by('-date') # ���� ���������� �ϴ� ������ ���͸� �ؼ� ������ / order_by: ����
    return render(request, 'brief_index.html', {'posts' : posts})

def brief_detail(request, brief_id):
    # develop_id ��° �Խñ��� DB�κ��� �����ͼ�
    brief_detail = get_object_or_404(Brief, pk=brief_id)

    # comment_form = CommentForm()

    # develop_id ��° ��α� ���� detail.html�� ���� �ڵ�
    return render(request, 'brief_detail.html', {'brief_detail' : brief_detail})


def modelformcreate(request):
    if request.method == 'POST':
        # �Է� ������ DB�� ����
        form = DevelopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # �Է��� ���� �� �ִ� html �����ֱ�
        form = DevelopModelForm()
    return render(request, 'form_create.html', {'form' :form})

def qna(request):
    # ��α� ���� ��� ���� �ڵ� (DB�� ��α� ��ü���� ��� ������)
    # posts = Blog.objects.all()
    posts = QnA.objects.filter().order_by('-date') # ���� ���������� �ϴ� ������ ���͸� �ؼ� ������ / order_by: ����
    return render(request, 'qna.html', {'posts' : posts})

def qna_detail(request, qna_id):
    # qna_id ��° �Խñ��� DB�κ��� �����ͼ�
    qna_detail = get_object_or_404(QnA, pk=qna_id)

    # comment_form = CommentForm()

    # qna_id ��° ��α� ���� detail.html�� ���� �ڵ�
    return render(request, 'qna_detail.html', {'qna_detail' : qna_detail})








