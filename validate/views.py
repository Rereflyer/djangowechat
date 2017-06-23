from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from django.views.decorators.csrf import csrf_exempt
from wechatpy import parse_message
from wechatpy.replies import TextReply

from wechatpy import WeChatClient

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

def menu(request):
	app_id = "wx5b39f2c756e6be62"
	app_secret = "5deff779d96d0b38ba97abd2beda6837"
	client = WeChatClient(app_id, app_secret)
	client.menu.create({
		"button":[
			{
				"type":"click",
				"name":u"今日歌曲",
				"key":"V1001_TODAY_MUSIC"
			},
			{
				"type":"click",
				"name":u"歌手简介",
				"key":"V1001_TODAY_SINGER"
			},
			{
				"name":u"菜单",
				"sub_button":[
					{
						"type":"view",
						"name":u"搜索",
						"url":"http://www.soso.com/"
					},
					{
						"type":"view",
						"name":u"视频",
						"url":"http://v.qq.com/"
					},
					{
						"type":"click",
						"name":u"赞一下我们",
						"key":"V1001_GOOD"
					}
				]
			}
		]
	})