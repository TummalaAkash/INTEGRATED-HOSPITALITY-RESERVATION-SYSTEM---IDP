import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .bot_model.chat import ChatBot

@csrf_exempt
def get_response(request):
    bot = ChatBot()
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            query = data.get('query', 'asdfgh')  
            print("Received query:", query)  
            return JsonResponse({'status': 'success', 'response': bot.get_response(query)})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data received'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'})


# chatbot/chatbot/bot/bot_model/chat.py