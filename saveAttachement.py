import base64
from apiclient import errors
import re
from datetime import date
from csv import writer


def SaveAttachment (file_data_date,file_data,store_dir):
    path = ''.join([store_dir, 'National_Grid_Gas_BillPeriod_'+file_data_date.replace("/", "_")+'.txt'])
    f = open(path, 'w')
    f.write(file_data.decode('utf-8'))
    f.close()
    print('Saved attachement to '+path)


def GetAttachments(service, user_id, msg_id, store_dir):
  """Get National Grid Bill attachement from Message with given id and save it with ending Bill period date"""
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()
    file_data = base64.urlsafe_b64decode(message['payload']['parts'][0]['parts'][0]['body']['data'].encode('UTF-8'))
    file_data_date=re.search("([0-9]{2}\/[0-9]{2}\/[0-9]{4} - [0-9]{2}\/[0-9]{2}\/[0-9]{4})", file_data.decode('utf-8'))
    print('Found attachememnt for billing period '+str(file_data_date.group()))
    file_data_date_start=file_data_date.group()[:10]
    file_data_date=file_data_date.group()[13:]
    bill_amount=re.search("\$\d+(?:\.\d+)?", file_data.decode('utf-8')).group()
    SaveAttachment (file_data_date,file_data,store_dir)
    return msg_id,file_data_date_start,file_data_date,bill_amount

  except errors.HttpError as error:
    print ('An error occurred: %s') % error


def AppendListAsRow(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

def LogAttachmentInfo(msg_id,file_data_date_start,file_data_date,bill_amount):
    print('Logging data to bills_history.csv')
    row_contents = ['National_Grid',msg_id,file_data_date_start,file_data_date,bill_amount,date.today()]
    AppendListAsRow('bills/bills_history.csv', row_contents)
