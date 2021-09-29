numri= int(input("Jep numrin: "))
temp=numri
reverse=0
while(numri>0):
    shifra = numri % 10
    reverse = reverse * 10 + shifra
    numri = numri // 10

if (temp==reverse):
    print("Numri eshte palindrome")
else:
    print("Numri nuk eshte palindrome")
