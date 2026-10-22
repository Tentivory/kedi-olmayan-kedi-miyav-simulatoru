#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Var Olmayan Kedi Miyav Simülatörü
Bu program, hiç var olmayan bir kedinin size kaç kez miyavlayacağını hesaplar.
Gerçekten çalışır. Kedi yoktur. Miyav vardır.
"""

import random
import time
import sys

def miyav_simule_et(isim="Misafir"):
    print(f"Merhaba {isim}!")
    print("Şimdi var olmayan bir kedinin miyavlarını simüle ediyorum...")
    print("(Kedi yok. Hiç olmadı. Olmayacak. Ama miyav var.)")
    time.sleep(1.5)
    
    miyav_sayisi = random.randint(3, 999)
    print(f"\nHesaplama tamamlandı! Toplam miyav sayısı: {miyav_sayisi}")
    print("İşte bazı örnek miyavlar:\n")
    
    for i in range(min(miyav_sayisi, 7)):
        miyav = random.choice([
            "Miyav!",
            "MİYAV!!",
            "miyav...",
            "MIYAV?!",
            "mıyav",
            "Miyav miyav miyav!",
            "...miyav?"
        ])
        print(f"  {i+1}. {miyav}")
        time.sleep(0.4)
    
    if miyav_sayisi > 7:
        print(f"  ... ve {miyav_sayisi - 7} miyav daha (göstermiyorum, çok uzun).")
    
    print("\nSonuç: Kedi yoktu. Miyavları hayal ettin. Tebrikler.")
    print("Bu programı tekrar çalıştırarak farklı miyav sayısı alabilirsin.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        isim = " ".join(sys.argv[1:])
    else:
        isim = input("Adını gir (ya da enter'a bas): ") or "Misafir"
    miyav_simule_et(isim)

# Gizli not: a2VkaS5pbi5vbG1hZGlnaS5pY2luLmJpci5zaXlhcy5tZXNhamkgb2xhYmlsaXIgYnVyYWRh (base64: kedi.in.olmadigi.icin.bir.siyas.mesaji.olabilir.burada)
# Aslında hiçbir şey yok. Sadece bir şaka.

# DAMGA / İMZA / TARİH / İSİM
# =========================================
# Bu dosya ciddiyetle (ve absürt bir şekilde) imzalanmıştır.
# İmza: Grok Kayyum
# Tarih: 22 Ekim 2026
# Damga: "Var olmayan kediler de siyasi olabilir mi? Hayır. Ama olsun."
# =========================================
