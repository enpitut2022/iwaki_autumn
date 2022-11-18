def create_single_text_message(message):
    if message == '予定':
        message = 'やるきかっけの予定が生成されました！\n 題名：レスポンもくもく会\n 11/16 15時よりこちらのURLから参加できます！\n https://discord.com/channels/963633143317938176/987247856991744020'
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message