from django.core.exceptions import ObjectDoesNotExist
from .models import Subject

def create_single_text_message(message):
    if message == '予定':
        message = 'やるきっかけの予定が生成されました！\n 題名：レスポンもくもく会\n 11/16 15時よりこちらのURLから参加できます！\n https://discord.com/channels/963633143317938176/987247856991744020'
    elif message == '今日の勉強会':
        lectures = Subject.objects.filter(semester="秋AB", schools="情報学群")
        for lecture in lectures:
            message += (lecture.name + '第9回\n')
        message += 'などがあります！'
    elif message == 'ヘルプ':
        message = 'やるきっかけの使い方\n\n予定\n今日の勉強会\n科目番号\n\nの3つのコマンドがあります。'
    else:
        lecture = Subject.objects.get(semester="秋AB", schools="情報学群", code=message)
        try :
            message =  "【題名】:"+lecture.name+"#9をやっつける会\n【対象学類】:" + lecture.colleges + "(他学類も可)\n【日時】:12/12 20時から1時間程度(途中入退出OK)\n好きなところのURLから参加しよう!\n\n【Discord(音声)】https://discord.com/channels/963633143317938176/997416162218483782 \n"
        except ObjectDoesNotExist :
            message = "この授業の勉強会の予定はありません"
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message