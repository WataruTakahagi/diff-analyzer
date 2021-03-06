# diff-analyzer

解析対象ファイルの指定
```
diff.center('target.tif')
```

起動
```
python main.py
```

### 次のような画像がディスプレイされます。マウスで、3点以上のリファレンスを選択してください。選択する点が多いほど近似精度と中心判別能が向上します。キーボードで0を押して選択終了を宣言してください。
![carbon-1050mm1 tif_screenshot_06 03 2021](https://user-images.githubusercontent.com/7247018/110142412-7bb9fa00-7e19-11eb-8bf9-5de67c32f156.png)

### 選択されたポイントに基づき、最小二乗法で円近似したのち中心円がプロットされます。Debye-Scherrer Ringと中心を共有する幾何学的に相似な円に対応します。次に、解析したい中心-スポット間距離をマウスで選択してください。キーボードで0を押して選択終了を宣言してください。
![LSA-carbon-1050mm1 tif_screenshot_06 03 2021](https://user-images.githubusercontent.com/7247018/110142750-d81d1980-7e19-11eb-9e88-875b68cd02e9.png)

### 中心-スポット間距離がピクセル数で表示されます。
![Result-LSA](https://user-images.githubusercontent.com/7247018/110144157-5ded9480-7e1b-11eb-9a4d-22425707aeb2.png)
