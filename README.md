## docker-zabbix-monitor

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
	mysql_user = "zabbix"
	mysql_passwd = "zabbix"
	mysql_db = "zabbix"
	mysql_host = "192.168.221.66"
