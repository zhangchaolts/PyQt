#coding=gbk

import sys
import urllib
import urllib2
import cookielib
import re
import time,datetime
import recognizer_dtjr.recognizer
import string

def sign(username, password):

	# 获取Cookiejar对象（存在本机的cookie消息）
	cj = cookielib.CookieJar()
	# 自定义opener,并将opener跟CookieJar对象绑定
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	# 安装opener,此后调用urlopen()时都会使用安装过的opener对象
	urllib2.install_opener(opener)

	print username + " start ..."

	is_logined = False
	try_times = 0

	while try_times < 30:

		try_times += 1

		# Step1:识别验证码
		url = "http://weixin.dtd365.com/index.php/home/account/login.html"
		html = urllib2.urlopen(url).read()

		fw = open('pics_captcha_dtjr/0.jpg', 'wb+')
		#fw = open('pics_captcha_dtjr/000' + str(try_times-1) + '.jpg', 'wb+')
		content = urllib2.urlopen('http://weixin.dtd365.com/index.php/home/index/getvcode.html').read()
		fw.write(content)
		fw.close()

		randcode = recognizer_dtjr.recognizer.recognize('pics_captcha_dtjr/0.jpg', 'pics_train_dtjr')
		#randcode = recognizer_dtjr.recognizer.recognize('pics_captcha_dtjr/000' + str(try_times-1) + '.jpg', 'pics_train_dtjr')
		#print "(" + str(try_times) + ") " + "randcode:" + randcode

		if randcode == "":
			continue

		# Step2:登录
		login_url = "http://weixin.dtd365.com/index.php/home/index/login.html"

		login_data = {	"username": username, \
						"password": password, \
						"captcha": randcode \
					}
		print login_data

		login_post_data = urllib.urlencode(login_data) 

		login_headers = {	"Accept" : "application/json, text/javascript, */*; q=0.01", \
							#"Accept-Encoding" : "gzip, deflate", \
							#"Accept-Language" :" zh-CN,zh;q=0.8", \
							#"Connection" : "keep-alive", \
							#"Content-Length" : "52", \
							"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8", \
							"Host" : "weixin.dtd365.com", \
							"Origin" : "http://weixin.dtd365.com", \
							"Referer" : "http://weixin.dtd365.com/index.php/home/account/login.html", \
							"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8", \
							"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.69 Safari/537.36", \
							"X-Requested-With" : "XMLHttpRequest" \
						}

		login_request = urllib2.Request(login_url, login_post_data, login_headers)

		login_response = opener.open(login_request).read().decode('utf8').encode('gb18030')
		#print login_response

		homepage_url = "http://weixin.dtd365.com/index.php/home/account/index.html";
		homepage_html = urllib2.urlopen(homepage_url).read().decode('utf8').encode('gb18030')
		#print homepage_html

		if homepage_html.find('上次登录') == -1:
			#print "第" + str(try_times) +"次识别验证码错误，登录失败..."
			continue
		else:
			#print "登录成功!"
			is_logined = True
			break

	if is_logined == False:
		result = "登录失败：尝试30次都登陆失败！"
		return result

	# Step3:签到

	result1 = ""
	result3 = ""

	status_url = "http://weixin.dtd365.com/index.php/home/activity/showsign.html"
	status_html = urllib2.urlopen(status_url).read().decode('utf8').encode('gb18030')

	status = ""
	status_anwser = re.search('<input type="hidden" id="showsign_status" value="(.*?)" />', status_html)
	if status_anwser:
		status = status_anwser.group(1)

	if status == "1":
		result1 = "今日已经签到过。"
	else:

		sign_url = "http://weixin.dtd365.com/index.php/home/activity/activitysign.html"

		sign_data = {"sign" : "1"}

		sign_post_data = urllib.urlencode(sign_data)

		sign_headers = {	"Referer" : "http://weixin.dtd365.com/index.php/home/activity/showsign.html", \
							"Host" : "weixin.dtd365.com", \
							"Accept" : "*/*", \
							"Origin" : "http://weixin.dtd365.com", \
							"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8", \
							"X-Requested-With" : "XMLHttpRequest", \
							"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.69 Safari/537.36" \
						}

		sign_request = urllib2.Request(sign_url, sign_post_data, sign_headers)
		sign_response = opener.open(sign_request).read().decode('utf8').encode('gb18030')

		hongbao_anwser = re.search(',"hongbao":"(.*?)"}', sign_response)
		if hongbao_anwser:
			hongbao = hongbao_anwser.group(1)
			result3 = "获得" + hongbao +"元红包。"

		status_html = urllib2.urlopen(status_url).read().decode('utf8').encode('gb18030')

		status_anwser = re.search('<input type="hidden" id="showsign_status" value="(.*?)" />', status_html)
		if status_anwser:
			status = status_anwser.group(1)
			if status == "1":
				result1 = "签到成功。"

	result2 = ""
	total_anwser = re.search('<p>已签到<br><span>(.*?)</span>&nbsp;天</p>', status_html)
	if total_anwser:
		days = total_anwser.group(1)
		result2 = "已签到" + days + "天。"

	result =  result1 + result2 + result3
	return result


if __name__ == '__main__':

	reload(sys)
	sys.setdefaultencoding("gbk")

	username_array = []
	password_array = []

	for line in file("当天金融账号密码.txt"):
		line = line.strip()
		parts = line.split(" ")
		if len(parts) == 2:
			username_array.append(parts[0])
			password_array.append(parts[1])

	print "\n【" + datetime.datetime.now().strftime("%Y-%m-%d") + "】";
 
	for i in range(len(username_array)):
		result = sign(username_array[i], password_array[i])
		print username_array[i] + ":" + result


