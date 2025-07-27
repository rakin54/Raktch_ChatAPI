from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
# from .models import Post

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .model_loader import generate_reply

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilgpt2")


def generate_reply(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=50, do_sample=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

class ChatView(APIView):
    def post(self, request):
        message = request.data.get("message")
        if not message:
            return Response({"error": "No message provided"}, status=400)
        reply = generate_reply(message)
        return Response({"reply": reply}, status=200)

