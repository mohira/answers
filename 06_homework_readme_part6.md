第6回 課題説明
====================

## はじめに: 今回はチームでの取り組み
- 今回はすべての課題をチーム単位で一緒に取り組んでもらいます
- チーム編成は下記のとおりです
  - ※ 河相さんはどこかのチームに入ってください(業務都合で自習時間を確保できるかを知らないため)
- 最初にチーム名とリーダーを決めておいてください(そして教えて下さいね)

### チーム編成
1. 大山 山本 杉山
2. 松崎 原田 鈴木
3. 古澤 西見 三浦

### 進め方
どう進めるかはチームにお任せしますが、全体の利益が高まるような行動を方針としてください。
学習環境に何か不都合があればうまいこと解決してください。

### 開発環境について: ローカルかWebか
- 学習は基本的にGPUで行うべきものと考えてください(KaggleNotebooks or GoogleColaboratory)
- ただし、PyCharmやローカルのJupyterの方が効率よく開発できるのでうまく使い分けてみましょう

## 課題R: 【チーム課題】Metricsの可視化
DigitRecognizerにおけるMetricsを可視化しましょう。
Metricsをわかりやすく把握できることは作業の質に直結します。

### エポックごとの正答率
エポックごとの正答率を出力するようにコードを変更してください

### 学習の様子の可視化
次の値をエポックごとにプロットしたグラフを作成するようにしてください

1. 訓練データおよび検証データにおけるLoss
2. 訓練データおよび検証データにおけるAccuracy

### 実験
各種設定を変更してみて学習の様子やPublicScoreがどう変わるかを実験して簡易なレポートをつくってください。

- ネットワークのアーキテクチャ
- Optimizer
- エポック数
- バッチサイズ
- データの前処理
- などなど  


## 課題S:【チーム課題】CIFAR-10での学習
- PyTorch公式のチュートリアルを写経してください
  - [Training a Classifier — PyTorch Tutorials 1\.3\.0 documentation](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html#sphx-glr-beginner-blitz-cifar10-tutorial-py)

### 写経のポイント
- 講義での実装方針と異なる部分や使ってない命令もありますが素直に写経しましょう
  - 例: 講義では自作Datasetでやってきましたが、チュートリアルでは`torchvision.datasets.CIFAR10` を利用している
- CIFAR-10は画像分野でよく使われるデータなのでEDAも行っておくと◎です  
- 適宜リファクタリングしてみましょう
  - よりわかりやすい変数の導入
  - 意義のあるコメントの追加や削除
  - 変数の抽出やインライン化
  - 関数やクラスへの切り出し


## 課題T: 【チーム課題】アリvsハチの学習コード
- `hymenoptera_data`を使ってCNNで学習するコードを実装してください
- 自作のDatasetクラスは講義中に実装しているのでそのまま使いましょう
- 学習のコードは暗記する必要はないです。過去のコードと見比べながら実装してみましょう
- なるべく高いAccuracyがでるようにモデルの構造などをいじってみましょう


## 課題U: 【チーム課題】転移学習の写経
- PyTorch公式の転移学習チュートリアルを写経してください
  - [Transfer Learning for Computer Vision Tutorial — PyTorch Tutorials 1\.3\.0 documentation](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)
  - 利用しているデータは `hymenoptera_data` です

### 写経のポイント
- 学習するときはColaboratoryやKaggleのGPU環境を使いましょう
  - すべてColaboratoryで実装すると開発しにくいかもしれません
  - ローカル環境で実装をほとんど終えてからColabで実行するのもアリですね
- すべてを理解しようとしなくてOKです
  - 講義での実装方針と異なる部分や使ってない命令もあります
    - わからない部分があったらMax3分くらい粘る
    - 解決すれば周りに伝える、解決しない場合は講義で質問できるようしておく

## 課題V: 自作Datasetや自作Transforms
- PyTorch公式のチュートリアルを写経してください
  - [Writing Custom Datasets, DataLoaders and Transforms — PyTorch Tutorials 1\.3\.0 documentation](https://pytorch.org/tutorials/beginner/data_loading_tutorial.html)



以上

<!--- 追加課題のメモ
## 課題X: argparseを利用した実験の高速化
- [argparse \-\-\- コマンドラインオプション、引数、サブコマンドのパーサー — Python 3\.7\.5 ドキュメント](https://docs.python.org/ja/3/library/argparse.html)

---->
