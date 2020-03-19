第5回 課題説明
====================
## 課題N: PyTorch入門
### 課題N-1: PyTorchのインストール
- https://pytorch.org/get-started/locally/ を参考にしてPyTorchを実行する環境を作ってください
- PyTorchのバージョンは `1.2.0` にすること

### 課題N-2: Tensorの基本操作
- Tensorの操作に慣れるために次のスクリプト群の写経をしてください(コピペはしないでね)
    - https://github.com/mohira/answers/tree/master/N_pytorch_tensor
    - [PyTorch公式のチュートリアル: What is PyTorch? — PyTorch Tutorials 1\.2\.0 documentation](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py)
- 使える命令は `numpy` と結構似ています
- PyCharmでもJupyterNotebookでも構いません  

### 課題N-3: モデルの学習コードの写経
- 次の4つの機械学習タスクを行うコードを写経してください(https://github.com/mohira/answers/tree/master/O_simple_models_using_pytorch)
    1. フルスクラッチでの単回帰 (`O1_linear_regression_scratch.py`)
    2. `nn`モジュールを使った単回帰 (`O2_linear_regression_using_nn.py`)
    3. ロジスティック回帰で2クラス分類(irisを2クラス分類問題として解く) (`O3_binary_logistic_regression.py`)
    4. 多クラス分類(digitsを利用) (`O4_multi_class_logistic_regression.py`)
- sklearnと違って `.fit(X, y)` だけでは学習できないので、とにかく書き慣れが必要です

## 課題O: MNISTデータセットのEDA
### 課題O-1: MNISTとは何か？ 
- MNIST という非常に有名なデータセットがあります。どんなデータなのかを調べてください。

### 課題O-2: MNISTのEDA
- MNISTを使ったKaggleコンペ  [Digit Recognizer | Kaggle](https://www.kaggle.com/c/digit-recognizer) があります
- このコンペのデータを使ってEDAを行ってください
- データをダウンロードしてもよいですし、Kaggle上のNotebookを使っても構いません
- ヒント: 他のKagglerが公開しているNotebook(旧称: Kernel)を参考にしてみましょう
    - 公開されているNotebook → https://www.kaggle.com/c/digit-recognizer/notebooks
      - 「Most Votes」でソートするとよいです(Notebookは玉石混交)
    - EDAをするときは、「EDA」「Visualization」「Starter」などと検索すると便利です
- ヒント: 英語を読むのがしんどい人は下記のChrome拡張をいれると最高にはかどります
  - [英語の文章を選択するだけで和訳を表示させる方法](https://little-hands.hatenablog.com/entry/2017/11/03/google-translator)

### 課題O-3: Digit Recognizer で自作モデルSubmission
- 自作のモデルを構築し、Submissionを完了させてください
    - PublicScoreは気にしなくてOKです
    - とにかく自作のモデルでSubmissionができればOKです
- ヒント: データの量に注意
    - データの量が多いので、適当に調節しないと学習に相当時間がかかると思います


## 課題P: 学習の流れ
- 改めて機械学習における「学習」の流れを理解しましょう
- `PyTorch` や `Tensorflow` などのライブラリでは `sklearn` と違って内部の処理が露出しています
    - メリット: カスタマイズがしやすい
    - デメリット: 自分で書かないといけない量が増える
- 学習の流れを理解することが、実装やデバッグの助けになります    
    

### 課題P-1: 学習の基本的な流れ
- 機械学習における学習の流れを説明できるようにしてください
    - モデルのパラメータを推定するまでにどんな手順をたどりますか？
    - 大まかな手順がイメージできていればOKです(数学的な完全理解までは不要) 
- わからない部分があれば、どこがわからないのかを明らかにすることを頑張ってください
- 関連キーワード
    - 損失関数
    - 最適化
    - 勾配降下法
    - 誤差逆伝播

### 課題P-2: バッチ学習とミニバッチ学習
- バッチ学習とミニバッチ学習について説明できるようにしてください
- わからない部分があれば、どこがわからないのかを明らかにすることを頑張ってください
- 関連キーワード
    - エポック
    - 確率的勾配降下法


## 課題Q: 一連の学習コードの実装
### 課題Q-1: irisで前処理+GridSearch
- irisデータを利用して機械学習の一連の流れを実装しましょう
- ただし、下記の条件を満たすこと
    - 評価指標: 正答率
    - 評価プロトコル
        - testデータは全体の2割を使うこと
        - 10分割のStratifiedKFold
    - 対象モデル: ロジスティック回帰 / 決定木 / SVM / RandomForest 
    - 特徴量: 4次元全て利用
    - 前処理: 標準化を適用
    - パラメータ探索範囲: 各モデルについて重要そうなパラメータを適当に探索すること
    - random_state: 何らかの値で固定する(再現性を担保する)
- その他、適切な分析や考察を行うこと    

### 課題Q-2: タイタニック gender_submission 超え
- タイタニックのデータで一連の流れを実装し、Submissionを完了させましょう
    - すでにPublicScoreが0.76555を超えている人は更なる高みを目指してください
        - アイデアが枯渇した場合は、周りのメンバーと相談するなり、KaggleのNotebookを参考にしてください
- ただし、下記の条件を満たすこと
    - 評価指標: 自由
    - 評価プロトコル
        - 交差検証を使うこと
        - 交差検証のバリエーションや分割数は自由
    - 対象モデル: ロジスティック回帰 / 決定木 / SVM / RandomForest 
    - 特徴量: 自由
    - 前処理: 自由
    - パラメータ探索範囲: 各モデルについて重要そうなパラメータを適当に探索すること
    - random_state: 何らかの値で固定する(再現性を担保する)
- さまざまな特徴量生成やモデル、パラメータを使った実験になるので、上手に方法や結果を管理できるにはどうするがいいかを考えてください
- きっと 0.76555 は超えると思います
- その他、適切な分析や考察を行うこと

### 課題Q-3: タイタニックに飽きた人は別のコンペ(自由課題)
- タイタニックに飽きたり、Submission制限に達してしまったりしたひとは是非別のコンペにも挑戦してみてください
- コンペ候補になりそうなもの
    - [Categorical Feature Encoding Challenge \| Kaggle](https://www.kaggle.com/c/cat-in-the-dat) 
    - [Home Credit Default Risk \| Kaggle](https://www.kaggle.com/c/home-credit-default-risk)
    - [初心者お勧め過去コンペ](https://kaggler-ja-wiki.herokuapp.com/kaggle初心者ガイド#初心者お勧め過去コンペ)





以上
