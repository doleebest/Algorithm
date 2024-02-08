x = int(input()) #(1)
y = int(input()) #(2)

#(3)
y1 = (y%100)%10 #5
result3 = x*y1

#(4)
y2 = (y -y1)%100 #80
result4 = int(x*y2/10)

#(5)
y3 = y-y1-y2
result5 = int(x*y3/100)

print(result3)
print(result4)
print(result5)
print(x*y)


