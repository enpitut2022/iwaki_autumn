def create_single_text_message(message):
    if message == '予定':
        message = 'やるきっかけの予定が生成されました！\n 題名：レスポンもくもく会\n 11/16 15時よりこちらのURLから参加できます！\n https://discord.com/channels/963633143317938176/987247856991744020'
    elif message == '今日の勉強会':
        message = '並列処理アーキテクチャの第9回\n情報線形代数第9回\n専門英語基礎第9回\nなどがあります！\n'
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message