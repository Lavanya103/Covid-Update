from plyer import notification
import requests
from bs4 import BeautifulSoup
import time



def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\Users\Lavanya\OneDrive\Desktop",
        timeout = 10,
     )
def getData(url):
    r = requests.get(url)
    return r.text
if __name__ == '__main__':
    #while True:
        #notifyMe("Lavanya","Let's fight covid together")
        myhtmlData = getData("http://mohfw.gov.in/")
        #print(myhtmlData)
        soup = BeautifulSoup(myhtmlData, 'html.parser')
        #print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr=myDataStr[0:]
        itemlist=myDataStr.split("\n\n")
        states = ['Maharashtra','Karnataka','Assam']
        for item in itemlist[0:35]:
            datalist = item.split("\n")
            if datalist[1] in states:
                print(datalist)
                nTitle = "Cases of Covid-19"
                nText = f"State :  {datalist[1]} \nActive : {datalist[2]} \nCured : {datalist[3]} \ndeaths : {datalist[4]}"

                notifyMe(nTitle,nText)
                time.sleep(2)
        time.sleep()