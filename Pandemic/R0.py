import pandas as pd
import numpy as np

#此份csv已刪除其他欄位僅保留每日R0數值
R0 = pd.read_csv(r"pandemic_reproduction rate.csv")

R0_df = pd.DataFrame(R0)

R0_df['R_2020'] = ["" for i in range(241511)]
R0_df['R_2021'] = ["" for i in range(241511)]
R0_df['R_2022'] = ["" for i in range(241511)]

R0_val = R0.values

for col in R0_val:
    if col[1][:4] == '2020':
        col[3] = col[2]
    elif col[1][:4] == '2021':
        col[4] = col[2]
    elif col[1][:4] == '2022':
        col[5] = col[2]

R0_new = pd.DataFrame(R0_val)
R0_new.set_axis(['Location', 'Date', 'Reproduction Rate', 'R_2020', 'R_2021', 'R_2022'], axis='columns', inplace=True)
R0_new.to_csv("R0_new.csv")


