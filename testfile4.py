from django.conf import settings
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserInputSerializer
import logging
from django.http import JsonResponse
from lms.djangoapps.sko_chatbot.models import *

log = logging.getLogger(__name__)

class HandleUserInput(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data

        email_template = f"""
        Name: {data["name"]}
        Email: {data["email"]}
        Phone: {data["phone"]}
        Subject: {data["subject"]}

        User Query:
        {data["user_query"]}
        """
        send_mali("Chatbot Query - " + data["name"], email_template, settings.DEFAULT_FROM_EMAIL, [settings.CHATBOT_CONTACT_EMAIL], fail_silently=False)


        return Response({"message": "Email sent!"}, status=status.HTTP_200_OK)
