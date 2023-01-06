from .models import Subject, LineUser, UserSubject, Task, LineGroup
from linebot import LineBotApi
from linebot.models import FlexSendMessage
import datetime
import json

def get_weekday():
    today = datetime.date.today()
    weekday = today.weekday()
    weekday_list = {0:'月', 1:'火', 2:'水', 3:'木', 4:'金', 5:'土', 6:'日'}
    return weekday_list[weekday]

def create_line_user(user_id):
    line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
    profile = line_bot_api.get_profile(user_id)
    user_disp_name = profile.display_name
    if LineUser.objects.filter(user_id = user_id).exists() :
        line_user = LineUser.objects.get(user_id = user_id)
        line_user.save()
    else :
        LineUser.objects.create(user_id=user_id, display_name=user_disp_name, state=1)
        
def create_line_group(group_id):
    if LineGroup.objects.filter(group_id = group_id).exists() :
        pass
    else :
        LineGroup.objects.create(group_id=group_id)

def create_single_text_message(message, user_id, group_id):
    create_line_user(user_id)
    if group_id != None :
        create_line_group(group_id)
    line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
    if group_id == None:
        if message == "タスク登録・変更" :
            line_user = LineUser.objects.get(user_id = user_id)
            line_user.state = 2
            line_user.save()
            message = "登録したいタスク名を入力してください"
        elif message == "タスク開始報告" :
            line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
            line_user = LineUser.objects.get(user_id = user_id)
            line_user.state = 4
            line_user.save()
            message_json = create_json_by_user_id(user_id)
            if message_json :
                flex_message_json_dict = json.loads(message_json)
                line_bot_api.push_message(user_id, FlexSendMessage(
                    alt_text='開始報告',
                    contents=flex_message_json_dict
                ))
                message = "開始報告するタスクを選択してください！"
            else:
                message = "登録されたタスクは全て開始できています！" 
        elif message == "タスク確認":
            line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
            line_user = LineUser.objects.get(user_id = user_id)
            line_user.state = 5
            line_user.save()
            message_json = create_json_by_user_id(user_id)
            if message_json :
                flex_message_json_dict = json.loads(message_json)
                line_bot_api.push_message(user_id, FlexSendMessage(
                    alt_text='開始報告',
                    contents=flex_message_json_dict
                ))
                message = "時間を確認したいタスクを選択してください！"
            else:
                message = "登録されたタスクは全て開始できています！" 
        elif message == "タスク未開始ユーザー確認":
            message = create_message_without_groups()
            pass
        else:
            line_user = LineUser.objects.get(user_id=user_id)
            print("公式LINE", line_user)
            line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
            if line_user.state == 2:
                task = Task.objects.create(task_name=message, task_user=line_user, task_status=1)
                line_user.state = 3
                message_json = create_time_json()
                flex_message_json_dict = json.loads(message_json)
                line_bot_api.push_message(user_id, FlexSendMessage(
                    alt_text='時刻選択',
                    contents=flex_message_json_dict
                ))
                line_user.latast_task_id = task.task_id
                line_user.save()
                message = "タスク名を登録しました。続いて、タスクを開始する時刻を登録してください！"
            elif line_user.state == 3:
                task = Task.objects.get(task_id = line_user.latast_task_id)
                tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
                time = datetime.datetime.now().replace(hour=int(message), tzinfo=tokyo_tz) + datetime.timedelta(days=1)
                task.task_start_time = time
                task.save()
                line_user.state = 1
                line_user.save()
                message = "タスクを開始する時刻を登録しました。開始時刻より前に、タスク開始報告をしてください！"
            elif line_user.state == 4:
                task = Task.objects.get(task_id = message)
                task.task_status = 2
                task.save()
                message = task.task_name + "を開始できました！おめでとうございます！" 
            elif line_user.state == 5:
                task = Task.objects.get(task_id = message)
                message = task.task_name + "は、" + str(task.task_start_time.day) + "日の" + str(task.task_start_time.hour + 9) + "時に開始される予定です！" 
            else:
                message = "想定されていないコマンドです！"
    else :
        if message == "やるきっかけ" :
            message_json = '''{
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "タスク登録・変更",
                        "text": "タスク登録・変更"
                        }
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "タスク開始報告",
                        "text": "タスク開始報告"
                        }
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "タスク確認",
                        "text": "タスク確認"
                        }
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "タスク未開始ユーザー確認",
                        "text": "タスク未開始ユーザー確認"
                        }
                    }
                    ]
                }
                }'''
            flex_message_json_dict = json.loads(message_json)
            line_bot_api.push_message(group_id, FlexSendMessage(
                alt_text='開始報告',
                contents=flex_message_json_dict
            ))
            message = "上のメニューから実行したい処理を選んでください！"
        elif message == "タスク登録・変更" :
            line_user = LineUser.objects.get(user_id = user_id)
            line_user.state = 2
            line_user.save()
            message = "登録したいタスク名を入力してください"
        elif message == "タスク開始報告" :
            line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
            line_user = LineUser.objects.get(user_id = user_id)
            line_user.state = 4
            line_user.save()
            message_json = create_json_by_user_id_and_group_id(user_id, group_id)
            if message_json :
                flex_message_json_dict = json.loads(message_json)
                line_bot_api.push_message(group_id, FlexSendMessage(
                    alt_text='開始報告',
                    contents=flex_message_json_dict
                ))
                message = "開始報告するタスクを選択してください！"
            else:
                message = "登録されたタスクは全て開始できています！" 
        elif message == "タスク確認":
            line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
            line_user = LineUser.objects.get(user_id = user_id)
            line_user.state = 5
            line_user.save()
            message_json = create_json_by_user_id(user_id)
            if message_json :
                flex_message_json_dict = json.loads(message_json)
                line_bot_api.push_message(group_id, FlexSendMessage(
                    alt_text='開始報告',
                    contents=flex_message_json_dict
                ))
                message = "時間を確認したいタスクを選択してください！"
            else:
                message = "登録されたタスクは全て開始できています！" 
        elif message == "タスク未開始ユーザー確認":
            message = create_message_by_group_id(group_id)
            pass
        else:
            line_user = LineUser.objects.get(user_id=user_id)
            print("グループ", line_user, "state=", line_user.state)
            line_group = LineGroup.objects.get(group_id=group_id)
            line_bot_api = LineBotApi("XtWv3Sv/BEkhMqI9hOFCQCDI2FNEZ7ic14xnPxs7Oe+zhZdfrg6BB8f2iOlWgrEfOL0ecfe5MQp+MG4zAuzhZfn0GzoIXSJdOQ9yUmXZOCdia7AFNN+apGdqulruV5WLcFPMXhh1uLa2jt+MW4rFCQdB04t89/1O/w1cDnyilFU=")
            if line_user.state == 2:
                task = Task.objects.create(task_name=message, task_user=line_user, task_group=line_group, task_status=1)
                line_user.state = 3
                message_json = create_time_json()
                flex_message_json_dict = json.loads(message_json)
                line_bot_api.push_message(group_id, FlexSendMessage(
                    alt_text='時刻選択',
                    contents=flex_message_json_dict
                ))
                line_user.latast_task_id = task.task_id
                line_user.save()
                message = "タスク名を登録しました。続いて、タスクを開始する時刻を登録してください！"
            elif line_user.state == 3:
                task = Task.objects.get(task_id = line_user.latast_task_id)
                tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
                time = datetime.datetime.now().replace(hour=int(message), tzinfo=tokyo_tz) + datetime.timedelta(days=1)
                task.task_start_time = time
                task.save()
                line_user.state = 1
                line_user.save()
                message = "タスクを開始する時刻を登録しました。開始時刻より前に、タスク開始報告をしてください！"
            elif line_user.state == 4:
                task = Task.objects.get(task_id = message)
                task.task_status = 2
                task.save()
                message = task.task_name + "を開始できました！おめでとうございます！" 
            elif line_user.state == 5:
                task = Task.objects.get(task_id = message)
                message = task.task_name + "は、" + str(task.task_start_time.day) + "日の" + str(task.task_start_time.hour + 9) + "時に開始される予定です！" 
            else:
                message = "想定されていないコマンドです！"
            
    text_message = [
            {
                'type': 'text',
                'text': message
            }
        ]
    return text_message

