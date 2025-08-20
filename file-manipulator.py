import sys
from typing import Tuple


# メイン関数
def main():
    # 引数を受け取る
    args = sys.argv[1:]
    # 検証
    ok, message = validate_args(args)
    if not ok:
        print(message)
        sys.exit(1)
    # 振り分け
    command, params = args[0], args[1:]
    # 検証
    try:
        dispatch(command, params)  # 実処理
    except Exception as error:
        print(f"エラー: {error} ")
        sys.exit(1)


# -----------部品(バリデート・ディスパッチ)-------------


# バリテーション関数 ->bool, string
def validate_args(args: list[str]) -> Tuple[bool, str]:
    # コマンドに必要な引数の数
    command_map = {
        "reverse": 2,
        "copy": 2,
        "duplicate_contents": 2,
        "replace_string": 3,
    }
    # コマンドの未入力チェック
    if len(args) == 0:
        return False, "エラー: コマンドが入力されていません。"
    # コマンド
    command = args[0]
    # コマンドの存在テェック
    if command not in command_map:
        return False, f"エラー： {command} は未登録です。"
    # 引数個数のチェック
    required_args = command_map[command]
    if len(args) - 1 != required_args:
        return False, f"エラー: {command} には {required_args} 個の引数が必要です。"
    return True, ""


# 振り分け関数　-> None
def dispatch(command: str, params: list[str]) -> None:
    # スペック辞書
    spec = {
        "reverse": lambda params: reverse(params[0], params[1]),
        "copy": lambda params: copy(params[0], params[1]),
        "duplicate_contents": lambda params: duplicate_contents(params[0], int(params[1])),
        "replace_string": lambda params: replace_string(params[0], params[1], params[2]),
    }
    # 未知のコマンド
    try:
        fn = spec[command]
    except KeyError:
        raise ValueError(f"未知のコマンド: {command} ")
    try:
        fn(params)
    except (IndexError, ValueError) as e:
        raise ValueError(f"{command}: 引数が不正です({e})")


# -------部品(スペック関数)-------
def reverse(input_path, output_path):
    process_file(input_path, output_path, lambda s: s[::-1])

def copy(input_path, output_path):
    process_file(input_path, output_path, lambda s: s)

def duplicate_contents(input_path, n):
    """input_path を読み込み、その内容を複製し、複製された内容を input_path に n 回複製する"""
    def dup(s):
        if n < 0:
            raise ValueError("回数は 0 以上で入力してください")
        return s * (n + 1)
    process_file(input_path, input_path, dup)

def replace_string(input_path, needle, new_string):
    """input_path にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'new_string' に置き換える"""
    def repl(s):
        return s.replace(needle, new_string)
    process_file(input_path, input_path, repl)

def process_file(input_path, output_path, transform):
    """共通の入出力をラップして、変換だけ外から渡す。"""
    try:
        with open(input_path, "r", encoding = "utf-8") as f:
            data_file = f.read()
        result = transform(data_file)
        with open(output_path, "w", encoding = "utf-8") as f:
            f.write(result)
    except FileNotFoundError:
        raise FileNotFoundError(f"{input_path} が見つかりません")
    except Exception as e:
        raise RuntimeError(f"reverse でエラーが発生しました: {e}")

if __name__ == "__main__":
    main()
