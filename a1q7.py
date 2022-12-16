num=int(input('enter your keyboard'))
d1,d2,d3,d4,d5,sum=int
d1=(num%10)
d2=(num%100)/10
d3=(num%1000)/100
d4=(num%10000)/1000
d5=(num/1000)
sum=d1+d2+d3+d4+d5

print(sum)