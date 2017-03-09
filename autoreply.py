#encoding:utf-8

import itchat, time

itchat.auto_login()

@itchat.msg_register(['Text', 'Picture', 'Map','Card', 'Note', 'Sharing','Recording','Attachment','Video'])

def text_reply(msg):
	if msg['Type'] == 'Text':
		reply =u'消息：'+'[%s]'%(msg['Text'])	
		print '[%s]:[%s]'%(msg['FromUserName'],msg['Text'])
	elif msg['Type']=='Picture':
		reply =u'图片'
		print '[%s]:[%s]'%(msg['FromUserName'],reply)
	elif msg['Type'] == 'Recording':
		reply = u"语音"
		print '[%s]:[%s]'%(msg['FromUserName'],reply)
	elif msg['Type'] == 'Attachment':
		reply = u"文件" 
		print '[%s]:[%s]'%(msg['FromUserName'],reply)
	elif msg['Type'] == 'Video':
		reply = u"视频"
		print '[%s]:[%s]'%(msg['FromUserName'],reply)
	elif msg['Type'] == 'Note':
		reply = u"通知"
		print '[%s]:[%s]'%(msg['FromUserName'],reply)
	elif msg['Type'] == 'Sharing':
		reply = u"分享"
		print '[%s]:[%s]'%(msg['FromUserName'],reply)
	else:
		reply = u'通知'
		print '[%s]:[%s]'%(msg['FromUserName'],reply)

	itchat.send(u'Time:%s，Message:%s'%(time.ctime(),reply),toUserName='filehelper')
	itchat.send(u'您好，我收到了您在[%s]发送的%s，您呼叫的用户正在图书馆思考人生，稍后会回复您哒'%( time.ctime(),reply), msg['FromUserName'])

itchat.run()