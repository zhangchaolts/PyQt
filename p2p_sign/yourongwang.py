#coding:gbk
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
	token_url = 'http://www.yrw.com/security/login'
	token_html = urllib2.urlopen(token_url).read()

	xToken = ""
	token_anwser = re.search('name="xToken" value="(.*?)"', token_html)
	if token_anwser:
		xToken = token_anwser.group(1)
		#print xToken
	else:
		return "��¼ʧ�ܣ���ȡtokenʧ�ܣ�"

	# Step2:��¼
	login_url = "https://www.yrw.com/security/logined"

	login_data = {	"xToken" : xToken, \
					"username": username, \
					"password": password, \
					"pngCode": "", \
					"loginSource": "0" \
				}

	login_post_data = urllib.urlencode(login_data) 

	login_headers = {	"Referer" : "https://www.yrw.com/security/login", \
						"Host" : "www.yrw.com", \
						"Accept" : "*/*", \
						"X-Requested-With" : "XMLHttpRequest", \
						"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8", \
						"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.69 Safari/537.36" \
					}

	login_request = urllib2.Request(login_url, login_post_data, login_headers)

	login_response = opener.open(login_request).read().decode('utf8').encode('gbk')
	#print login_response
	
	if login_response.find('"success":true') == -1:
		return "��¼ʧ�ܣ�"

	# Step3:ǩ��
	sign_url = "https://www.yrw.com/member/check/?_=" + str(int(time.mktime(datetime.datetime.now().timetuple()))) + "000"
	#print sign_url
	sign_request = urllib2.Request(sign_url)
	sign_response = opener.open(sign_request).read()
	#print sign_response
	#sign_response = '{"error":false,"page":null,"result":{"checkDate":1441268468855,"checkSource":0,"createTime":null,"gainPopularity":2,"id":null,"memberId":110850038887,"popularityDouble":1},"resultCode":null,"resultCodeEum":null,"resultCodeList":[],"resultList":null,"success":true}'

	result1 = ""

	gainPopularity = ""
	sign_anwser = re.search('"gainPopularity":(.*?),', sign_response)
	if sign_anwser:
		gainPopularity = sign_anwser.group(1)
		result1 = "����ǩ�����" + gainPopularity + "����ֵ��"
	else:
		result1 = "�����Ѿ�ǩ������"

	# Step4����ȡ������ֵ����
	home_url = "https://www.yrw.com/member/home"
	home_html = urllib2.urlopen(home_url).read()
	#print home_html

	result2 = ""

	totalPopularity = ""
	home_anwser = re.search('<dd><span class="f-ff-din"><a href="/coupon/reputation">(.*?)</a></span>', home_html)
	if home_anwser:
		totalPopularity = home_anwser.group(1)
		result2 = "������ֵΪ" + totalPopularity + "��"
	
	result = result1 + result2
	return result


if __name__ == '__main__':

	reload(sys)
	sys.setdefaultencoding("gbk")


	username_array = []
	password_array = []

	for line in file("�������˺�����.txt"):
		line = line.strip()
		parts = line.split(" ")
		if len(parts) == 2:
			username_array.append(parts[0])
			password_array.append(parts[1])

	print "\n��" + datetime.datetime.now().strftime("%Y-%m-%d") + "��";

	for i in range(len(username_array)):
		result = sign(username_array[i], password_array[i])
		print username_array[i] + ":" + result

