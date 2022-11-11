from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

def index(request):
    # subject = "題名"
    # message = "本文です\nこんにちは。メールを送信しました"
    # from_email = "information@yarukikkake"
    # recipient_list = [
    #     "amixedcolor@gmail.com",
    #     "iwanatteiwanai123@gmail.com",
    #     "morinotsukuba@gmail.com",
    #     "okegom@outlook.com"
    # ]

    # send_mail(subject, message, from_email, recipient_list)
    return HttpResponse("やるきっかけにこんにちは！")