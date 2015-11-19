#coding=gbk

import sys
import urllib
import urllib2
import cookielib
import re
import time,datetime
import recognizer_dtjr.recognizer
import string
import multiprocessing

def sign(queue, line_ptr, username, password):

	# ��ȡCookiejar���󣨴��ڱ�����cookie��Ϣ��
	cj = cookielib.CookieJar()
	# �Զ���opener,����opener��CookieJar�����
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	# ��װopener,�˺����urlopen()ʱ����ʹ�ð�װ����opener����
	urllib2.install_opener(opener)

	print username + " start ..."

	is_logined = False
	try_times = 0

	while try_times < 20:

		try_times += 1

		# Step1:ʶ����֤��
		url = "http://weixin.dtd365.com/index.php/home/account/login.html"
		html = urllib2.urlopen(url).read()

		fw = open('pics_captcha_dtjr/' + str(line_ptr) + '.jpg', 'wb+')
		content = urllib2.urlopen('http://wxticket.dtd365.com/index.php/home/index/getvcode.html').read()
		fw.write(content)
		fw.close()

		randcode = recognizer_dtjr.recognizer.recognize('pics_captcha_dtjr/' + str(line_ptr) + '.jpg', 'pics_train_dtjr')
		print "(" + str(line_ptr) + "," + str(try_times) + ") " + "randcode:" + randcode

		# Step2:��¼
		login_url = "http://weixin.dtd365.com/index.php/home/index/login.html"

		login_data = {	"username": username, \
						"password": password, \
						"captcha": randcode \
					}
		print login_data

		login_post_data = urllib.urlencode(login_data) 

		login_headers = {	"Referer" : "http://weixin.dtd365.com/index.php/home/account/login.html", \
							"Host" : "weixin.dtd365.com", \
							"Accept" : "*/*", \
							"Origin" : "http://weixin.dtd365.com", \
							"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8", \
							"X-Requested-With" : "XMLHttpRequest", \
							"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.69 Safari/537.36" \
						}

		login_request = urllib2.Request(login_url, login_post_data, login_headers)

		login_response = opener.open(login_request).read().decode('utf8').encode('gb18030')

		homepage_url = "http://weixin.dtd365.com/index.php/home/account/index.html";
		homepage_html = urllib2.urlopen(homepage_url).read().decode('utf8').encode('gb18030')
		#print homepage_html

		if homepage_html.find('�ϴε�¼') == -1:
			#print "��" + str(try_times) +"��ʶ����֤����󣬵�¼ʧ��..."
			continue
		else:
			#print "��¼�ɹ�!"
			is_logined = True
			break

	if is_logined == False:
		#print "����20�ζ���½ʧ�ܣ���������Ϊ���ˣ����������ֶ�ǩ����~\n"
		result = "��¼ʧ�ܣ�����20�ζ���½ʧ�ܣ�"
		queue.put(str(line_ptr) + " " + result)
		return

	# Step3:ǩ��

	result1 = ""
	result3 = ""

	status_url = "http://weixin.dtd365.com/index.php/home/activity/showsign.html"
	status_html = urllib2.urlopen(status_url).read().decode('utf8').encode('gb18030')

	status = ""
	status_anwser = re.search('<input type="hidden" id="showsign_status" value="(.*?)" />', status_html)
	if status_anwser:
		status = status_anwser.group(1)

	if status == "1":
		result1 = "�����Ѿ�ǩ������"
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
			result3 = "���" + hongbao +"Ԫ�����"

		status_html = urllib2.urlopen(status_url).read().decode('utf8').encode('gb18030')

		status_anwser = re.search('<input type="hidden" id="showsign_status" value="(.*?)" />', status_html)
		if status_anwser:
			status = status_anwser.group(1)
			if status == "1":
				result1 = "ǩ���ɹ���"

	result2 = ""
	total_anwser = re.search('<p>��ǩ��<br><span>(.*?)</span>&nbsp;��</p>', status_html)
	if total_anwser:
		days = total_anwser.group(1)
		result2 = "��ǩ��" + days + "�졣"

	result =  result1 + result2 + result3
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

    print "\n��" + datetime.datetime.now().strftime("%Y-%m-%d") + "��";
    
    account_list = []
    for line in file("��������˺�����.txt"):
        line = line.strip()
        parts = line.split(" ")
        if len(parts) == 2:
            account_list.append([parts[0], parts[1]])

    status_list = sign_all(account_list)

    for status in status_list:
        print status.encode('gbk')
