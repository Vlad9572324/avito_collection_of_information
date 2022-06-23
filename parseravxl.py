import random
import xlwt
from bs4 import BeautifulSoup
import requests
import lxml
import time
import re
rand1=str(random.randint(1, 15))+"."
rand2=str(random.randint(1, 100))
times=float(rand1+rand2)
def jsonpars(seach,script):
    spisokgg9=[]
    for i in script:
        i=str(i.text)        
        if seach in i:
            i=str(i)
            cg=i.find(seach)
            if cg!=-1:
                
                g=i.find(seach)+len(seach)
                k=g
                while i[k]!=',' and i[k]!='}':
                    k+=1
                if i[g:k]!="":
                    spisokgg9+=[i[g:k]]
                    
                    
        
    return spisokgg9
def parserstr(ssilk):
    ll=session.get(ssilk)
    
    #print(ll)
    #print(ssilk)
    soup = BeautifulSoup(ll.text, "lxml")
    print(soup)
    spisokgg=["item-description-html","style-item-description-html-1_RNo","item-description-text","style-item-description-1e2Yo"]
    gg = sum([soup.find_all(class_=x) for x in spisokgg],[])
    gg=gg[0].text if gg !=[] else "Не нашел" # содержание
    
    spisokgg1=["title-info-title-text"]
    gg1 = sum([soup.find_all(class_=y) for y in spisokgg1],[])
    gg1=gg1[0].text if gg1 !=[] else "Не нашел" # заголовок
    

    spisokgg2=["js-item-price"]
    gg2 = sum([soup.find_all(class_=y) for y in spisokgg2],[])
    gg2=gg2[0].text if gg2 !=[] else "Не нашел" # цена
    

    spisokgg3=["seller-info-name js-seller-info-name","text-text-1PdBw text-size-ms-23YBR"]
    gg3 = sum([soup.find_all(class_=y) for y in spisokgg3],[])
    gg3=gg3[0].text if gg3 !=[] else "Не нашел" #Фирма
    


    spisokgg4=["item-address__string","style-item-address__string-3Ct0s"]
    gg4 = sum([soup.find_all(class_=y) for y in spisokgg4],[])
    gg4=gg4[0].text if gg4 !=[] else "Не нашел"  #Расположение
       
    spisokgg5=["title-info-metadata-item-redesign","style-item-metadata-date-1y5w6"] 
    gg5 = sum([soup.find_all(class_=y) for y in spisokgg5],[])
    gg5=gg5[0].text if gg5 !=[] else "Не нашел"  #время обьявления
    

    spisokgg6=["CardBadge-content-1A8Mf","CardBadge-description-2i7_-","CardBadge-title-3Jrch"] 
    gg6 = sum([soup.find_all(class_=y) for y in spisokgg6],[])
    gg6=gg6[0].text if gg6 !=[] else "Не нашел"  #Удостоверение
    print(gg6)
    
    spisokgg7 =["=","'",";"] # поиск в скрипте id вакансии
    gg7 = soup.find_all('script')
    gg7= sum([re.findall('avito.item.id (.*)',z.text) for z in gg7],[])[0]
    
    for i in spisokgg7 :                                               
        gg7= gg7.replace(i, '')
    #print(gg7)
    
    
    bad_chars = ['\\', ':', '!', '"',"'"]
    script = soup.find_all('script')
    
    
    seach8='totalViews' #всего просмотров 
    for i in (jsonpars(seach8,script)):
        x=i
        for l in bad_chars :
            x = x.replace(l, '')
    gg8=x
    
    seach9='todayViews' #просмотры сегодня
    for i in jsonpars(seach9,script):
        x=i
        for l in bad_chars :
            x = x.replace(l, '')
    gg9=x
    

    
    seach10='validThrough' #действительно до
    for i in jsonpars(seach10,script):
        x=i
        for l in bad_chars :
            x = x.replace(l, '')
    gg10=x

    seach11='datePosted' #публикация обьявления
    for i in jsonpars(seach11,script):
        x=i
        for l in bad_chars :
            x = x.replace(l, '')
    gg11=x

    seach12='replyTimeText' #время ответа продавца
    for i in jsonpars(seach12,script):
        x=i
        for l in bad_chars :
            x = x.replace(l, '')
    gg12=x


    seach13='min_price' #прошлая цена
    for i in jsonpars(seach13,script):
        x=i
        for l in bad_chars :
            x = x.replace(l, '')
    gg13=x
    return gg,gg1,gg2,gg3,gg4,gg5,gg6,gg7,gg8,gg9,gg10,gg11,gg12,gg13,ssilk


