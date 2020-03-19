第1回 課題説明
===================

## 課題は合計6つ
- 課題A から 課題F までの合計6つです
- それぞれの課題には小問(A-1やA-2など)があります
- アルファベットに特に意味はありません
- 課題文の不備に気づいた場合や、課題に対する質問があるときは随時Slackでお願いします

## 課題の難易度
ざっくりですがこのような関係です。
純粋な実装の難しさだけでなく、必要な知識の多さが難易度に影響しています。

(易) B < A < C < E < F < D (難)

## 1つの課題につき1つのリポジトリ
- 課題ごとにリポジトリを作成すること
    - ex: `kadai-A` や `kadai-F` など
- 各リポジトリ内のファイルやフォルダの構成は読み手にとってわかりやすいものにすること


## コミットは小問ごと
- コミットは少なくとも小問ごとに行うこと
    - 1つの小問の中で複数のコミットがあるのはOKです
    - コミットするかを迷った場合はコミットしてOKです
- コミットメッセージも分かりやすくすること
- 3行名以降には躓いたところや気づいたことを書いてもらえるとフィードバックしやすいです

以下、コミットメッセージの例です。

```text
[課題A-1] 日本の九九表を実装
```


```text
[課題C-4] NGワードを複数実装

- このサイト(URL)を参考に実装
- 動いてはいるがもっとキレイに書く方法を知りたい
```


## 1つの課題が終わるたびにSlackで報告をする
- 1つの課題が終わったら、その段階でSlackに報告してください
- 報告するときには、次の内容を入れてください
    1. pushを完了した状態でのリポジトリURL
    2. どれくらいの時間がかかったか
    3. 3行程度の感想

```text
課題A終了しました。

http://github.com/mohira/kadai-A

・所要時間: 約45分
・感想:
    ・思ったより時間が掛かったけど、おおよそできた！
    ・A-3での文字列のフォーマットに少し苦労した
    ・統計量計算の関数実装は楽勝だった
```

## 実装に詰まったら
- 独力で解決がむずかしそうだと思ったら仲間と一緒に考えてみてください
- このとき、どういうところで詰まったのか、何がわからないのかを言語化してみてください


## 課題をすべてクリアしたら
まずは、おめでとうございます。素晴らしいですね。

課題が終わったら他のメンバーのサポートをしてみてください。一緒に考えたり、教えると相当に実力がつきます。
あるいは、さらなる応用課題が欲しい場合はその旨を教えて下さい。




課題: Python基本総ざらい
=======================

Pythonの基礎的な文法を抑えるための課題です。

## 課題A-1: 日本の九九表
### 要件
下記のような出力が得られる `kuku_1.py` を実装してください

```
$ python kuku_1.py
1 2 3 4 5 6 7 8 9
2 4 6 8 10 12 14 16 18
3 6 9 12 15 18 21 24 27
4 8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54
7 14 21 28 35 42 49 56 63
8 16 24 32 40 48 56 64 72
9 18 27 36 45 54 63 72 81
```

## 課題A-2: 九九表の拡張
### 要件
- 下記のような出力が得られる `kuku_2.py` を実装してください
    - 任意の行数および任意の列数での掛け算の結果が得られます

#### 出力例1
```bash
$ python kuku_2.py
行数を入力してください: 4
列数を入力してください: 6
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
```

#### 出力例2
```bash
$ python kuku_2.py
行数を入力してください: 12
列数を入力してください: 12
1 2 3 4 5 6 7 8 9 10 11 12
2 4 6 8 10 12 14 16 18 20 22 24
3 6 9 12 15 18 21 24 27 30 33 36
4 8 12 16 20 24 28 32 36 40 44 48
5 10 15 20 25 30 35 40 45 50 55 60
6 12 18 24 30 36 42 48 54 60 66 72
7 14 21 28 35 42 49 56 63 70 77 84
8 16 24 32 40 48 56 64 72 80 88 96
9 18 27 36 45 54 63 72 81 90 99 108
10 20 30 40 50 60 70 80 90 100 110 120
11 22 33 44 55 66 77 88 99 110 121 132
12 24 36 48 60 72 84 96 108 120 132 144
```



## 課題A-3: きれいな九九表
### 要件
- 下記のような出力が得られる `beautiful_kuku.py` を実装してください
- きれいに整っているので見やすくなっています
    - 式が表示されている
    - 結果の桁数が違う場合は適切な量の半角スペースを挿入しているので、みやすい
    - ※結果が3桁の場合は崩れてもOKです    


