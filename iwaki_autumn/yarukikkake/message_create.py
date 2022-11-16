def create_single_text_message(message):
    if message == '予定':
        message = 'やるきかっけの予定が生成されました！11/17 18時よりこちらのURLから参加できます！\n https://github.com/enpitut2022/iwaki_autumn'
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message