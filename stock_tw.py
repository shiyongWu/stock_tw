import requests
import pandas as pd

dates = [20200201, 20200101, 20191201]
stockNo = 2330

class Stock_tw():
    url_template = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}" 

    def __inti__(self,No_tw):
        self.no_tw = No_tw

    def craw_data_to_csv(self,dates):
        for date in dataes:
            self.url  = url_template.format(date,self.no_tw)
            file_name = "{}_{}.csv".format(self.no_tw,date)
        data = pd.read_html(requests.get(url).text)[0]
        data.columns = data.columns.droplevel(0)
        data.to_csv(file_name, index = False)

if '__name__' == '__main__':
    test = Stock_tw(2330)
    dates = [20200201, 20200101, 20191201]
    test.craw_data_to_csv(dates)
