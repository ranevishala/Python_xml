from xml.dom import minidom
import xml.etree.ElementTree as ET
import csv
import operator
from datetime import datetime
import time
import sys
class Goods:
    def updateOnReturn(self, goodsfile, goodsNo):
        flag = 0
        try:
            tree1 = ET.parse(goodsfile)
            root1 = tree1.getroot()
        except ET.ParseError:
            flag = 1
        stat = ''
        if flag == 1:
            print("Goods not available")
            return True
        else :
            for goodn in root1.findall('goods'):
                num = goodn.find('number').text
                stat = goodn.find('status').text
                if int(num) == goodsNo:
                    if stat == 'available':
                        print("Status already available")
                    else :
                        goodn.find('status').text = 'available'
                        tree1.write(goodsfile)
                        print("Status Updated to available")
                    return True
                
                
    def checkGoodsType(self, goodsfile, username, goodsType):
        flag = 0
        try:
            tree1 = ET.parse(goodsfile)
            root1 = tree1.getroot()
        except ET.ParseError:
            flag = 1
        stat = ''
        if flag == 1:
            print("Goods not available")
            return True
        else :
            for goodn in root1.findall('goods'):
                typ = goodn.find('type').text
                gname = goodn.find('name').text
                gid = goodn.find('id').text
                stat = goodn.find('status').text
                if goodsType == typ:
                    if stat == 'available':
                        goodn.find('status').text = 'unavailable'
                        tree1.write(goodsfile)
                        print(gname, "with id", gid, "is successfully assigned to", username)
                    return True
                
                
    def validateUsernamePassword(self, userfile, user, passwrd):
        tree = ET.parse(userfile)
        root = tree.getroot()
        for usern in root.findall('user'):
            uname = usern.find('username').text
            pwd = usern.find('password').text
            if uname == user and pwd == passwrd:
                return True