### 出力例
```bash
行数を入力してください: 9
列数を入力してください: 9
1 x 1 =  1 | 2 x 1 =  2 | 3 x 1 =  3 | 4 x 1 =  4 | 5 x 1 =  5 | 6 x 1 =  6 | 7 x 1 =  7 | 8 x 1 =  8 | 9 x 1 =  9 |
1 x 2 =  2 | 2 x 2 =  4 | 3 x 2 =  6 | 4 x 2 =  8 | 5 x 2 = 10 | 6 x 2 = 12 | 7 x 2 = 14 | 8 x 2 = 16 | 9 x 2 = 18 |
1 x 3 =  3 | 2 x 3 =  6 | 3 x 3 =  9 | 4 x 3 = 12 | 5 x 3 = 15 | 6 x 3 = 18 | 7 x 3 = 21 | 8 x 3 = 24 | 9 x 3 = 27 |
1 x 4 =  4 | 2 x 4 =  8 | 3 x 4 = 12 | 4 x 4 = 16 | 5 x 4 = 20 | 6 x 4 = 24 | 7 x 4 = 28 | 8 x 4 = 32 | 9 x 4 = 36 |
1 x 5 =  5 | 2 x 5 = 10 | 3 x 5 = 15 | 4 x 5 = 20 | 5 x 5 = 25 | 6 x 5 = 30 | 7 x 5 = 35 | 8 x 5 = 40 | 9 x 5 = 45 |
1 x 6 =  6 | 2 x 6 = 12 | 3 x 6 = 18 | 4 x 6 = 24 | 5 x 6 = 30 | 6 x 6 = 36 | 7 x 6 = 42 | 8 x 6 = 48 | 9 x 6 = 54 |
1 x 7 =  7 | 2 x 7 = 14 | 3 x 7 = 21 | 4 x 7 = 28 | 5 x 7 = 35 | 6 x 7 = 42 | 7 x 7 = 49 | 8 x 7 = 56 | 9 x 7 = 63 |
1 x 8 =  8 | 2 x 8 = 16 | 3 x 8 = 24 | 4 x 8 = 32 | 5 x 8 = 40 | 6 x 8 = 48 | 7 x 8 = 56 | 8 x 8 = 64 | 9 x 8 = 72 |
1 x 9 =  9 | 2 x 9 = 18 | 3 x 9 = 27 | 4 x 9 = 36 | 5 x 9 = 45 | 6 x 9 = 54 | 7 x 9 = 63 | 8 x 9 = 72 | 9 x 9 = 81 |
```

## 課題A-4: 天気情報の分析
### 要件
- 3都府県のいくつかの駅名とある日の最高気温のデータを辞書として持っています
- このデータを使って3つの問を満たす実装をしてください

```python
def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)


if __name__ == '__main__':
    main()

```

## 課題A-5:基本統計量の計算
- スペース区切りで入力された整数群において、以下の4つの統計量を計算アプリを実装してください
    1. 合計値
    2. 最大値
    3. 最小値
    4. 平均値
- ただし、**組み込み関数やライブラリは使わないこと**(`sum()`や`np.mean()`など)
- 1つの統計量につき、それ専用の関数を実装すること

### 実行例
```bash
データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6
```

## 課題A-6: N面サイコロの反復試行
- N面サイコロをM回振ったときの結果を表示してください
    - N, M は正の整数とします
    - N, M はユーザーからの入力を利用すること

### 実行例
```bash
サイコロの面の数は?: 8
何回振りますか?: 20
[6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]
```


課題B: オブジェクト指向プログラミング 初級
=====================================

オブジェクト指向プログラミングの初級課題です。
オブジェクト指向プログラミングを使った良いコードの書き方というよりも、正しい文法で記述できるかを目的としています。

## 課題B-1: 円オブジェクト
- 次のコードが正しく動作するような `Circle` クラスを実装してください
- `area` は面積、 `perimeter` は周囲長(=円周の長さ) という意味です。

```python
# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 1 8.85
```

## 課題B-2: 長方形オブジェクト
- 次のコードが正しく動作するような `Rectangle` クラスを実装してください
- `diagonal` は 対角線(の長さ) という意味です。

```python
rectangle1 = Rectangle(height=5, width=6)
rectangle1.area()  # 30.00
rectangle1.diagonal()  # 7.81

rectangle2 = Rectangle(height=3, width=3)
rectangle2.area()  # 9.00
rectangle2.diagonal()  # 4.24
```

## 課題B-3: カウンターその1
- 次のコードが正しく動作するような `MyCounterV1` クラスを実装してください

```python
counter1 = MyCounterV1(value=0)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

counter2 = MyCounterV1(value=7)
print(counter2.value)  # 7

counter2.count_up()
print(counter2.value)  # 8

counter2.count_up()
print(counter2.value)  # 9

```

