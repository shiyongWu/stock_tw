from stock_tw import STOCK_TW

print("test example!")

tsmc  = STOCK_TW(2330)
dates = [20201201,20201101] 
tsmc.craw_data_to_csv(dates)

