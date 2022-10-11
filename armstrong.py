#liste mantığını kullan
print("*************çıkmak için q ya basınız.****************")
sayı = input("lütfen bir sayı giriniz:")
liste=list(sayı)
toplam = 0
for i in liste:
  elemanlar=int(i)
  toplam+=pow(elemanlar,len(liste))
print("toplam=",toplam)
if toplam == int(sayı):
 print("armstrong sayıdır.")
else:
   print("armstrong sayı değildir.")