cena=float(input('Podaj cenę:'))
znizka=float(input('Podaj procentową zniżkę:'))
kwotaznizki=cena-cena*znizka
nowacena=round(cena-kwotaznizki,2)
print(f'Pierwotna cena to {cena}, a po zniżce {nowacena}')