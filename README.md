# find-anaglam

## idea
「こんにちは」->「konnnitiha」->「a:1,b:0,c:0,,,h:1i:2,j:0,k1,,,」
のようなデータに分解し, 同一のものを見つけることでanaglamの探索が効率化出来ることの検証.

- 長い文章でも計算コストほぼ変わらないと思われる
	- 名台詞集を入力してからひたすら探索したい


## 実装
python3で実装

pykakasiを用いて漢字・かなをローマ字へ変換する

取得したデータはSQLiteなどを用いて保持することを考えている

## 実行方法
```
$ pyvenv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ python find-anaglam.py
```
