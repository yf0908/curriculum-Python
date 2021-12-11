all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]

for place in all_place:
    if place in get_place: #ここから記述（ヒント：in演算子を用いて、条件分岐）
        print(place + "のチケットが当選しました！")
    elif place in wait_place: #ここから記述（ヒント：in演算子を用いて、条件分岐
        print(place + "のチケットは結果待ち")
    else:
        print(place + "のチケットは落選しました")

new_get_place = get_place + wait_place
s = "{}と{}と{}のチケットが当選しました！"
print(s.format(new_get_place[0], new_get_place[1], new_get_place[2]))