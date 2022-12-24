#資料有先經過Excel 樞紐前處理，之後用pandas復刻
import pandas as pd
case = pd.read_csv(r"casepermillion_pivot.csv")
case = case.fillna(0)

#計算每年[每月case新增速率]的平均
case_2020 = case[["2020_1", "2020_2", "2020_3", "2020_4", "2020_5", "2020_6", "2020_7", "2020_8", "2020_9", "2020_10", "2020_11", "2020_12"]]
case["2020_rate"] = case_2020.mean(axis = 1)

case_2021 = case[["2021_1", "2021_2", "2021_3", "2021_4", "2021_5", "2021_6", "2021_7", "2021_8", "2021_9", "2021_10", "2021_11", "2021_12"]]
case["2021_rate"] = case_2021.mean(axis = 1)

case_2022 = case[["2022_1", "2022_2", "2022_3", "2022_4", "2022_5", "2022_6", "2022_7", "2022_8", "2022_9", "2022_10", "2022_11", "2022_12"]]
case["2022_rate"] = case_2022.mean(axis = 1)
case

#提取2020, 2021, 2022三筆數據
case_rate = case.drop(labels=["2020_1", "2020_2", "2020_3", "2020_4", "2020_5", "2020_6", "2020_7", "2020_8", "2020_9", "2020_10", "2020_11", "2020_12", "2021_1", "2021_2", "2021_3", "2021_4", "2021_5", "2021_6", "2021_7", "2021_8", "2021_9", "2021_10", "2021_11", "2021_12", "2022_1", "2022_2", "2022_3", "2022_4", "2022_5", "2022_6", "2022_7", "2022_8", "2022_9", "2022_10", "2022_11", "2022_12"], axis = 1)
case_rate

#輸出csv
case_rate.to_csv("casepermillionrate_data.csv")