## 課題B-4: カウンターその2
- 次のコードが正しく動作するような `MyCounterV2` クラスを実装してください

```python

counter1 = MyCounterV2(value=0, step=1)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

counter2 = MyCounterV2(value=0, step=3)
print(counter2.value)  # 0

counter2.count_up()
print(counter2.value)  # 3

counter2.count_up()
print(counter2.value)  # 6
```

## 課題B-5: カウンターその3
- 次のコードが正しく動作するような `MyCounterV3` クラスを実装してください


```python
counter1 = MyCounterV3(value=1, step=2)
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 3

counter1.count_up()
print(counter1.value)  # 5

counter1.count_down()
print(counter1.value)  # 3

counter2 = MyCounterV3(value=3, step=4)
print(counter2.value)  # 3

counter2.count_down()
print(counter2.value)  # -1

counter2.count_down()
print(counter2.value)  # -5
```


課題C: オブジェクト指向プログラミング 基本
==========================================

オブジェクト指向プログラミングの基本的な課題です。
これが独力で実装できればPythonにおけるオブジェクト指向プログラミングの最低限は抑えたといってもよいでしょう。


## 課題C: ワードフィルタ
- ワードフィルタとは、メッセージ内に特定のワードが含まれる場合にそのワードを別のものに置き換えるツールです。
- 例えば、ドラマや映画、スポーツの試合結果のネタバレを防ぐときなどの利用が考えられます。
- 参考: https://www.slideshare.net/t_wada/tddbc-exercise

### 例: "アーセナル"(サッカーチームの名前)フィルタ
- フィルタ前: `昨日のアーセナルの試合アツかった！`
- フィルタ後: `昨日の<censored>の試合アツかった！`


### C-1: NGワードが含まれているかどうかを判定できる
- NGワードが含まれているかどうかを判定できる `detect()` メソッドを持つ `WordFilter`クラス を実装してください
- 下記のコードが動作すればOKです

```python
my_filter = WordFilter("アーセナル")

# NGワードが含まれている場合
my_filter.detect("昨日のアーセナルの試合アツかった！") # Trueを返す ※出力されるわけではありません！

# NGワードが含まれていない場合
my_filter.detect("昨日のリバプールの試合アツかった！") # Falseを返す ※出力されるわけではありません！
```

### C-2: NGワードを変換できる
- NGワードが含まれていた場合に、NGワードを `<censored>` という文字に変換できる `censor` メソッドを実装してください
- 下記のコードが動作すればOKです

```python
my_filter = WordFilter("アーセナル")

# NGワードが含まれている場合
my_filter.censor("昨日のアーセナルの試合アツかった！") # "昨日の<censored>の試合アツかった！" を返す ※出力されるわけではありません！

# NGワードが含まれていない場合
my_filter.censor("昨日のリバプールの試合アツかった！") # "昨日のリバプールの試合アツかった！" を返す ※出力されるわけではありません！

```

以降は`WordFilter`クラスの実装だけではなく、仕様の理解やどういうふうにクラスを利用するかも含めて考えてください。

### C-3: `<censored>` を自由に変更できるようにする
- NGワードが含まれていた場合に置き換える文字列を自由に設定できるようにしてください

### C-4: NGワードの複数登録
-  NGワードを複数登録できるようにしてください

### C-5: NGワードの変更
- NGワードを後から変更できるようにしてください


課題D: オブジェクト指向プログラミング 応用
==========================================

