dem_dict = free_liber_filter.to_dict('index')

country_id = 3  # 以最小的country_id為基準
delta_dem = []
base = 0  # 該國2018的
for i in range (716):
    if dem_dict[i]['country_id'] == country_id:
        if dem_dict[i]['year'] == 2018:
            base = dem_dict[i]['score']
            delta_dem.append('na')
        else:
            delta_dem.append(dem_dict[i]['score'] - base)
    else:
        country_id = dem_dict[i]['country_id']
        base = dem_dict[i]['score']
        delta_dem.append('na')
delta_dem
free_liber_filter['panback'] = pd.DataFrame(delta_dem)

free_liber_filter.to_csv("dem_panback.csv")
