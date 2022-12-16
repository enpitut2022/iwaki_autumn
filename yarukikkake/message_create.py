from .models import Subject, LineUser, UserSubject
from linebot import LineBotApi

def create_single_text_message(message, user_id):
    if message == '予定':
        message = 'やるきっかけの予定が生成されました！\n 題名：レスポンもくもく会\n 11/16 15時よりこちらのURLから参加できます！\n https://discord.com/channels/963633143317938176/987247856991744020'
    elif message == '登録':
        line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
        profile = line_bot_api.get_profile(user_id)
        user_disp_name = profile.display_name
        LineUser.objects.update_or_create(user_id = user_id, display_name=user_disp_name)
        print(LineUser.objects.all())
        message = "ユーザー登録ができました！"
    elif "登録" in message :
        list = message.split(" ")
        line_user = LineUser.objects.filter(user_id = user_id)
        message = ""
        for ele in list :
            if ele == "登録" : continue
            UserSubject.objects.create(push = line_user.id, subject = ele)
            message += str(ele)
        print(UserSubject.objects.all())
        message += " が登録されました！"
    elif message == '今日の勉強会':
        lectures = Subject.objects.filter(semester="秋AB", schools="情報学群", day_of_week__icontains="金")
        message += 'は\n'
        for lecture in lectures:
            message += (lecture.name + '第9回\n')
        message += 'などがあります！'
    elif message == 'ヘルプ':
        message = 'やるきっかけの使い方\n\n予定\n今日の勉強会\n科目番号\n\nの3つのコマンドがあります。'
    else:
        try :
            lecture = Subject.objects.get(semester="秋AB", schools="情報学群", code=message,)
            message =  "【題名】:"+lecture.name+"#10をやっつける会\n【対象学類】:" + lecture.colleges + "(他学類も可)\n【日時】:12/12 20時から1時間程度(途中入退出OK)\n好きなところのURLから参加しよう!\n\n【Discord(音声)】https://discord.com/channels/963633143317938176/997416162218483782 \n"
        except Subject.DoesNotExist :
            message = "この授業の勉強会の予定はありません"
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message