やや発展させた課題です。Pythonの[データモデル](https://docs.python.org/ja/3/reference/datamodel.html)を理解しているかどうかポイントです。

講義で触れていない内容も多いので、ちょっとむずかしいです。がんばってください。

## 課題D: セマンティックバージョニング
> 「[セマンティック バージョニング](https://semver.org/lang/ja/)」(以下 semver )は、ソフトウェアにバージョン番号を付ける際の規則です。
>
> semver では、バージョン番号は主に三つのフィールドに分かれ、それぞれ major, minor, patch と名付けられています。 (主にというのは、実は semver には仕様上はさらなる追加フィールドがあるのですが、今回の演習では扱いません)
>
> 例: バージョン 1.4.2 の場合、 major は 1, minor は 4 となります
>
> 参考: [お題: セマンティック・バージョニング](https://gist.github.com/twada/760b1fe7f04eb03ee9799d75ecd28cd8)


## 課題D-1: 等価性の比較
- ヒント: https://docs.python.org/ja/3/reference/datamodel.html#object.__eq__

```python
# Python3.7.0 というバージョンを表現したもの
py370 = SemanticVersion(major=3, minor=7, patch=0)

# 等価である場合
print(SemanticVersion(3, 7, 0) == py370)  # True

# 等価でない場合
print(SemanticVersion(3, 7, 1) == py370)  # False
```

## 課題D-2: 文字列表現を得られる
- ヒント: https://docs.python.org/ja/3/reference/datamodel.html#object.__str__

```python
# Python3.7.0 というバージョンを表現したもの
py370 = SemanticVersion(major=3, minor=7, patch=0)

print('3.7.0' == str(py370))  # True
```

## 課題D-3: パッチバージョンアップができる
- パッチバージョンをアップデートする例
    - 3.7.0 -> 3.7.1
    - 2.1.2 -> 2.1.3
- ヒント: `patch_version_up()` は `SemanticVersion` を返しています(内部の値を更新しているわけではない！)

```python
# Python3.7.0 というバージョンを表現したもの
py370 = SemanticVersion(major=3, minor=7, patch=0)

py371 = py370.patch_version_up()
print(SemanticVersion(3, 7, 1) == py371)  # True
```

## 課題D-4: マイナーバージョンアップができる
- マイナーバージョンをアップデートする例
    - 3.7.0 -> 3.8.0
    - 2.1.2 -> 2.2.0

```python
# Python3.7.0 というバージョンを表現したもの
py370 = SemanticVersion(major=3, minor=7, patch=0)

py380 = py370.minor_version_up()
print(SemanticVersion(3, 8, 0) == py380)  # True
```


## 課題D-5: メジャーバージョンアップができる
- メジャーバージョンをアップデートする例
    - 3.7.0 -> 4.0.0
    - 2.1.2 -> 3.0.0

```python
# Python3.7.0 というバージョンを表現したもの
py370 = SemanticVersion(major=3, minor=7, patch=0)

py400 = py370.major_version_up()
print(SemanticVersion(4, 0, 0) == py400)  # True
```


課題E: WebAPIの利用 HackersNews
=====================

WebAPIを使った課題です。
どの情報をどのAPIを利用して取得するかを考えるところがポイントです。

## 要件
[Hacker News](https://news.ycombinator.com/)という計算機科学やベンチャーなどのテーマを取り扱うソーシャルニュースサイトがあります。

[HackerNews/API: Documentation and Samples for the Official HN API](https://github.com/HackerNews/API) を利用して、トップページに表示されているニュースのタイトルおよびリンクURLを取得してください()。

### 具体例
ある時刻でのトップページはこのようになっています。

![image.png (315.1 kB)](https://img.esa.io/uploads/production/attachments/6586/2019/09/24/21054/d67367de-804b-4fca-9ba7-5f0e4f5e798a.png)


この状況において、次のような出力が得られたらOKです。

```bash
{'title': 'Facebook to acquire CTRL-Labs, a startup for controlling computers with the mind', 'link': 'https://www.bloomberg.com/news/articles/2019-09-23/facebook-to-buy-startup-for-controlling-computers-with-your-mind'}
{'title': 'The news industry was complicit in the opioid crisis', 'link': 'https://www.cjr.org/opinion/opioids-news-prescription-doctor.php'}
{'title': 'Adblock Radio', 'link': 'https://github.com/adblockradio/adblockradio'}
{'title': 'Voidcall – Making of 13kb JavaScript RTS Game', 'link': 'https://phoboslab.org/log/2019/09/voidcall-making-of'}
{'title': 'Yahoo Customer Data Security Breach Litigation Settlement', 'link': 'https://yahoodatabreachsettlement.com/'}
```

### 注意事項
APIで連続的にアクセスする場合は、少なくとも1秒の間隔を空けること！
連続的にアクセスすると相手のサーバーに負荷をかけるばかりか、悪質な場合は通報されてしまいます。

処理を N秒 止める場合は、`time`モジュールで実現できます。
実際に試してみてください。

```python
import time


for i in range(10):
    time.sleep(1) # ここで1秒止まる
    print(i)
```


課題F: Webアプリ 簡易掲示板
=================

Webアプリの基本的な課題です。HTTPの基本やFlaskでの書き方、ファイル入出力の知識も問われます。


## 要件
- 簡易掲示板をつくる
- 動作イメージ → https://simple-bbs.herokuapp.com
    - 実際に投稿して動きを確かめてください


## 課題F-1: 要件の書き出し
- https://simple-bbs.herokuapp.com でいくつか投稿を試し、どういう要件を備えたアプリなのかを書き出してください

## 課題F-2: 実装
- 課題F-1で書き出した要件に従って実装してください

## 課題F-3: 改善
- 自由課題です
- より使い勝手のよい掲示板になるような改善をしてください
    - 例: 機能の追加, 見た目の変更 など




以上
