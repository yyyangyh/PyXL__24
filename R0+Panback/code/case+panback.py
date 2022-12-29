import pandas as pd
case = pd.read_csv(r"C:\Users\user\Documents\Personal files\111-1\PyXL\casepermillionrate_data.csv")
panback = pd.read_csv(r"C:\Users\user\Documents\Personal files\111-1\PyXL\panback.csv")
case_dict = case.to_dict('index')  # 0: {'country_name': 'Afghanistan', 'meanR_2020': 1.106366906, 'meanR_2021': 1.004136986}
panback_dict = panback.to_dict('index')  # 0: {'Unnamed: 0': 0, 'country_name': 'Mexico', 'year': 2020, 'panback': 1.49}

panback_2020 = []
panback_2021 = []

for i in range(248):
    for j in range(358):
        if panback_dict[j]['country_name'] == case_dict[i]['Location']:
            if panback_dict[j]['year'] == 2020:
                panback_2020.append(panback_dict[j]['panback'])
            else:
                panback_2021.append(panback_dict[j]['panback'])
                break
        elif j == 357:
            panback_2020.append('NaN')
            panback_2021.append('NaN')
        else:
             continue   

case['panback_2020'] = pd.DataFrame(panback_2020)
case['panback_2021'] = pd.DataFrame(panback_2021)

case = case.dropna(axis = 0)
indexNames = case[ (case['panback_2020'] == 'NaN')].index
case.drop(indexNames , inplace=True)
case = case.reset_index(drop = True)
case.to_csv("mixed_case_data.csv")
