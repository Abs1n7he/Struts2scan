#!/usr/bin/env python
# coding=utf-8
from gevent import monkey;monkey.patch_all()#并发,要放最前面
from gevent.pool import Pool

import sys
import gevent
import re
import urllib
import requests
import urllib3
urllib3.disable_warnings()
from module.proxy import proxies
from module.color import color
import os
import time
import argparse


from payloads.s2_001 import s2_001,s2_001_exp
from payloads.s2_005 import s2_005,s2_005_exp
from payloads.s2_007 import s2_007,s2_007_exp
from payloads.s2_008 import s2_008,s2_008_exp
from payloads.s2_009 import s2_009,s2_009_exp
from payloads.s2_013 import s2_013,s2_013_exp
from payloads.s2_015 import s2_015,s2_015_exp
from payloads.s2_032 import s2_032,s2_032_exp
from payloads.s2_045 import s2_045,s2_045_exp
from payloads.s2_046 import s2_046,s2_046_exp
from payloads.s2_048 import s2_048,s2_048_exp
from payloads.s2_052 import s2_052,s2_052_exp
from payloads.s2_053 import s2_053,s2_053_exp
from payloads.s2_057 import s2_057,s2_057_exp
from payloads.s2_059 import s2_059,s2_059_exp
from payloads.s2_061 import s2_061,s2_061_exp


print(color.cyan(
                "  _____ _              _       ___\r\n"+
                " / ____| |            | |     |__ \\\r\n"+
                "| (___ | |_ _ __ _   _| |_ ___   ) |___  ___ __ _ _ __\r\n"+
                " \___ \| __| '__| | | | __/ __| / // __|/ __/ _` | '_ \\ \r\n")+
color.magenta(  " ____) | |_| |  | |_| | |_\__ \/ /_\__ \ (_| (_| | | | |\r\n"+
                "|_____/ \__|_|   \__,_|\__|___/____|___/\___\__,_|_| |_|\r\n"+
                "V1.0                                        by Abs1n7he\r\n"))
#figlet -f big Struts2scan


def list():
    

    print('+--------------------------------------------------------------+')
    print('+              CVE Number        Struts2 Version               +')    
    print('+   s2-001     CVE-2007-4556     2.0.0-2.0.8                   +')
    print('+   s2-005     CVE-2010-1870     2.0.0-2.1.8.1                 +')
    print('+   s2-007     CVE-2012-0838     2.0.0-2.2.3                   +')
    print('+   s2-008     CVE-2012-0391     2.1.0-2.3.1                   +')
    print('+   s2-009     CVE-2011-3923     2.1.0-2.3.1.1                 +')
    print('+   s2-013     CVE-2013-1966     2.0.0-2.3.14                  +')
    print('+   s2-015     CVE-2013-2135     2.0.0-2.3.14.2                +')
    print('+   s2-032     CVE-2016-3081     2.3.20-2.3.28                 +')
    print('+   S2-045     CVE-2017-5638     2.3.5-2.3.31                  +')
    print('+   s2-046     CVE-2017-5638     2.3.5-2.3.31  2.5.0-2.5.10    +')
    print('+   s2-048     CVE-2017-9791     2.3.x                         +')
    print('+   s2-052     CVE-2017-9805     2.1.2-2.3.33  2.5-2.5.12      +')
    print('+   S2-053     CVE-2017-12611    2.0.1-2.3.33  2.5-2.5.10      +')
    print('+   s2-057     CVE-2018-11776    <=2.3.34  2.5.16              +')
    print('+   s2-059     CVE-2019-0230     2.0.0-2.5.20                  +')
    print('+   s2-061     CVE-2020-17530    2.0.0-2.5.25                  +')
    print('+--------------------------------------------------------------+')

