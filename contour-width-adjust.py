## 線の太さを自動調整するスクリプト

# 必要なライブライブをロード
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

# 日時を指定
yyyy = 2025 # 年
mm = 3 # 月
dd = 4 # 日
hh = 18 # 時

# GSMデータ（gribをNetCDFに変換したもの）を読み込む
ds_surf = xr.open_dataset(f'./data/GSM_jp-surf_{yyyy:04d}{mm:02d}{dd:02d}.nc')
slp = ds_surf['slp'].sel(time=f"{yyyy:04d}-{mm:02d}-{dd:02d}T{hh:02d}:00").values # 海面校正気圧
lats = ds_surf['latitude'].values # 緯度
lons = ds_surf['longitude'].values # 経度

# 作図