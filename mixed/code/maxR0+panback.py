import pandas as pd
R0_max = pd.read_csv(r"C:\Users\user\Documents\Personal files\111-1\PyXL\R0_max.csv")
panback = pd.read_csv(r"C:\Users\user\Documents\Personal files\111-1\PyXL\panback.csv")
R0_dict = R0_max.to_dict('index')  # 0: {'country_name': 'Afghanistan', 'meanR_2020': 1.106366906, 'meanR_2021': 1.004136986}
panback_dict = panback.to_dict('index')  # 0: {'Unnamed: 0': 0, 'country_name': 'Mexico', 'year': 2020, 'panback': 1.49}

panback_2020 = []
panback_2021 = []

for i in range(249):
    for j in range(358):
        if panback_dict[j]['country_name'] == R0_dict[i]['country_name']:
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

R0_max['panback_2020'] = pd.DataFrame(panback_2020)
R0_max['panback_2021'] = pd.DataFrame(panback_2021)

R0 = R0_max.dropna(axis = 0)
indexNames = R0[ (R0['panback_2020'] == 'NaN')].index
R0.drop(indexNames , inplace=True)
R0 = R0.reset_index(drop = True)
R0
R0.to_csv("mixed_maxR0_data.csv")
