import random

# ユーザーから最小値と最大値を入力
n = int(input("最小値を入力してください: "))
m = int(input("最大値を入力してください: "))

# 最大値が最小値より小さくないことを確認
if n > m:
    print("最小値は最大値以下でなければなりません。")
else:
    # 乱数を生成
    rand_num = random.randint(n, m)
    attempts = 5  # 試行回数の制限
    for i in range(attempts):
        guess = int(input("数を推測してください: "))
        if guess == rand_num:
            print("正解です！")
            break
        elif guess < rand_num:
            print("もっと大きい数です。")
        else:
            print("もっと小さい数です。")
    else:
        print(f"残念！正解は {rand_num} でした。")
