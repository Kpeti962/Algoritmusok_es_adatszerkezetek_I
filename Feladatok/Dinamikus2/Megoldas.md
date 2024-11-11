#### Ez a feladat ezért született meg, mert utólag vettem észre, hogy csak amiatt tudtam "lefoglalni" a Roads and Libraries feladatot, mivel elírtam a nevét.

#### Elsőnek létrehozzuk a modulo változóját, a végösszeget és az aktuális összeget beállítjuk 0-ra

    mod = 10**9 + 7;
    vegosszeg = 0;
    aktual_osszeg = 0;

#### Végigiterálunk az n-en, ahol megkeressük az éppen aktuális számokat a stringben. Az aktuális összeget a korábban számított aktual_osszeg tízszeresével bővítjük, mivel egy új számjegyet hozzáadunk a végéhez. Az aktuális számjegy értéke szorozva (i + 1)-gyel figyelembe veszi, hogy az i-edik számjegy hány részstringhez járul hozzá.

     for i in range(len(n)):
        aktual_szam = int(n[i]);
        aktual_osszeg = (aktual_osszeg * 10 + aktual_szam * (i + 1)) % mod;
        

#### Majd a végösszeghez folyamatosan hozzáadogatjuk a részösszegeket, majd megnézzük a moduló változóval osztott maradékát és a végén visszaadjuk azt a függvényben.

        vegosszeg = (vegosszeg + aktual_osszeg) % mod;

    return vegosszeg;