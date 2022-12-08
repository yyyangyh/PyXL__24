import pandas as pd

dem = pd.read_csv(r"C:\Users\user\Documents\Personal files\111-1\PyXL\V-Dem-CY-Core-v12.csv")

# 挑選3.8.3要的所有數據，並留下年份2018~2021
free_liber = dem[['country_name', 'country_id', 'year', 'v2cldiscm', 'v2cldiscw', 'v2clacfree',
                 'v2clrelig', 'v2clfmove', 'v2cldmovem', 'v2cldmovew']]
free_liber_filter = free_liber[dem['year'] >= 2018]

# 新增欄位計算各國各年3.8.3的總分
free_liber_filter['score'] = free_liber_filter[['v2cldiscm', 'v2cldiscw','v2clacfree','v2clrelig',
                                             'v2clfmove', 'v2cldmovem', 'v2cldmovew']].sum(1)
# 移除原先csv檔的index
free_liber_filter = free_liber_filter.reset_index(drop = True)

free_liber_filter.to_csv("dem_data.csv")
