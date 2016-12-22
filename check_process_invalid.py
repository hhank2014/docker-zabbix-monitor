#!/usr/bin/env python
#conding=utf-8
#by huangjie

import json
import urllib2
import MySQLdb
import commands

#You should install MySQL-python
#for example CentOS 
#yum install -y MySQL-python

def Auth(url, header, zabbix_user, zabbix_passwd):
	
	data = json.dumps(
        {
                "jsonrpc": "2.0",
                "method": "user.login",
                "params": {
                "user": zabbix_user,
                "password": zabbix_passwd
                },
        "id": 0
        })

	request = urllib2.Request(url,data)
	for key in header:
	   request.add_header(key,header[key])
	try:
	   result = urllib2.urlopen(request)
	except URLError as e:
	   print "Auth Failed, Please Check Your Name AndPassword:",e.code
	else:
	   response = json.loads(result.read())
	   result.close()
	return response['result']

def DeleteItemID(itemid, auth):
	
	Id=[]
	for i in itemid:
		id = i[0]
        	Id.append(id)
       
	data = json.dumps(
        {
                "jsonrpc": "2.0",
                "method": "item.delete",
		"params":Id,
	"auth": auth,
        "id": 0
        })
        request = urllib2.Request(url,data)
        for key in header:
           request.add_header(key,header[key])
        try:
           result = urllib2.urlopen(request)
        except URLError as e:
           print "Auth Failed, Please Check Your Name AndPassword:",e.code
        else:
           response = json.loads(result.read())
           result.close()

def GetItemID(mysql_host, mysql_user, mysql_passwd, mysql_db, hostid):
	
	mysql_conn = MySQLdb.connect(host=mysql_host, user=mysql_user,passwd=mysql_passwd, db=mysql_db)
	db_cursor = mysql_conn.cursor()
	sql = "select itemid from items where state=1 and hostid=\"%s\"" %(hostid)
	db_cursor.execute(sql)
	result = db_cursor.fetchall()
	return result

def GetIP():
	
	stat, proStr = commands.getstatusoutput("ifconfig eth0 | grep netmask | awk -F 'netmask' '{print $1}'|awk '{print $2}'")
	ip =  proStr
	return ip

def GetHostId(ip):
        
	mysql_conn = MySQLdb.connect(host=mysql_host, user=mysql_user,passwd=mysql_passwd, db=mysql_db)
        db_cursor = mysql_conn.cursor()
	sql = "select hostid from interface where ip = \"%s\"" %(ip)
	db_cursor.execute(sql)
	result = db_cursor.fetchall()
	
	for i in result:
		return i[0]

if __name__ == "__main__":
	
        url = "http://192.168.221.66/zabbix/api_jsonrpc.php"
        header = {"Content-Type":"application/json"}
	zabbix_user = "Admin"
	zabbix_passwd = "zabbix"
	
	auth = Auth(url, header, zabbix_user, zabbix_passwd)

	mysql_user = "zabbix"
	mysql_passwd = "zabbix"
	mysql_db = "zabbix"
	mysql_host = "192.168.221.66"

	ip = GetIP()
	hostid = GetHostId(ip)
	itemid = GetItemID(mysql_host, mysql_user, mysql_passwd, mysql_db, hostid)
	DeleteItemID(itemid, auth)
