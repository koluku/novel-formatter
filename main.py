import sys
import re


def main(args):
    input_file = args[1]

    with open(input_file, "r") as f:
        body = f.read()

        # 空白をすべて削除する
        body = re.sub(r"(　)", "", body)

        # 文頭に空白を入れる
        body = re.sub(r"^(?![「『]).*$", "　", body)

        # 感嘆符の後に空白を入れる
        body = re.sub(r"[！？](?![」』\n])", "　", body)

        # 3点リーダに直す
        body = re.sub(r"・・・", "……", body)

        # ダッシュに直す
        body = re.sub(r"ーー", "――", body)

        # 鉤括弧の中で記号の直前・直後に空白を作らない
        body = re.sub(r"((?<=[「『])(　)+)|((　)+(?=[」』]))", "", body)

        # 2行以上の改行を1行の改行にする
        body = re.sub(r"(?<![。」])(\n)+", "\n", body)

    with open(input_file, "w") as f:
        f.write(body)


if __name__ == "__main__":
    args = sys.argv
    main(args)
