from django.shortcuts import render
import cv2

# Create your views here.

def index(requests):
    return render(requests, 'index.htm')
