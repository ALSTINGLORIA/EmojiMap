from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import EmojiSubmission


def index(request):
    return render(request, 'index.html')

@csrf_exempt
def get_all_emojis(request):
    emojis = EmojiSubmission.objects.all()
    emoji_data = [
        {'emoji': emoji.emoji, 'latitude': emoji.latitude, 'longitude': emoji.longitude}
        for emoji in emojis
    ]
    return JsonResponse({'status': 'success', 'emojis': emoji_data})

@csrf_exempt
def submit_emoji(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            emoji = data.get("emoji")
            latitude = data.get("latitude")
            longitude = data.get("longitude")

            if not all([emoji, latitude, longitude]):
                return JsonResponse({"status": "fail", "message": "Missing required fields"})

            emoji_submission = EmojiSubmission(emoji=emoji, latitude=latitude, longitude=longitude)
            emoji_submission.save()

            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "fail", "message": str(e)})
    return JsonResponse({"status": "fail", "message": "Invalid request method"})
