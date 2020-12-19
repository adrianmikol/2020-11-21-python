osoba1 = {"imie":"Xawery", "wzrost":1.81, "waga":72 }
osoba2 = {"imie":"Zdzisław", "wzrost":1.61, "waga":92 }
osoba3 = {"imie":"Zygmunt", "wzrost":1.91, "waga":71 }
osoba4 = {"imie":"Alojzy", "wzrost":1.72, "waga":93 }

osoby = [ osoba1, osoba2, osoba3, osoba4 ]

# wypisz osoby posortowane wg wzrostu
osoby.sort(key=lambda osoba:osoba["wzrost"])

# wypisz osoby posortowane wg wzrostu (od najwyższego)
osoby.sort(key=lambda osoba:-osoba["wzrost"])
osoby.sort(key=lambda osoba:osoba["wzrost"], reverse=True)

# wypisz osoby posortowane wg BMI

osoby.sort(key=lambda o:o['waga']/(o['wzrost']**2))

for o in osoby:
    print(o)
