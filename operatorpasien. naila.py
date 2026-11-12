print("=== SISTEM MONITORING 10 JENIS PASIEN OPNAME ===")
print("1. Pasien Demam Berdarah (DBD)   6. Pasien Patah Tulang")
print("2. Pasien Tifus (Tipes)          7. Pasien Asma Akut")
print("3. Pasien Pasca Operasi          8. Pasien Diabetes Melitus")
print("4. Pasien Pneumonia              9. Pasien Stroke Ringan")
print("5. Pasien Persalinan            10. Pasien Cedera Kepala")
print("================================================")

# Input jenis pasien dan lama hari opname
pilih_pasien = int(input("Pilih nomor jenis pasien (1-10) : "))
lama_opname = int(input("Masukkan lama hari rawat inap   : "))

# Batas pembanding hari opname
batas_standar = 5
batas_intensif = 14

# Kondisional untuk menentukan jenis pasien dari 10 pilihan
if pilih_pasien == 1:
    jenis_pasien = "Pasien Demam Berdarah (DBD)"
elif pilih_pasien == 2:
    jenis_pasien = "Pasien Tifus (Tipes)"
elif pilih_pasien == 3:
    jenis_pasien = "Pasien Pasca Operasi"
elif pilih_pasien == 4:
    jenis_pasien = "Pasien Pneumonia"
elif pilih_pasien == 5:
    jenis_pasien = "Pasien Persalinan"
elif pilih_pasien == 6:
    jenis_pasien = "Pasien Patah Tulang"
elif pilih_pasien == 7:
    jenis_pasien = "Pasien Asma Akut"
elif pilih_pasien == 8:
    jenis_pasien = "Pasien Diabetes Melitus"
elif pilih_pasien == 9:
    jenis_pasien = "Pasien Stroke Ringan"
elif pilih_pasien == 10:
    jenis_pasien = "Pasien Cedera Kepala"
else:
    jenis_pasien = "Kategori Pasien Tidak Valid"

print("\n--- HASIL OPERATOR PEMBANDING (RAWAT INAP) ---")
print("Kategori :", jenis_pasien)
print(lama_opname, "==", batas_standar, "(Pas batas standar 5 hari) :", lama_opname == batas_standar)
print(lama_opname, "!=", batas_standar, "(Tidak sama dengan 5 hari) :", lama_opname != batas_standar)
print(lama_opname, ">", batas_standar,  "(Lebih dari 5 hari)        :", lama_opname > batas_standar)
print(lama_opname, "<", batas_standar,  "(Kurang dari 5 hari)       :", lama_opname < batas_standar)
print(lama_opname, ">=", batas_intensif, "(Perawatan jangka panjang):", lama_opname >= batas_intensif)
print(lama_opname, "<=", 2,             "(Perawatan singkat/observasi):", lama_opname <= 2)

print("\n--- KEPUTUSAN KONDISIONAL RUMAH SAKIT ---")
if lama_opname <= 2:
    print("TINDAKAN:", jenis_pasien, "masuk masa observasi awal. Belum boleh pulang.")
elif lama_opname < batas_standar:
    print("TINDAKAN:", jenis_pasien, "masih dalam masa pemulihan standar.")
elif lama_opname == batas_standar:
    print("TINDAKAN:", jenis_pasien, "mencapai hari ke-5. Jadwalkan pemeriksaan akhir dokter.")
elif lama_opname >= batas_intensif:
    print("TINDAKAN:", jenis_pasien, "dirawat >= 14 hari. Perlu evaluasi tim medis lanjutan.")
else:
    print("TINDAKAN:", jenis_pasien, "melewati masa standar (6-13 hari). Lanjutkan pemantauan harian.")