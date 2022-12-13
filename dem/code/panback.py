# 將dem_data以dict的方式開啟，格式會是{index:{'country_name':'XXXXX'...}}
dem_dict = free_liber_filter.to_dict('index')

country_id = 3  # 以最小的country_id為基準
delta_dem = []
base = 0  # 該國2018的score
for i in range (716):
    # 同國家時country_id同，比較年分，若為2018(基礎年)，則將該年score設為減數，在list中添加na；否則添加(該年 score - 2018 score)
    if dem_dict[i]['country_id'] == country_id:
        if dem_dict[i]['year'] == 2018:
            base = dem_dict[i]['score']
            delta_dem.append('na')
        else:
            delta_dem.append(dem_dict[i]['score'] - base)
    # 首次出現不同國家時必為2018年，更新country_id及base
    else:
        country_id = dem_dict[i]['country_id']
        base = dem_dict[i]['score']
        delta_dem.append('na')

# 把list delta_dem加入原csv檔
free_liber_filter['panback'] = pd.DataFrame(delta_dem)

free_liber_filter.to_csv("dem_panback.csv")
