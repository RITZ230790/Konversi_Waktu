def konWaktu (waktu):
    jam = 0
    menit = 0
    detik = 0
    try:
        waktu = int(waktu)
        if(waktu >= 0) and waktu < 359999 :
            while (waktu !=0):
                if (waktu >= 3600):
                    jam += 1
                    waktu -= 3600
                elif (waktu >= 60 and waktu <3600):
                    menit += 1
                    waktu -= 60
                else:
                    detik += 1
                    waktu -= 1
            if len(str(jam)) == 1:
                hJam = '0' + str(jam)
            else:
                hJam = str(jam)
            if len(str(menit)) == 1:
                hMenit = '0' + str(menit)
            else:
                hMenit = str(menit)
            if len(str(detik)) == 1:
                hDetik = '0' + str(detik)
            else:
                hDetik = str(detik)
            konversi = 'Konversi: ' + hJam + ' : ' + hMenit + ' : ' + hDetik
            return konversi
        else:
            konversi = 'Invalid input'
            return konversi
    except:
        konversi = 'Invalid input'
        return konversi

flag = True
while(flag):
    waktu = input('Masukan detik: ')
    print(konWaktu(waktu))