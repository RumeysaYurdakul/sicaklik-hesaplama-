#sıcaklık dönüşüm programı
#10.11.2020


derece=eval(input("derece  (c) cinsinden sıcaklığı giriniz :"))


#dönüşümler

kelvin = 273 + derece

fahr=32 + ( 1.8 * derece )      #burada parantez kullanmaya mecbur değiliz
                                                #çünkü zaten çarpmanın işlem önceliği var 



#ekran yazdırma 
print(derece,"C=",kelvin,"kelvin")
print(derece,"C=",fahr,"fahrenheit")


