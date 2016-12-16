# docker-zabbix-monitor
Docker 监控方案

1、pip install docker-py 安装python docker api接口
2、docker_collector.py 收集所有docker信息
3、check_process_discovery.py 自动发现docker container name and pose port
4、check_process_status.py 通过自动发现的pose port，检查docker内部程序状态
5、check_process_invalid.py 检查所有的无效container，并删除
6、containerdiscover.conf
Docker Zabbix Monitor

1, pip install docker-py
2, cp docker_collector.py check_process_discovery.py check_process_status.py check_process_invalid.py to /etc/zabbix/scripts/docker/
3, cp containerdiscover.conf /etc/zabbix/zabbix_agentd.d/
4, systemctl restart zabbix-agent
5, check_process_invalid.py
   This scripts will delete all invalid items,When a new container replace old container,
   You should assign your zabbix server's url username,and password.
   You should assign your zabbix db's (mysql) username,password and database.

   for example:

        url = "http://192.168.1.66/zabbix/api_jsonrpc.php"
	zabbix_user = "Admin"
	zabbix_passwd = "zabbix"
	
	auth = Auth(url, header, zabbix_user, zabbix_passwd)

	mysql_user = "zabbix"
	mysql_passwd = "zabbix"
	mysql_db = "zabbix"
	mysql_host = "192.168.221.66"
