第2回 課題説明
===================
## 概要
- 課題は全部で課題G、Hの合計2つ(+ 前回課題の復習)です
- どの課題から着手しても構いません
- 課題が終わることにSlackで報告してください
  - EDAの課題はデータ単位で報告してください


## 課題A-F: 前回の課題の復習
- 前回の課題の復習をしてください
  - 完了してない人はやりきりましょう
  - 実装できている人も回答例や他の人の実装と見比べて適宜コードの改善をしてください
  - コードの改善を行う場合はきちんとコミットメッセージを残すこと
- リンク   
  - 課題内容: https://gist.github.com/mohira/d6eb4026aa1baf07717304edd2ec618a
  - 回答例: https://github.com/mohira/answers


## 課題G: すべてのCSVにヘッダーを追加する
- 詳細は https://github.com/mohira/csv_header_addtion で説明しています
- この課題で1つのリポジトリをつくってください


## 課題H: EDA課題
- 指定されたデータに対するEDAを行ってください
- 他のメンバーとの協力プレイは大歓迎です
- **以降の課題で1つのリポジトリ** をつくってください
  - フォルダ名やファイル名はわかりやすく工夫しましょう
  - 1つのデータにつき複数のファイルをつくっても全く問題ありません
    - むしろ、観点を絞って独立させることで見通しがよくなることもあります
- 適宜、コミットすること  
- 結果は上司に報告できるようにまとめてください(フォーマットは任せます)

### 注意: EDAは散らかりがちなので気をつけること
- 各データごとにテキストファイルやスプレッドシートを準備し、適宜調べる項目や仮説を書き出す
- 調べる項目を書き出してから初めてコードを書く
- ノートブックのコードは適宜 KernelRestart, RunAll する(上から実行するだけで正しく動作するのか？)
- ノートブックの無駄なセル(一時的な確認のためのセルなど)は削除する
- 意味のある単位でセルをまとめる(無駄にセルが分かれていないか？ 1つのセルで多くのことをやりすぎていないか？)

### EDAの観点例
- そもそも論
  - どういう目的で集められたデータか？
  - データ分析の目的は何か？ (何を予測したいのか？)
- 全体感
  - データ数はどれだけか？
  - 変数の数はどれだけか？
  - 欠損はあるのか？ あったらどうするべきなのか？
- 単一の変数について
  - 各変数の正しい意味は何か？
    - 連続量か？ 離散量か？
    - 単位は？
  - 異常な値はないか？
  - 基本統計量はどれだけか？
  - 分布を可視化するとどうか？
- 変数の同士の関係性について
  - 散布図を描いてみるとどうか？
  - 層別に分析するとどうか？
  - 変数どうしには何らかの関係性があるか？
  - ピアソンの相関はどれだけか？
  - 目的変数との関係性はどうか？
- その他
  - 仮説を日本語でまとめる


### sklearn付属データセットのEDA
- 下記のsklearn付属データセットに対してEDAを行ってください

#### 対象データセット
1. [sklearn.datasets.load_boston](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_boston)
2. [sklearn.datasets.load_wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine)
3. [sklearn.datasets.load_breast_cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer)
4. [sklearn.datasets.load_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes)

### Kaggleのデータセット
- Titanic と MNIST のEDAをしてください
- ヒント: 他のKagglerが公開しているNotebook(旧称: Kernel)を参考にしてみましょう
  - 「Most Votes」でソートするとよいです(Notebookは玉石混交)
  - EDAをするときは、「EDA」「Visualization」「Starter」などと検索すると便利です
- ヒント: 英語を読むのがしんどい人は下記のChrome拡張をいれると最高にはかどります
  - [英語の文章を選択するだけで和訳を表示させる方法](https://little-hands.hatenablog.com/entry/2017/11/03/google-translator)

#### Titanic
- [Titanic: Machine Learning from Disaster | Kaggle](https://www.kaggle.com/c/titanic)
- 公開されているNotebook → https://www.kaggle.com/c/titanic/notebooks


#### MNIST(Digit Recognizer)
- [Digit Recognizer | Kaggle](https://www.kaggle.com/c/digit-recognizer)
- 公開されているNotebook → https://www.kaggle.com/c/digit-recognizer/notebooks



以上
