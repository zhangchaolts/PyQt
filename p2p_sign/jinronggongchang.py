#coding=gbk

import sys
import urllib
import urllib2
import cookielib
import re
import time,datetime

def sign(username, password):

	# ��ȡCookiejar���󣨴��ڱ�����cookie��Ϣ��
	cj = cookielib.CookieJar()
	# �Զ���opener,����opener��CookieJar�����
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	# ��װopener,�˺����urlopen()ʱ����ʹ�ð�װ����opener����
	urllib2.install_opener(opener)

	# Step1:��ȡtoken
	token_url = 'https://passport.9888.cn/passport/login'
	token_html = urllib2.urlopen(token_url).read()

	xToken = ""
	token_anwser = re.search('name="lt" value="(.*?)"', token_html)
	if token_anwser:
		xToken = token_anwser.group(1)
		#print xToken
	else:
		return "��¼ʧ�ܣ���ȡtokenʧ�ܣ�"

	# Step2:��¼
	login_url = "https://passport.9888.cn/passport/login"

	login_data = {	"username": username, \
					"password": password, \
					"lt": xToken, \
					"execution": "e1s1", \
					"_eventId": "submit" \
				}

	login_post_data = urllib.urlencode(login_data) 

	login_headers = {	#"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", \
						#"Accept-Encoding": "gzip, deflate", \
						"Accept-Language": "zh-CN,zh;q=0.8", \
						#"Cache-Control": "max-age=0", \
						#"Connection": "keep-alive", \
						#"Content-Length" : "117", \
						"X-Requested-With" : "XMLHttpRequest", \
						#"Content-Type" : "application/x-www-form-urlencoded", \
						"Host" : "passport.9888.cn", \
						#"Origin" : "https://passport.9888.cn", \
						"Referer" : "https://passport.9888.cn/passport/login", \
						"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.69 Safari/537.36" \
					}

	login_request = urllib2.Request(login_url, login_post_data, login_headers)

	login_response = opener.open(login_request).read()
	#print login_response
	if login_response.find("http://www.9888.cn?islogin=true&pc=1") == -1:
		return "��¼ʧ�ܣ�"

	#�ǵô������ҳ��������ǩ��
	homepage_url = "http://www.9888.cn/account/home.shtml";
	homepage_html = urllib2.urlopen(homepage_url).read().decode('utf8').encode('gb18030')
	#print homepage_html
	#if homepage_html.find('�˳�') == -1:
	#	print "��¼ʧ��!"
	#	return

	# Step3:ǩ��
	sign_url = "http://www.9888.cn/account/signMethod.do?_" + str(int(time.mktime(datetime.datetime.now().timetuple()))) + "000"
	#print sign_url

	sign_request = urllib2.Request(sign_url)
	sign_response = opener.open(sign_request).read()
	print sign_response

	result1 = ""

	gainPopularity = ""
	sign_anwser = re.search('"returnAmount":(.*?),', sign_response)
	if sign_anwser:
		gainPopularity = sign_anwser.group(1)
		result1 =  "����ǩ�����" + gainPopularity + "������"
	else:
		result1 =  "�����Ѿ�ǩ������"

	patten = ""

	result3 = ""
	if sign_response.find('"win":"true"') != -1:
		result3 = "��ϲ��ú����"
		patten = '"G_AVAILABLE_BALANCE":(.*?),'
	else:
		result3 = "�޺����"
		patten = '"G_AVAILABLE_BALANCE":(.*?)}'

	result2 = ""
	totalPopularity = ""
	sign_anwser = re.search(patten, sign_response)
	if sign_anwser:
		totalPopularity = sign_anwser.group(1)
		result2 = "�ܹ���Ϊ" + totalPopularity + "��"


	result = result1 + result2 + result3
	return result

if __name__ == '__main__':

	reload(sys)
	sys.setdefaultencoding("gbk")

	username_array = []
	password_array = []

	for line in file("���ڹ����˺�����.txt"):
		line = line.strip()
		parts = line.split(" ")
		if len(parts) == 2:
			username_array.append(parts[0])
			password_array.append(parts[1])

	print "\n��" + datetime.datetime.now().strftime("%Y-%m-%d") + "��";
 
	for i in range(len(username_array)):
		result = sign(username_array[i], password_array[i])
		print username_array[i] + ":" + result
