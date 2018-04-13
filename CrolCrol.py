import requests
from bs4 import BeautifulSoup

def get_Malware_Name_list(Malware_Name_list,pageNum) :
    ahnlab_URL = 'http://www.ahnlab.com/kr/site/securityinfo/asec/asecCodeList.do?'
    
    req = requests.get(ahnlab_URL+'curPage='+pageNum)
    req_HTML = req.text
    BS = BeautifulSoup(req_HTML,"html.parser")
    fProd_list = BS.select('[class~=fProd]')
    for item in fProd_list :
        item_split_list = item.string.split()
        try:
            Malware_Name_list.append(item.string.split()[0])
        except Exception as e:
            print(e)
            print("------------------------------")
            print("item is {0}".format(item.string))
            print("------------------------------")
            print("pageNum is {0}".format(pageNum))
    return len(fProd_list)

def get_Malware_Type_list(Malware_Type_list,pageNum) :
    ahnlab_URL = 'http://www.ahnlab.com/kr/site/securityinfo/asec/asecCodeList.do?'
    
    req = requests.get(ahnlab_URL+'curPage='+pageNum)
    req_HTML = req.text
    BS = BeautifulSoup(req_HTML,"html.parser")
    tbody = BS.find('tbody')
    tr_list = tbody.find_all('tr')
    for tr_item in tr_list :
        try:
            Malware_Type_list.append(tr_item.get_text().split()[2])
        except Exception as e:
            print(e)
            print("------------------------------")
            print("item is {0}".format(item.string))
            print("------------------------------")
            print("pageNum is {0}".format(pageNum))
    return len(tr_list)
            
    
def Croler() :
    Malware_Name_list  = []
    Malware_Type_list  = []
    for pageNum in range(1,3416):
        #get_Malware_Name_list(Malware_Name_list,str(pageNum))
        get_Malware_Type_list(Malware_Type_list,str(pageNum))
    print("the number of Malware_Name_list is {0}".format(str(len(Malware_Type_list))))

if __name__ == "__main__" :
    Croler()
