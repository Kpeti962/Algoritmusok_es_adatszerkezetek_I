# Sam and Substrings feladatleírás

## Forrás:
#### https://www.hackerrank.com/challenges/sam-and-substrings/problem?isFullScreen=true

#### Samantha és Sam egy számjátékot játszanak. Egy számot kapnak meg sztringként, amely nem tartalmaz kezdő nullákat. A feladat az, hogy határozzuk meg a sztring összes részsztringjének egész értékeinek összegét.

#### Adott egy szám sztringként, és az a feladat, hogy az összes részsztringjét átalakítva egész számokká, összeadjuk. Mivel az összeg nagy lehet, az eredményt modulo 10^9+7-tel kell visszaadni.

#### Példa n = '42'. Itt az n egy sztring, amely három lehetséges részsztringet tartalmaz: 4, 2 és 42.
#### Ezek összege 48, és 48 mod (10^9+7)=48
#### Függvény Leírás
#### Készítsd el a substrings nevű függvényt a szerkesztőben.

#### A substrings függvény a következő paraméterekkel rendelkezik: 
##### string n: egy egész szám sztring reprezentációja

#### Visszatérési érték:
##### int: az összes részsztring egész értékének összege modulo 10^9+7