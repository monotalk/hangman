def myfavoritecolorgame():
    colors = ["black", "green", "blue"]
    colors_amount = len(colors)

    guess = input("僕の好きな色は${colors_amount}色あるよ！君の好きな色は？")

    if guess in colors:
        print("いいセンスしてるね！！"*3)
    else:
        print("イマイチ！！")
myfavoritecolorgame()