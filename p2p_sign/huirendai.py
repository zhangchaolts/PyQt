#coding=gbk

import sys
import urllib
import urllib2
import cookielib
import re
import time,datetime
import string
import multiprocessing

def sign(queue, line_ptr, username, password):

	# 获取Cookiejar对象（存在本机的cookie消息）
	cj = cookielib.CookieJar()
	# 自定义opener,并将opener跟CookieJar对象绑定
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	# 安装opener,此后调用urlopen()时都会使用安装过的opener对象
	urllib2.install_opener(opener)

	print username + " start ..."

	# Step1:登录
	login_url = "http://m.huirendai.com/user/login"

	login_data = {	"username": username, \
					"password": password, \
					"referer": "", \
					"backurl": "", \
					"operation": "" \
				}

	login_post_data = urllib.urlencode(login_data) 

	login_headers = {	"Referer" : "http://m.huirendai.com/user/login", \
						"Host" : "m.huirendai.com", \
						"Accept" : "*/*", \
						"Origin" : "http://m.huirendai.com", \
						"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8", \
						"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.69 Safari/537.36" \
					}

	login_request = urllib2.Request(login_url, login_post_data, login_headers)

	login_response = opener.open(login_request).read().decode('utf8').encode('gb18030')
	#print login_response
	
	if login_response.find('您好，') == -1:
		result = "登录失败！"
		queue.put(str(line_ptr) + " " + result)
		return

	# Step2:签到
	sign_url = "http://m.huirendai.com/account/signin"

	sign_headers = {	"Referer" : "http://m.huirendai.com/account/point", \
						"Host" : "m.huirendai.com", \
						"Accept" : "*/*", \
						"X-Requested-With" : "XMLHttpRequest",
						"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.69 Safari/537.36" \
					}

	sign_request = urllib2.Request(sign_url, headers = sign_headers)
	sign_response = opener.open(sign_request).read().decode('utf8').encode('gb18030')
	#print sign_response
	#sign_response = '{"r":"00","m":"\u7b7e\u5230\u6210\u529f","d":{"np":"7"}}'

	result1 = ""

	CURR_POINTS = ""
	sign_anwser = re.search('"np":"(.*?)"', sign_response)
	if sign_anwser:
		CURR_POINTS = sign_anwser.group(1)
		result1 = "今日签到获得" + CURR_POINTS + "惠米。"
	else:
		result1 =  "今日已经签到过！"

	# Step3：获取总惠米数量
	home_url = "http://m.huirendai.com/account/point"
	req = urllib2.Request(home_url,headers = sign_headers)
	home_html = urllib2.urlopen(req).read().decode('utf-8').encode('gbk')
	#print home_html

	result2 = ""

	totalPopularity = ""
	home_anwser = re.search('<div class="content">(.*?)</div>', home_html)
	if home_anwser:
		totalPopularity = home_anwser.group(1)
		result2 = "总惠米为" + totalPopularity + "。"
	else:
		print "no"

	result = result1 + result2

	print username + " " + result
	queue.put(str(line_ptr) + " " + result)
	return


def get_status_list(queue):
	status_list = [None] * queue.qsize()
	while queue.empty() != True:
		parts = queue.get().split(" ")
		if len(parts) == 2:
			ptr = string.atoi(parts[0])
			status_list[ptr] = parts[1]
	return status_list


def sign_all(account_list):
	queue = multiprocessing.Queue()
	jobs = []
	for i in xrange(len(account_list)):
		job = multiprocessing.Process(target=sign, args=(queue, i, account_list[i][0], account_list[i][1]))
		jobs.append(job)
		job.start()
	for job in jobs:
		job.join()
	return get_status_list(queue)


if __name__ == '__main__':

	reload(sys)
	sys.setdefaultencoding("gbk")

	print "\n【" + datetime.datetime.now().strftime("%Y-%m-%d") + "】";

	account_list = []
	for line in file("惠人贷账号密码.txt"):
		line = line.strip()
		parts = line.split(" ")
		if len(parts) == 2:
			account_list.append([parts[0], parts[1]])

	status_list = sign_all(account_list)

	for status in status_list:
		print status.encode('gbk')

