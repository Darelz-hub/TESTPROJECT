from django.shortcuts import render
import requests
import subprocess


# Create your views here.
def get_linux_param(request):

    name = request.POST.get('name')
    result = {}
    #process = subprocess.Popen(['inxi', f'-{name}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8') # Первая утилита, не совсем подходит под тз
    process = subprocess.Popen(['hwinfo', f'--{name}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')  # Вторая утилита, где можно найти нужные данные
    try:
        process, error = process.communicate(timeout=10)
        process = process.split('\n') # Делим данные строки. получаем список
        result['content'] = process
        print(error)
        return {'response': result}
    except subprocess.TimeoutExpired:
        process.kill()

def informations(request):
    data = get_linux_param(request)
    #print(data['content'])
    return render(request, 'linux_param.html', data)