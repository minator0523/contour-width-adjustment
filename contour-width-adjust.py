''' 線の太さを自動調整して作図するプログラム '''

# 必要なライブライブをロード
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
import matplotlib # wsl2上で実行する場合のおまじない
matplotlib.use('Agg') # wsl2上で実行する場合のおまじない

def contour_lines(data, interval, linewidth_thin, linewidth_thick):
    min_value = np.floor(np.min(data)/interval)
    max_value = np.ceil(np.max(data)/interval)
    lines_value = np.arange(np.floor(min_value), np.ceil(max_value), 1.0)*interval

    head5 = lines_value[:5]
    result = head5%(5*interval) == 0.0
    linewidths = [ linewidth_thick if value else linewidth_thin  for value in result ]
    index_label = np.where(result)[0][0]
    return lines_value, linewidths, index_label

# 日時を指定
yyyy = 2024 # 年
mm = 12 # 月
dd = 21 # 日
hh = 18 # 時
lat_center = 35.0 # 中心緯度
lon_center = 135.0 # 中心経度

## GSMデータ（gribをNetCDFに変換したもの）を読み込む
ifile = f'./data/GSM_jp-surf_{yyyy:04d}{mm:02d}{dd:02d}.nc'
ds_surf = xr.open_dataset(ifile)
print(f"ifile: {ifile}")
slp = ds_surf['slp'].sel(time=f"{yyyy:04d}-{mm:02d}-{dd:02d}T{hh:02d}:00").values # 海面校正気圧
lats = ds_surf['latitude'].values # 緯度
lons = ds_surf['longitude'].values # 経度

# 作図に必要な配列を用意
lines_value, linewidths, index_label = contour_lines(slp, 4.0, 1.5, 3.0)

## 作図
x, y = np.meshgrid(lons, lats)
fig, ax = plt.subplots(
    1, 1, subplot_kw={'projection': ccrs.Stereographic(central_latitude=lat_center, central_longitude=lon_center)}, tight_layout=True, figsize=(8,8)
)
ax.text(0.0, 1.05, f'SLP, {yyyy:04d}/{mm:02d}/{dd:02d} {hh:02d}:00UTC ANL', transform=ax.transAxes, size=25, weight='bold') # タイトル
# 地図を作成
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, linestyle=':', color='k', alpha=0.8) # 経度・緯度線を描写:
gl.xlocator = mticker.FixedLocator(np.arange(120.0, 150.0, 10.0)) # 経度線の間隔を設定
gl.ylocator = mticker.FixedLocator(np.arange(20.0, 50.0, 10.0)) # 緯度線の間隔設定
ax.coastlines(color='black', linestyle='-', linewidth=0.75) # 海岸線を描画
ax.set_extent([120.0, 150.0, 20.0, 50.0], ccrs.PlateCarree()) # 作図範囲の設定

# 等値線を描画
cs = ax.contour(x, y, slp, transform=ccrs.PlateCarree(), colors="green", levels=lines_value, linewidths=linewidths)
cs.clabel(cs.levels[index_label::5], fmt="%.0f", fontsize=20, manual=False, inline=False)

ofile = f"contour-width-adjust_slp.png"
print(f"ofile: {ofile}")
plt.savefig(ofile)
