import http
import json

from django.db import transaction
from django.http import JsonResponse

from webapp.models import Announcement


def set_status_accept(request):
    try:
        if request.body:
            body = json.loads(request.body)
            if body["status"] == "accept":
                Announcement.objects.get(pk=body["id"]).set_accept_status()
                return JsonResponse(data={"status": "success"}, status=http.HTTPStatus.OK)
    except:
        return JsonResponse(data={"status": "failed"}, status=http.HTTPStatus.NOT_FOUND)


def set_status_reject(request):
    try:
        if request.body:
            body = json.loads(request.body)
            if body["status"] == "reject":
                Announcement.objects.get(pk=body["id"]).set_reject_status()
                return JsonResponse(data={"status": "success"}, status=http.HTTPStatus.OK)
    except:
        return JsonResponse(data={"status": "failed"}, status=http.HTTPStatus.NOT_FOUND)
