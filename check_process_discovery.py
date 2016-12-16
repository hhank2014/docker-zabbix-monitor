#!/usr/bin/python
#Usage etcd key/value IP:PORT
#
import commands

stat, proStr = commands.getstatusoutput("docker ps | egrep -v 'CONTAINER|registrator' | awk '{print $NF,$(NF-1)}'|awk -F '->' '{print $1}'|awk -F ':' '{print $1,$2}' |awk '{print $1,$3}'")
tmpList = proStr.split("\n")
newList = []
for i in tmpList:
        new = i.split()
        newList.append(new)
json_data = "{\n" + "\t" + '"data":[' + "\n"
for net in newList:
        if net != newList[-1]:
                json_data = json_data + "\t\t" + "{" + "\n" + "\t\t" + '"{#PNAME}":"' + str(net[0]) + "\",\n" + "\t\t" + '"{#PPORT}":"' + str(net[1]) + "\"},\n"
        else:
                json_data = json_data + "\t\t" + "{" + "\n" + "\t\t" + '"{#PNAME}":"' + str(net[0]) + "\",\n" + "\t\t" + '"{#PPORT}":"' + str(net[1]) + "\"}]" + "\n" +"}"

print json_data
