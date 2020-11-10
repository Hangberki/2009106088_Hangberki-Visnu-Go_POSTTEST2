#inputan awal

print ("program info tentang kopi")
print ("Pertanyaan Singkat")
tanya = input("mau tau mendalam soal kopi. seperti aku ingin tau dirimu ?? (iya/tidak)")

#proses printing

if tanya == "iya":

	print ("="*70)

	Kopi = []

	NamaKopi = input("masukan nama kopi yang anda ketahui :")
	JenisKopi = input("masukan jenis kopi yang di maksud tadi :")
	KetinggianKopi = float(input("masukan ketinggian di tanamnya kopi tersebut :"))
	SuhuKopi = int(input("masukan suhu air untuk menyeduh kopi :"))
	TempatRoaster = input ("masukan tempat roasting kopi tersebut :")
	TempatNgopi = input ("masukan tempat kalian ngopi :")

	print ("="*70)

	print("nama kopi yang kalian masukan ", NamaKopi)
	print("jenis kopi ", JenisKopi, "adalah", JenisKopi)
	print("kopi ini di tanam di ketinggian", KetinggianKopi)
	print("kopi ini identik diseduh dengan suhu", SuhuKopi)
	print("kopi ini di roasst oleh ", TempatRoaster)
	print("oh ternyata suka ngopi di ", TempatNgopi)

	Kopi.append(NamaKopi)
	Kopi.append(JenisKopi)
	Kopi.append(KetinggianKopi)
	Kopi.append(SuhuKopi)
	Kopi.append(TempatRoaster)
	Kopi.append(TempatNgopi)

	print (Kopi)

else:
	print("ya sudah sihhh")