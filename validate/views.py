from django.shortcuts import render
from django.http import HttpResponse
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

# Create your views here.

token = 'sfsfsfrereflyer'

def validate(request):
	signature = request.get('signature', None)
	timestamp = request.get('timestamp', None)
	nonce = request.get('nonce', None)

	try:
		check_signature(token, signature, timestamp, nonce)
	except InvalidSignatureException:
		return HttpResponse(10)
