# Kandidat baris ramalan — Charm the Commuter (kota fiktif, <=140 karakter)
# Dinilai terhadap 5 kriteria juri (urutan penting):
# 1. Ramalan satu baris, kota fiktif disebut, cuaca jadi inti
# 2. Membuat komuter bosan tersenyum sekali baca
# 3. Register ramalan sungguhan, ritme siaran yang dibengkokkan
# 4. Satu detail konkret cuaca/kehidupan kota
# 5. Tiap kata berguna dalam 140 karakter

A = "Pluvwick: rain all day, 11C, buses late as ever — bring a brolly, the number 7 is already swimming."
B = "Good morning, Drizzlemere: drizzle till dusk, 12C, and the 8:04 bus is running ten minutes late, as is tradition."
C = "Mizzleford: steady rain, 13C, buses delayed by puddles — take a brolly, leave your hopes of dry socks at home."
D = "Rain in Pluvwick all day, 11C, with the 8:04 bus ten minutes late — the puddles have formed a queue of their own."

# Penilaian (skala 1-5 per kriteria):
# A: 1:5 2:4 (bus berenang lucu, tapi agak datar) 3:4 4:4 (bus 7) 5:4 -> total 21
# B: 1:5 2:4 ("as is tradition" manis) 3:5 (sapaan siaran) 4:4 (bus 8:04) 5:4 -> total 22
# C: 1:5 2:4 (kaus kaki basah) 3:4 4:3 (puddle generik) 5:4 -> total 20
# D: 1:5 2:5 (antrean genangan = gambaran mengejutkan, khas komuter) 3:5 4:5 (bus 8:04 + antrean genangan) 5:4 -> total 24
# PEMENANG: D, dengan "11C" diganti "11°C" (114 karakter).
FINAL = "Rain in Pluvwick all day, 11°C, with the 8:04 bus ten minutes late — the puddles have formed a queue of their own."
assert len(FINAL) == 114
