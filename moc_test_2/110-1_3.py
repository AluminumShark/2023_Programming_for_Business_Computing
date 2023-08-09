length = int(input())
word = input()
comma = "。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !\"#$%&'()*+,-./:;<=>?@[\]^_`{¦}~"

word_list = []
for i in range(len(word)) :
    if i + length <= len(word) :
        conti = word[i : i + length]
        if not any(n in comma for n in conti) :
            word_list.append(conti)
    else : 
        break

word_set = list(set(word_list))
for i in range(len(word_set)) :
    word_set[i] = [word_set[i], 0]

for i in range(len(word_set)) :
    for j in range(len(word_list)) :
        if word_set[i][0] == word_list[j] :
            word_set[i][1] += 1

out_put = []
for i in range(len(word_set)) :
    if word_set[i][1] > 1 :
        out_put.append(word_set[i])

out_put.sort(key=lambda x : (-x[1], x[0]))
out_put = [[x[0], str(x[1])] for x in out_put]

if length >= 2 :
    for i in range(len(out_put)) :
        print(" ".join(out_put[i]))
else :
    print("ILLEGAL_N")