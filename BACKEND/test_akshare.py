import akshare as ak

# 使用 akshare 获取股票数据
stock_data_sh = ak.stock_sh_a_spot_em()
stock_data_sh=stock_data_sh.iloc[1:201]
json_data_sh = stock_data_sh.to_json(orient="records")

stock_data_sz = ak.stock_sz_a_spot_em()
stock_data_sz=stock_data_sz.iloc[1:201]
json_data_sz = stock_data_sz.to_json(orient="records")
print(json_data_sz)


#寄生陈老师嗯嗯
