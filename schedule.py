from crontab import CronTab
import os
import json

cred_file =os.path.dirname(__file__)+"/credentials/info.json"
f = open(cred_file ,)  
data = json.load(f)
anaconda_dir= data['anaconda_dir']


cron_command = anaconda_dir+' '+ os.path.dirname(__file__) +'/getBillAmount.py'
cron = CronTab(user='natkk')
job = cron.new(command=cron_command)
job.hour.every(24)

cron.write()