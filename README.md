# python_Ulamspiral

## 概要
tkinterのwindow上にウラムの螺旋を描画するプログラムです。

<img src="https://user-images.githubusercontent.com/75155218/201231668-0997a9c3-cc6e-4213-be55-59458a216750.gif" width="500px">


## 想定環境
Ubuntu20.04  
python 3.9.0  
`pip install matplotlib`で環境を整えることができます。


## プログラム
- Ulam_spiral_maker.py 
  - tkinterのwindow上にウラムの螺旋を描画するプログラム
  - 入力ボックスに1を指定するとウラムの螺旋(素数螺旋)が表示され、2以上の整数を入力するとその整数の倍数が色図いて表示されます。
- raindrop.py
  - tkinterのwindow上で、落下してくる玉をよけるオマケゲーム
  - 十字キーで操作して、玉に当たるとゲームオーバーです。


## 使い方
以下のように実行すると、tkinterのwindowが立ち上がります。
```
python Ulam_spiral_maker.py
```
```
python raindrop.py
```

終了は、立ち上がったwindowの右上の×ボタンで終了することができます。

## おまけのraindrop.py

<img src="https://user-images.githubusercontent.com/75155218/201232103-4aac8d62-266c-4a8b-9e09-fba3015cc066.gif" width="500px">

