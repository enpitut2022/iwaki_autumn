from .models import Subject

def create_single_text_message(message):
    if message == '予定':
        message = 'やるきっかけの予定が生成されました！\n 題名：レスポンもくもく会\n 11/16 15時よりこちらのURLから参加できます！\n https://discord.com/channels/963633143317938176/987247856991744020'
    elif message == '今日の勉強会':
        lectures = Subject.objects.filter(semester="秋AB", schools="情報学群")
        for lecture in lectures:
            message += (lecture.name + '第9回\n')
        message += 'などがあります！'
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message