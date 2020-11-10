#awal

print("Program ini adalah program pengkonversian suhu")
print ("Program ini mencakup konversi suhu dari:")
print ("="*50)
print ("Celcius - Fahrenheit")
print ("Celcius - Kelvin")
print ("Celcius - Reamur")
print ("=" * 50)

#proses

SuhuAwal = float(input("masuka suhu Celcius awal :"))
a= SuhuAwal
#rumus

f= 9/5 * a +32
print ("suhu konversi Celcius to Fahrenheit adalah", f, "derajat F")

K= a +273
print ("suhu konversi Celcius to Kelvin adalah", K, "K")

R= 4/5 * a
print ("suhu konversi Celcius to Reamur adalah", R, "derajat R")

#closing
print ("="* 50)
print ("terimakasih telah menggunakan Program ini")