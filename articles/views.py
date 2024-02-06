

# Create your views here.
from django.shortcuts import render,redirect
from . import forms
from .models import Category,Article
from .forms import SearchForm,ArticlesForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import View

def home(request):
    #  форма для поиска товаров на сайте
    search_bar = forms.SearchForm()
    article_info = Article.objects.all()
    # Собираем все категории товаров
    category_info = Category.objects.all()
    # Отправить элементы на фронт
    context = {"form": search_bar,  'article': article_info, 'category': category_info}
    return render(request, 'home.html', context)




def category(request, pk):
    category = Category.objects.get(id=pk)
    articles = Article.objects.filter(category=category)
    context = {'articles': articles}
    return render(request, 'category.html', context)


def article(request, pk):
    article = Article.objects.get(id=pk)
    context = {'article': article}
    return render(request, 'article.html', context)



def search_article(request):
    if request.method == 'POST':
        info = request.POST.get('search_article')
        try:
            infot = Article.objects.get(title__icontains=info)
            return redirect(f'article/{infot.id}')
        except:
            return redirect('/not-found')






def createarticles(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form = ArticlesForm()
    return render(request, 'createarticles.html', {'form': form})





def about(request):
    return render(request,'about.html')
def not_found(request):
    return render(request,'not-found.html')
def del_from_article(request,pk):
    article_to_delete = Article.objects.get(id=pk)
    Article.objects.all(user_id=request.user.id,
                        title=article_to_delete).delete()
    return redirect('/article')
class Register(View):
    template_name = 'registration/register.html'

    # Отправка формы регистрации
    def get(self, request):
        context = {'form': UserCreationForm}
        return render(request, self.template_name, context)

    # Добавление в БД
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        context = {'form': UserCreationForm}
        return render(request, self.template_name, context)