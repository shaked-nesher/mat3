# -*- coding: utf-8 -*-
"""
Created on Sat May  1 20:21:25 2021

@author: shaked nesher
"""
import json
def anonymous (line,unique_id):
    line=line.rstrip()
    datetime=line.split("-")[0].split(",")[0]+line.split("-")[0].split(",")[1]
    datetime=datetime.replace(".","-")
    datetime=datetime.strip()
    text="".join(line.split(":")[2:])
    return {"datetime":datetime,"id":unique_id,"text":text}
file=open("�צאט WhatsApp עם יום הולדת בנות לנויה.txt",encoding='utf-8')
## קובץ הבונוס 
#file=open("bonus.txt",encoding='utf-8')
unique_id_dic={}
dic_ls=[]
counter_id=1
textnew=" "
index=0
for line in file:
    line=line.rstrip()
    count = line.count(":")
    if "," and "-" and "." not in line:
        textnew=line
        textnew=" "+textnew
        dic_ls[index-1]["text"]+=textnew
        continue
    elif count<2:
        if "נוצרה על ידי" in line:
            chat_name=line.split("-")[1].split('"')[1]
            date_creation=line.split("-")[0].split(",")[0]+line.split("-")[0].split(",")[1]
            date_creation=date_creation.replace(".","-")
            date_creation=date_creation.strip()
            creator=line.split("נוצרה על ידי")[1]
        continue
    name="".join(line.split("-")[1:]).split(":")[0]
    if name in unique_id_dic :
        unique_id=unique_id_dic[name]
        dic_ls.append(anonymous(line,unique_id))
    else:
        unique_id_dic[name]=counter_id
        dic_ls.append(anonymous(line,counter_id))
        counter_id=counter_id+1
    index+=1
participants_of_num=counter_id-1     
dic_metadata={"chat_name":chat_name,"date_creation":date_creation,"participants_of_num":participants_of_num,"creator":str(creator)}                          
dic_all={"messages":dic_ls,"metadata":dic_metadata}
with open(dic_metadata["chat_name"] + ".txt",'w',encoding='utf8') as fp:
   json.dump(dic_all, fp,ensure_ascii=False,indent=4)
   



  
    