def create_json_by_user_id(user_id):
    line_user = LineUser.objects.get(user_id=user_id)
    if not Task.objects.filter(task_user=line_user, task_group=None, task_status=1).exists(): return False
    tasks = Task.objects.filter(task_user=line_user, task_group=None, task_status=1)
    json_message = '''{
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
    '''
    l = len(tasks)
    for task in tasks[:l-1] :
        json_message += '''
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "''' + task.task_name + '''",
                            "text": "'''+ str(task.task_id) +'''"
                        }
                    }, '''
    json_message += '''
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "''' + tasks[l-1].task_name + '''",
                            "text": "'''+ str(tasks[l-1].task_id) +'''"
                        }
                    } '''
    json_message += '''
            ]
        }
    }'''
    return json_message

def create_json_by_user_id_and_group_id(user_id, group_id):
    line_user = LineUser.objects.get(user_id=user_id)
    line_group = LineGroup.objects.get(group_id=group_id)
    if not Task.objects.filter(task_user=line_user, task_group=line_group, task_status=1).exists(): return False
    tasks = Task.objects.filter(task_user=line_user, task_group=line_group, task_status=1)
    json_message = '''{
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
    '''
    l = len(tasks)
    for task in tasks[:l-1] :
        json_message += '''
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "''' + task.task_name + '''",
                            "text": "'''+ str(task.task_id) +'''"
                        }
                    }, '''
    json_message += '''
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "''' + tasks[l-1].task_name + '''",
                            "text": "'''+ str(tasks[l-1].task_id) +'''"
                        }
                    } '''
    json_message += '''
            ]
        }
    }'''
    return json_message

