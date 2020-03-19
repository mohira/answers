第3回 課題説明
===================

## 概要
- どの課題から着手しても構いません
- 課題が終わることにSlackで報告してください
- ペアプロ歓迎です
- リポジトリやコミットの管理は工夫しましょう
- 講義ではまだ扱っていない内容も登場します
    - 詰まった場合はまわりと協力してみてください
    - 無理に理解し切ろうとしなくてもOK(分からない箇所を明らかできればOK!)
    - 分からない部分は、どこがどう分からないのかを言語化しておきましょう

## 課題A-H: 前回の課題の復習
- 前回までの課題の復習をしてください
  - 完了してない人はやりきりましょう
  - 実装できている人も回答例や他の人の実装と見比べて適宜コードの改善をしてください
  - コードの改善を行う場合はきちんとコミットメッセージを残すこと
- リンク   
  - 課題A-F: https://gist.github.com/mohira/d6eb4026aa1baf07717304edd2ec618a
  - 課題G-H: https://gist.github.com/mohira/d6eb4026aa1baf07717304edd2ec618a#file-06_homework_readme_part2-md

## 課題I: 評価指標の理解と実装
いくつかの評価指標について次の4つを行ってください。
(評価指標は後述)

1. 評価指標の導出方法を理解する
2. 評価指標の特性や、どういうときに使うべき(使わないべき)なのかを調べる
3. 簡単なデータを用意して手計算で計算を行う(丸暗記は不要)
4. sklearnを利用して計算するコードを実装する
    - 回帰問題であれば boston などを使いましょう
    - 2クラス分類であれば breast_cancer などを使いましょう

### 回帰問題での評価指標
1. RMSE(Root Mean Squared Error)
2. MAE(Mean Absolute Error)
3. 決定係数(R2 Score)

### 2クラス分類での評価指標
1. 混同行列(Confusion Matrix)
    - 厳密には評価指標ではないですが重要なので調べておいてください
    - 混同行列に登場する要素(TP,FP,TF,TN)を説明できるようにしましょう
2. 正答率(Accuracy)
3. 適合率(Precision)
4. 再現率(Recall) 
5. 交差エントロピー誤差(Cross Entropy Loss; LogLoss)


## 課題J: 評価プロトコルの理解と実装
### 課題J-1: 交差検証
- 交差検証とは何かを説明できるようにしてください
    - 交差検証のアルゴリズムはどうなっているか？
    - ホールドアウトとの違いは何か？
    - メリットやデメリットはあるのか？
    - などなど
- 実際のデータに対して交差検証を行ってください
    - 実装には [sklearn.model_selection.KFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold) を使うと便利です
   

### 課題J-2: 交差検証のバリエーション(StratifiedKFold)
- 交差検証のバリエーションである StratifiedKFold とは何かを説明できるようにしてください
- 実際のデータに対してStratifiedKFoldを行ってください
    - [sklearn.model_selection.StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold) を使いましょう



### 課題J-3: 交差検証のバリエーション(GroupKFold)
- 交差検証のバリエーションである GroupKFold とは何かを説明できるようにしてください
- 実際のデータに対してStratifiedKFoldを行ってください
    - [sklearn.model_selection.GroupKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold) を使いましょう


## 課題K: 一番の流れの実装になれよう
- sklearn付属データセットに対して、機械学習の一連の流れを実装しましょう
- ざっくりですが、流れとは例えば下記の感じです
    - 目的の確認(何を予測すればよいのか？)
    - EDA(簡易的なものでOKです)
    - 評価指標は何か？
    - 評価プロトコルは何か？(ホールドアウトや交差検証など。いろいろ試してみてください)
    - 機械学習モデルの訓練
    - 機械学習モデルの改善とモデルの選択
        - 特徴量エンジニアリング
            - 新たな説明変数を追加する(ex: 身長と体重からBMIという説明変数をつくるなど)
            - 説明変数を加工する(ex: 標準化など)
            - 説明変数を選ぶ
            - など
        - ハイパーパラメータのチューニング
    - テストデータでの評価

### 対象データセット
- [sklearn.datasets.load_boston](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_boston)
- [sklearn.datasets.load_wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine)
- [sklearn.datasets.load_breast_cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer)
- [sklearn.datasets.load_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes)


## 課題L: Titanic
Titanicのコンペに挑戦してみましょう！

### 課題L-1: 初のSubmission
- 自分でモデルを訓練し、Submissionを完了してください
- 利用するモデルは自由です
    - 講義で扱ったロジスティック回帰以外でも問題ないです
- この段階ではPublicScoreは気にしなくてOKです
    - Kaggleのルールに従ってデータ処理や最低限を実装ができるかがポイントです    

### 課題L-2: `gender_submission` 超え！
- `gender_submission` のスコアである 0.76555 を超えるモデルを目指しましょう
- 講義で扱っていない知識もきっと必要になってきます
- 参考となる資料
    - [Kaggleに登録したら次にやること ～ これだけやれば十分闘える！Titanicの先へ行く入門 10 Kernel ～ \- Qiita](https://qiita.com/upura/items/3c10ff6fed4e7c3d70f0)
    - KaggleのNotebooks
        - Vote数でソートするのがおすすめです
        - Scoreが表示されているものを参考にするとよいかもしれません
 

### 課題L-3: 0.78超え
- sklearnの使い方に加えて、1つか2つのアイデアがあれば到達できると思います

### 課題L-4: 0.80超え
- さらなる高みを目指しましょう



以上
