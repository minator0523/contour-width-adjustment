# 天気図の等圧線を4hPaごとに細線，20hPaごとに太線で描く（Python使用）
## 概要
普段目にする天気図は4hPaごとに細線，20hPaごとに太線で描かれることが一般的です．
しかし，ネットや書籍は線の太さを描き分ける方法を紹介していません．
リンク先のブログは[線の太さを描き分ける方法](https://note.com/fair_dunlin665/n/n1b3d6bcb3eb8)
を紹介しています．
気になる方は是非参考にしてください．

## 完成天気図
![完成天気図](contour-width-adjust_slp.png)

## データの出典
京都大学生存圏研究所の生存圏データベースのNCEP/NCAR再解析データを使用しました．

## ディレクトリ構成
```
.
├── DL_NCEP2.sh # 再解析をダウンロードするシェルスクリプト
├── README.md
├── contour-width-adjust.py　# 作図用Pythonスクリプト
└── contour-width-adjust_slp.png # 作成した天気図
```