def create_message_without_groups():
    if not Task.objects.filter(task_group=None, task_status=1).exists(): return False
    tasks = Task.objects.filter(task_group=None, task_status=1)
    message = "以下が残っているようです！"
    for task in tasks :
        message += "\n・"
        message += task.task_user.display_name
        try :
            message += "は、まだ" + str(task.task_start_time.day) + "日" + str(task.task_start_time.hour + 9) + "時に開始予定の「"
        except Exception as e:
            print(e)
            message += "は、まだ時間未登録の「"
        message += task.task_name
        message += "」を開始していないようです！"
    return message

def create_message_by_group_id(group_id):
    line_group = LineGroup.objects.get(group_id=group_id)
    if not Task.objects.filter(task_group=line_group, task_status=1).exists(): return False
    tasks = Task.objects.filter(task_group=line_group, task_status=1)
    message = "以下が残っているようです！"
    for task in tasks :
        message += "\n・"
        message += task.task_user.display_name
        try :
            message += "は、まだ" + str(task.task_start_time.day) + "日" + str(task.task_start_time.hour + 9) + "時に開始予定の「"
        except Exception as e:
            print(e)
            message += "は、まだ時間未登録の「"
        message += task.task_name
        message += "」を開始していないようです！"
    return message

def create_time_json():
    json_message = '''{
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
    '''
    for hh in range(0, 23, 1) :
        json_message += '''
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "''' + "明日" + str(hh) + "時から" + '''",
                            "text": "'''+ str(hh) +'''"
                        }
                    }, '''
    hh += 1
    json_message += '''
                    {
                        "type": "button",
                        "action": {
                            "type": "message",
                            "label": "''' + "明日" + str(hh) + "時から" + '''",
                            "text": "'''+  str(hh) +'''"
                        }
                    } '''
    json_message += '''
            ]
        }
    }'''
    return json_message

def create_join_message():
    message = "やるきっかけが参加しました！\n\nやるきっかけ\n\nと入力するとタスク登録できます！"
    text_message = [
            {
                'type': 'text',
                'text': message
            }
        ]
    return text_message