daftar_golongan = {
    "A" :  5000000,
    "B" :  6500000,
    "C" :  9500000
                   }

golongan = input("golongan A/B/C  :  ").upper()
jam_lembur = int(input("jam_lembur:  "))

gaji_pokok = daftar_golongan.get(golongan)

if gaji_pokok :
    if jam_lembur == 0 :
        persen_lembur = 0
    elif jam_lembur == 1 :
        persen_lembur = 0.30
    elif jam_lembur == 2 :
        persen_lembur = 0.32
    elif jam_lembur == 3 :
        persen_lembur = 0.34
    elif jam_lembur == 4 :
        persen_lembur = 0.36
    else :
        persen_lembur = 0.38 
        
    total_uang_lembur = jam_lembur * (persen_lembur * gaji_pokok)
    total_gaji = gaji_pokok + total_uang_lembur
    
    print ("\n-------------------------------------")
    print (f"golongan           :{golongan}")
    print (f"gaji pokok         :RP{gaji_pokok:,.0f}")
    print (f"jam lembur         :{jam_lembur} jam")
    print (f"persen lembur      :{ persen_lembur * 100:.0f}% per jam")
    print (f"total uang lembur  :RP{total_uang_lembur:,.0f}")
    print ("----------------------------------------")
    print (f"total gaji diterima:RP {total_gaji:,.0f}")
else:
    print("\nGolongan tidak valid! Harap masukkan A, B, atau C.") 