from django.shortcuts import render
from django.http import HttpResponse
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

# Create your views here.

token = 'sfsfsfrereflyer'

def validate(request):
	signature = request.GET.get('signature', None)
	timestamp = request.GET.get('timestamp', None)
	nonce = request.GET.get('nonce', None)

	try:
		check_signature(token, signature, timestamp, nonce)
	except InvalidSignatureException:
		return HttpResponse(10)

	return HttpResponse(request.GET.get('echostr', None))
