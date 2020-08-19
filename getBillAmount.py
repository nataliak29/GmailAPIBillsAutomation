import os
from connectToGmail import connectToGmail
from saveAttachement import GetAttachments,LogAttachmentInfo 
from getMessageIds import getMessageIds
from telegram_bot_sendtext import telegram_bot_sendtext  
from datetime import datetime, timedelta

d = datetime.today() - timedelta(days=3)
d_string=d.strftime("%Y/%m/%d")
store_dir=os.path.dirname(__file__)+"/bills/"
service=connectToGmail()
messages= getMessageIds(service,store_dir,"from:NationalGridOnlineServices@nationalgrid.com",d_string)
print(messages)

for i in range(len(messages)):
    try:
        attachmentData=GetAttachments(service, "me",messages[i], store_dir)
        LogAttachmentInfo(attachmentData[0],attachmentData[1],attachmentData[2],attachmentData[3])
        test = telegram_bot_sendtext("You received gas bill from National Grid for billing period from "+ attachmentData[1] +" to "+attachmentData[2]+". The bill amount is "+attachmentData[3])
        print("Send this message to Telegram bot --> You received gas bill from National Grid for billing period from "+ attachmentData[1] +" to "+attachmentData[2]+". The bill amount is "+attachmentData[3])
    except: continue





