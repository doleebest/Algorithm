words = input()
only_words = words.split(' ')
sum =0
for i in only_words :
    if bool(i) :
        sum+=1
print(sum)