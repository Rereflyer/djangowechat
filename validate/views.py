from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from django.views.decorators.csrf import csrf_exempt
from wechatpy import parse_message
from wechatpy.replies import TextReply

# Create your views here.

token = 'sfsfsfrereflyer'

@csrf_exempt
def index(request):
	if request.method == 'GET':
		signature = request.GET.get('signature', None)
		timestamp = request.GET.get('timestamp', None)
		nonce = request.GET.get('nonce', None)

		try:
			check_signature(token, signature, timestamp, nonce)
		except InvalidSignatureException:
			return HttpResponseBadRequest('Verify Failed')

		return HttpResponse(request.GET.get('echostr', None))

	# POST
	msg = parse_message(request.body)
	reply = TextReply(content='text reply', message=msg)
	xml = reply.render()
	return HttpResponse(xml)