def RunExp(url,exp):
    if exp == "s2_001":
        s2_001_exp(url)
    elif exp == "s2_005":
        s2_005_exp(url)
    elif exp == "s2_007":
        s2_007_exp(url)
    elif exp == "s2_008":
        s2_008_exp(url)
    elif exp == "s2_009":
        s2_009_exp(url)
    elif exp == "s2_013":
        s2_013_exp(url)
    elif exp == "s2_015":
        s2_015_exp(url)
    elif exp == "s2_032":
        s2_032_exp(url)
    elif exp == "s2_045":
        s2_045_exp(url)
    elif exp == "s2_046":
        s2_046_exp(url)
    elif exp == "s2_048":
        s2_048_exp(url)
    elif exp == "s2_052":
        s2_052_exp(url)
    elif exp == "s2_053":
        s2_053_exp(url)
    elif exp == "s2_057":
        s2_057_exp(url)
    elif exp == "s2_059":
        s2_059_exp(url)
    elif exp == "s2_061":
        s2_061_exp(url)
    else:
        print(color.red("[!]This exp is not supported..."))



def RunScan(targeturl):
    poclist = [
        's2_001("{0}")'.format(targeturl),
        's2_005("{0}")'.format(targeturl),
        's2_008("{0}")'.format(targeturl),
        's2_009("{0}")'.format(targeturl),
        's2_007("{0}")'.format(targeturl),
        's2_013("{0}")'.format(targeturl),
        's2_015("{0}")'.format(targeturl),
        's2_032("{0}")'.format(targeturl),
        's2_045("{0}")'.format(targeturl),
        's2_046("{0}")'.format(targeturl),
        's2_048("{0}")'.format(targeturl),
        's2_052("{0}")'.format(targeturl),
        's2_053("{0}")'.format(targeturl),
        's2_057("{0}")'.format(targeturl),
        's2_059("{0}")'.format(targeturl),
        's2_061("{0}")'.format(targeturl),
    ]
    def pocexec(pocstr):
        exec(pocstr)
        gevent.sleep(0)
    try:
        pool = Pool(10)
        threads = [pool.spawn(pocexec, item) for item in poclist]
        gevent.joinall(threads)
    except:
        exit()



def SetProxy(Proxy):
    scheme = urllib.parse.urlparse(Proxy).scheme
    proxies.update({'http': Proxy,'https': Proxy})




def arg():
    parser = argparse.ArgumentParser(usage="python Struts2scan.py [options]", add_help=False)

    target = parser.add_argument_group("target", "select a single or batch scan.")
    target.add_argument("-u",  dest="url",    type=str,  help="target URL")
    target.add_argument("-f", dest="file",   type=str,  help="target list file")

    other = parser.add_argument_group("other")
    other.add_argument("-e",  dest="exp",    type=str,  help="use a exp")
    other.add_argument("-p", dest="proxy",  type=str,  help="proxy")
    other.add_argument("-h", action="help",            help="help")
    other.add_argument("--list", dest="list", action='store_false', help="display the list of exps")

    example = parser.add_argument_group("examples")
    example.add_argument(action='store_false',
                         dest="python Struts2scan.py -u http://example.com\n  "
                              "python Struts2scan.py -u http://example.com -e s2_045\n  "
                              "python Struts2scan.py -f list.txt\n  "
                              "python Struts2scan.py -f list.txt -p http://127.0.0.1:8080\n  ")
    return parser.parse_args()




if __name__ == '__main__':
    args = arg()

    if args.list is False: 
        list()
        exit()

    if args.proxy:
        if re.findall('[a-zA-z]+://[^\s]{1,}(:{0,1})(\d*)', args.proxy):
            SetProxy(args.proxy)
            print(color.red_twinkle("[+]Proxy:"+proxies['http']))
        else:
            print(color.red("[!]代理格式错误"))
            exit()
        

    if args.url and args.exp:
        if args.url.find('http')==-1:
            print(color.red("[!]url无法识别"))
            exit()
        RunExp(args.url,args.exp)

    elif args.url and not args.exp:
        if args.url.find('http')==-1:
            print(color.red("[!]url无法识别"))
            exit()
        else:
            RunScan(args.url)

    elif args.file and not args.exp:
        with open(args.file, 'r') as f:
            for line in f:
                line = line.strip()# 过滤杂质
                print("[=]Scan：%s"%line)
                RunScan(line) 
    else:
        exit()





