from django.core.mail import send_mail
from django.http import HttpResponse

def emailfunc(request):
    send_mail(
        'テスト',
        'テスト成功です！',
        '10shoh10@gmail.com',
        ['10shoh10@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse('')