page=""
book = xlwt.Workbook()
sheet1 = book.add_sheet("Sheet 1", cell_overwrite_ok=True)
url = "https://www.avito.ru/novosibirsk/predlozheniya_uslug/remont_stroitelstvo-ASgBAgICAUSYC8CfAQ?cd=1&p="+page+"&q=ремонт+квартир&s=104"


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
session = requests.Session()
n=9
spisok=[]
spisok1=[]
for nm in range(1,n+1):     
      page=str(nm)
      time.sleep(times)
      r = session.get(url, headers = {
          'User-Agent': user_agent_val
      })
      #print(r)
      soup = BeautifulSoup(r.text, "lxml")

      #print(url)
      gg=soup.find_all("div",class_="iva-item-titleStep-pdebR")
      #spisok+=[gg]
      for i in gg:
          
          for a in i.find_all(href=True):
              #print(a)
              lkl=a['href']
              spisok+=[lkl]
for i in spisok:
    sslk="https://www.avito.ru/"+i
    sslk=str(sslk)
    
    spisok1+=[sslk]
    print("proshlo")
#print(spisok)
#spisok=sum(spisok,[])
print(spisok)
xx=range(1,len(spisok)+1)      
row = sheet1.row(0)
row.write(0,"заголовок")
row = sheet1.row(0)
row.write(1,"содержание")
row = sheet1.row(0)
row.write(2,"цена")
row = sheet1.row(0)
row.write(3,"фирма")
row = sheet1.row(0)
row.write(4,"расположение")
row = sheet1.row(0)
row.write(5,"время обьявления")
row = sheet1.row(0)
row.write(6,"удостоверение")
row = sheet1.row(0)
row.write(7,"id  вакансии")
row = sheet1.row(0)
row.write(8,"всего просмотров")
row = sheet1.row(0)
row.write(9,"сегодняшние просмотры")
row = sheet1.row(0)
row.write(10,"обьявление действительно до")
row = sheet1.row(0)
row.write(11,"публикация обьявления")
row = sheet1.row(0)
row.write(12,"время ответа продавца")
row = sheet1.row(0)
row.write(13,"прошлая цена")
row = sheet1.row(0)
row.write(14,"ссылка")



print(spisok)
for i, z in zip(spisok1,xx):
      time.sleep(times)
      pars=parserstr(i)
            
      
      
      row = sheet1.row(z) #слева
      row.write(0,pars[1]) #сверху загаловок

      row = sheet1.row(z) 
      row.write(1,pars[0]) #содержание
      
      row = sheet1.row(z) 
      row.write(2,pars[2]) #цена

      row = sheet1.row(z) 
      row.write(3,pars[3]) #фирма

      row = sheet1.row(z) 
      row.write(4,pars[4]) #расположение

      row = sheet1.row(z) 
      row.write(5,pars[5])# время обьявлений

      row = sheet1.row(z) 
      row.write(6,pars[6]) #удостоверение

      row = sheet1.row(z) 
      row.write(7,pars[7]) #id  вакансии

      row = sheet1.row(z) 
      row.write(8,pars[8]) #всего просмотров

      row = sheet1.row(z) 
      row.write(9,pars[9]) #сегодняшние просмотры

      row = sheet1.row(z) 
      row.write(10,pars[10]) # обьявление действительно до

      row = sheet1.row(z) 
      row.write(11,pars[11]) # публикация обьявления

      row = sheet1.row(z) 
      row.write(12,pars[12]) # время ответа продавца

      row = sheet1.row(z) 
      row.write(13,pars[13]) #прошлая цена

      row = sheet1.row(z) 
      row.write(14,pars[14]) #ссылка
      

   

      
      
            

      
   

        
book.save("test.xls")

