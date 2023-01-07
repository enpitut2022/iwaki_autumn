from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .message_create import create_single_text_message, create_join_message
from .line_message import LineMessage

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        
        reply_token = data['replyToken']
        event_type = data['type']
        if event_type == 'message' or event_type == 'postback':
            message = data['message']['text'] if event_type == 'message' else data['postback']['data']
            line_user_id = data['source']['userId']
            try:
                line_group_id = data['source']['groupId']
            except Exception as e:
                line_group_id = None
                # print(e)
            line_message = LineMessage(create_single_text_message(message, line_user_id, line_group_id))
            line_message.reply(reply_token)
        elif event_type == 'join':
            try:
                line_group_id = data['source']['groupId']
            except Exception as e:
                line_group_id = None
                # print(e)
            line_message = LineMessage(create_join_message())
            line_message.reply(reply_token)

        return HttpResponse("ok")
    else:
        return HttpResponse("やるきっかけ LINE Bot")