import pandas as pd
R0 = pd.read_csv(r"C:\Users\user\Documents\Personal files\111-1\PyXL\R0csv.csv")
panback = pd.read_csv(r"C:\Users\user\Documents\Personal files\111-1\PyXL\panback.csv")

# datframe轉dict
R0_dict = R0.to_dict('index')  # 0: {'country_name': 'Afghanistan', 'meanR_2020': 1.106366906, 'meanR_2021': 1.004136986}
panback_dict = panback.to_dict('index')  # 0: {'Unnamed: 0': 0, 'country_name': 'Mexico', 'year': 2020, 'panback': 1.49}

panback_2020 = []
panback_2021 = []
for i in range(249):
    for j in range(358):
        # 當panback和R0的country_name相同時，判斷年份並放入list中，並break for j迴圈
        if panback_dict[j]['country_name'] == R0_dict[i]['country_name']:
            if panback_dict[j]['year'] == 2020:
                panback_2020.append(panback_dict[j]['panback'])
            else:
                panback_2021.append(panback_dict[j]['panback'])
                break
        # 若判斷到panback最後一個國家還是沒對應的，list中填入NaN
        elif j == 357:
            panback_2020.append('NaN')
            panback_2021.append('NaN')
        else:
             continue   

# 以R0.csv為基礎，增加兩個list進入
R0['panback_2020'] = pd.DataFrame(panback_2020)
R0['panback_2021'] = pd.DataFrame(panback_2021)
# 刪除存在空資料的列
R0 = R0.dropna(axis = 0)
# 刪除存在NaN的列
indexNames = R0[ (R0['panback_2020'] == 'NaN')].index
R0.drop(indexNames , inplace=True)
# 重新排列index值
R0 = R0.reset_index(drop = True)
R0.to_csv("mixed_data.csv")
