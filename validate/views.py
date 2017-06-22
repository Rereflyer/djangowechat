from django.shortcuts import render
from django.http import HttpResponse
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

# Create your views here.

token = 'sfsfsfrereflyer'

def validate(request):
	signature = request.REQUEST.get('signature', None)
	timestamp = request.REQUEST.get('timestamp', None)
	nonce = request.REQUEST.get('nonce', None)

	try:
		check_signature(token, signature, timestamp, nonce)
	except InvalidSignatureException:
		return HttpResponse(10)
