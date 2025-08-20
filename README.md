# File Manipulator

Pythonで書かれたシンプルなファイル操作ツールです。\
コマンドライン引数を通じて、ファイル内容の反転、コピー、内容の複製、文字列の置換といった操作を行うことができます。

## 機能

-   **reverse**: ファイルの内容を逆順にして新しいファイルを作成
-   **copy**: ファイルをコピーして新しいファイルを作成
-   **duplicate_contents**: ファイルの内容を指定回数複製して上書き保存
-   **replace_string**: ファイル内の指定文字列を新しい文字列に置換

## 必要環境

-   Python 3.8 以上\
-   外部ライブラリ不要（標準ライブラリのみ使用）

## 使い方

``` python
# 一般的な実行形式
python file_manipulator.py <コマンド> <引数...>
```

### 実行例

``` python
# ファイルの内容を逆順にして保存
python file_manipulator.py reverse input.txt output.txt

# ファイルをコピー
python file_manipulator.py copy input.txt output.txt

# ファイル内容を3回複製して上書き保存
python file_manipulator.py duplicate_contents input.txt 3

# 文字列 "foo" を "bar" に置換
python file_manipulator.py replace_string input.txt foo bar
```

## エラーハンドリング

以下のケースではエラーメッセージを表示します: -
コマンドが未入力または不明
- 引数の数が正しくない
- ファイルが存在しない
- 不正な値（例: 複製回数に負数を指定した場合）

## ライセンス

MIT License
