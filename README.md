# random_bits_analysis

## はじめに

物理乱数の検証を行うプログラムをまとめるリポジトリ

## 使い方(hexデータの場合)

[data](./data/)ディレクトリに検定したい16進数表記のtxtファイルを置き，`./verify_hex.sh`を実行

## 使い方(binデータの場合)

[bin_ascii_data](./bin_ascii_data/)ディレクトリに検定したい2進数表記のtxtファイルを置き，`./verify_binascii.sh`を実行

## 確認方法

dataディレクトリに置いた乱数の数だけresultディレクトリに同名のディレクトリが作成される

その中にあるファイルはすべて検証結果となる
