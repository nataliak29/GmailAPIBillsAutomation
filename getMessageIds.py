
def getMessageIds(service,store_dir,from_address,min_date):
    
    messages = service.users().messages().list(userId="me",q=from_address+" after: "+min_date).execute()
 
    message_list=[]
    for i in range(len(messages["messages"])):
        message_id=messages["messages"][i]["id"]
        message_list.append(message_id)


    return message_list





