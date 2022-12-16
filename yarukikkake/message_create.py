from .models import Subject, LineUser, UserSubject
from linebot import LineBotApi

def create_single_text_message(message, user_id):
    if message == '予定':
        message = 'やるきっかけの予定が生成されました！\n 題名：レスポンもくもく会\n 11/16 15時よりこちらのURLから参加できます！\n https://discord.com/channels/963633143317938176/987247856991744020'
    elif message == '登録':
        line_bot_api = LineBotApi("3wF9UeJrvufp/qq2Ddn8wMqs4UDui4dlcZe5wVVSPEwYqHoX4h8lHFiKpLzjCRyhM5V4f5ruVUK8nYmqUCFA2C0hd1ZEJm5oBT2JsnFzyJYvlpOwLlsp6Ki1q8dNIsl26HSymk7Bbox6HSQKc9Bd9wdB04t89/1O/w1cDnyilFU=")
        profile = line_bot_api.get_profile(user_id)
        user_disp_name = profile.display_name
        LineUser.objects.update_or_create(user_id = user_id, display_name=user_disp_name)
        print(LineUser.objects.all())
        message = "ユーザー登録ができました！"
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