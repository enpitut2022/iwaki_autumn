from .models import Subject, LineUser, UserSubject
from linebot import LineBotApi
from linebot.models import FlexSendMessage
import datetime
import json


def get_weekday():
    today = datetime.date.today()
    weekday = today.weekday()
    weekday_list = {0:'月', 1:'火', 2:'水', 3:'木', 4:'金', 5:'土', 6:'日'}
    return weekday_list[weekday]

def create_single_text_message(message, user_id):
    if message == '新規登録・追加':
        line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
        profile = line_bot_api.get_profile(user_id)
        user_disp_name = profile.display_name
        if LineUser.objects.filter(user_id = user_id).exists() :
            line_user = LineUser.objects.get(user_id = user_id)
            line_user.state = 1
            line_user.save()
        else :
            LineUser.objects.create(user_id=user_id, display_name=user_disp_name, state=1)
        print(LineUser.objects.all())
        message_json = create_json()
        flex_message_json_dict = json.loads(message_json)
        line_bot_api.push_message(user_id, FlexSendMessage(
            alt_text='新規登録・追加',
            contents=flex_message_json_dict
        ))
        message = "登録したい勉強会を選んでください"
    elif message == "登録解除":
        line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
        profile = line_bot_api.get_profile(user_id)
        user_disp_name = profile.display_name
        if LineUser.objects.filter(user_id = user_id).exists() :
            line_user = LineUser.objects.get(user_id = user_id)
            line_user.state = 2
            line_user.save()
        else :
            LineUser.objects.create(user_id=user_id, display_name=user_disp_name, state=2)
        message_json = create_json_by_user_id(user_id)
        if not message_json:
            message = "登録済みの勉強会がありません！"
        else:
            flex_message_json_dict = json.loads(message_json)
            line_bot_api.push_message(user_id, FlexSendMessage(
                alt_text='登録解除',
                contents=flex_message_json_dict
            ))
            message = "登録解除したい勉強会を選んでください"
    elif message == '今日の登録済み勉強会一覧':
        message += "は\n"
        is_subject_exists = False
        line_user = LineUser.objects.get(user_id=user_id)
        user_subjects = UserSubject.objects.filter(push=line_user)
        n = str(10)
        for user_subject in user_subjects:
            if user_subject.subject.day_of_week != get_weekday() : continue
            message += (user_subject.subject.code + ': ' + user_subject.subject.name + '第' + n + '回\n')
            is_subject_exists = True
        message += 'です！'
        if not is_subject_exists :
            message = "今日は登録済みの勉強会がありません！"
    elif message == '全ての登録済み勉強会一覧':
        message += 'は\n'
        is_subject_exists = False
        line_user = LineUser.objects.get(user_id=user_id)
        user_subjects = UserSubject.objects.filter(push=line_user)
        n = str(10)
        for user_subject in user_subjects:
            message += (user_subject.subject.code + ': ' + user_subject.subject.name + '第' + n + '回\n')
            is_subject_exists = True
        message += 'です！'
        if not is_subject_exists :
            message = "登録済みの勉強会がありません！"
    elif message == 'ヘルプ':
        message = 'やるきっかけの使い方\n\n予定\n今日の勉強会\n科目番号\n\nの3つのコマンドがあります。'
    else:
        line_user = LineUser.objects.get(user_id=user_id)
        if line_user.state == 1:
            try :
                subject = Subject.objects.get(semester="秋AB", schools="情報学群", code=message,)
                UserSubject.objects.update_or_create(push=line_user, subject=subject)
                message =  subject.name + "の登録ができました！" + "勉強会の前日と当日の18:30" + "に通知が来ます！"
            except Subject.DoesNotExist :
                message = "この授業の勉強会の予定はありません"
        elif line_user.state == 2:
            try :
                subject = Subject.objects.get(semester="秋AB", schools="情報学群", code=message,)
                UserSubject.objects.filter(push=line_user, subject=subject).delete()
                message =  subject.name + "の削除ができました！"
            except Subject.DoesNotExist :
                message = "この授業の勉強会の予定はありません"
        else:
            message = "内部でエラーが起きています。host.iwaki [at] gmail.com に連絡してください。"
            
    text_message = [
            {
                'type': 'text',
                'text': message
            }
        ]
    return text_message

def create_json():
    subjects = Subject.objects.filter(semester="秋AB", schools="情報学群")
    json_message = '''{
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
    '''
    l = len(subjects)
    s = set(())
    for subject in subjects[:l-1] :
        if subject.name in s: continue
        json_message += '''
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "''' + subject.name[:40] + '''",
                            "text": "'''+ subject.code +'''"
                        }
                    }, '''
        s.add(subject.name)
    json_message += '''
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "''' + subjects[l-1].name[:40] + '''",
                            "text": "'''+ subjects[l-1].code +'''"
                        }
                    } '''
    json_message += '''
            ]
        }
    }'''
    return json_message

def create_json_by_user_id(user_id):
    line_user = LineUser.objects.get(user_id=user_id)
    if not UserSubject.objects.filter(push=line_user).exists(): return False
    user_subjects = UserSubject.objects.filter(push=line_user)
    json_message = '''{
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
    '''
    l = len(user_subjects)
    s = set(())
    for user_subject in user_subjects[:l-1] :
        if user_subject.subject.name in s: continue
        json_message += '''
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "''' + user_subject.subject.name[:40] + '''",
                            "text": "'''+ user_subject.subject.code +'''"
                        }
                    }, '''
        s.add(user_subject.subject.name)
    json_message += '''
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "''' + user_subjects[l-1].subject.name[:40] + '''",
                            "text": "'''+ user_subjects[l-1].subject.code +'''"
                        }
                    } '''
    json_message += '''
            ]
        }
    }'''
    return json_message