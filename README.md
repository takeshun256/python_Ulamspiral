# python_Ulamspiral

## 概要
tkinterのwindow上にウラムの螺旋を描画するプログラムです。

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

