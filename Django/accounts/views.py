from django.shortcuts import render, redirect

from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm

def register(request):
    # 首次请求显示空表单
    if request.method != 'POST':
        form = UserCreationForm()
    # 对提交的POST表单数据进行处理
    else:
        form = UserCreationForm(data=request.POST)
        new_user = form.save()
        # 让用户登录， 并重新定位到主页
        login(request, new_user)
        return redirect('learning_logs:index')
    
    # 显示空表单或指出表单无效
    context = {'form': form}
    return render(request, 'registration/register.html', context)
