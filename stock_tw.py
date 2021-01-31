import requests
import pandas as pd

class STOCK_TW():
    def __init__(self,No_tw):
        self.no_tw = No_tw
    
    def craw_data_to_csv(self,dates):
        for date in dates:
            self.url  = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}".format(date,self.no_tw)
            file_name = "./CSV/{}_{}.csv".format(self.no_tw,date)
            data = pd.read_html(requests.get(self.url).text)[0] #### A list of DataFrames
            data.columns = data.columns.droplevel(0) ## remove column[0]
            data.to_csv(file_name, index = False,encoding = "utf-8-sig")

if __name__ == '__main__':
    tsmc = STOCK_TW(2330)
    date = [20200101]
    tsmc.craw_data_to_csv(date)

