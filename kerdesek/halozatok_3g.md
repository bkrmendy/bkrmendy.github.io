# Mik az áramkörkapcsolás jellemzői?
A klasszikus telefonhálózatok voltak áramkörkapcsoltak. Végponttól végpontig garantált minőségű csatornát szolgáltat. A kommunikáció előtt hívásfelépítés, utána pedig lebontás történik. A csatornát csak a hívó és a hívott fél használhatja, ha éppen nem beszélnek, üres a csatorna. Lehet fizikailag egy áramkör, de lehet általánosabb értelemben egy csatorna (pl. adott időrés, adott frekvencia egy nyalábolt átviteli rendszerben).

# Miben változtatott ehhez képest a csomagkapcsolás?
A számítógép-hálózatok újdonsága volt, az átvitt információt kis csomagokra bontva továbbítja. Nem kell hívásfelépítés, bontás a használthoz. Előnye a statikus multiplexelés: ha épp nincs kommunikáció, más is használhatja a csatornát, így összességében nagyobb forgalom bonyolítható le ugyanakkora csatornán (és így olcsóbb is). Hátránya, hogy a minőség (Quality of Service, QoS) nem garantált, külön feladat marad.

# Mik az UMTS céljai?
GSM-nél jobb beszédhangminőség, GSM-nél jobb frekvenciakihasználtság, GSM-nél nagyobb adatátviteli sebesség, GSM kompatibilitás.

# Milyen szolgáltatásokat nyújt az UMTS?
Beszédátvitel az AMR kodekkel (4,7 - 12,2 kb/s)
Adatátvitel, Internet-elérés 3G-n keresztül (városban max 384 kb/s, vidéken 144 kb/s)
Multimédia szolgáltatások 3G felett: Videótelefonálás, TV adások közvetítése, rádióhallgatás , filmek, zenék letöltése – ezek nem váltak be.

# Hogy néz ki az UMTS hálózat?
(3. diasor -> 7.oldal)

# Milyen duplexitás-kezelést használ az UMTS? (2)
FDD (nagyobb frekvencia a lefele irányban (nagyobb csillapítás nagyobb teljesítmény kell), TDD (a fel- és letöltés időben váltakozik ugyanabban a frekvenciasávban, előnye: a fel/letöltés aránya dinamikusan változtatható az aktuális igények függvényében).

# Hány MHz-s csatornákra osztják a rádiós közeget és milyen közeghozzáférést alkalmaznak benne?
5 MHz, CDMA

# Hogy működik a CDMA?
Minden jel „szét van kenve” a teljes spektrumra, de kis teljesítménnyel. Célja a jobb spektrumkihasználtság.

# Mik az UMTS kódosztás lépései?
1. Csatornakódolás
2. Csatornázási kódolás
3. Keverő kódolás
4. Rádiófrekvenciás modulálás, kisugárzás

# Mit csinál a csatornázási kód?
E kód a keskenysávú bemenő jelet szélessávúvá alakítja. A kiterjesztési faktor változik 4 és 512 között mozog: azt adja meg, hogy hányszorosa lesz a chipsebesség a bitsebességnek (másképpen: hány chip hosszú egy szóró kód, hány db szóró kód van). 
A chipsebesség viszont mindig fix: 3 840 000 chip/sec


# Hogy működik a csatornázási kód?
A digitális jelet összeszorozzuk (pontosabban: NOT(XOR(b1, b2))) egy ún. szóró kóddal (spreading code), és ezt sugározzuk ki. A szóró kód bitsebességge (chiprate) sokkal nagyobb (kb. 100x), mint a jelé.
A szóró kódok ortogonálisak, azaz egy bitidőre átlagolva két szórókód szorzatát nullát kapunk.

# Miért működik ez tökéletesen ortogonális csatornázási kódokkal?
<Kidolgozni>
Azonban az ortogonalitás csak akkor teljesül, ha pontosan egy fázisban vannak a kódok. Nem azonos kezdőfázis esetén sem magával, sem másik kóddal nem nulla a korrelációja, azaz közös órajel kell.
Gyakorlatban: azonos adó különböző csatornáinak elválasztására használják.

# Hogyan lehet OVSF kódokat generálni?
C2x,2y-1=(Cx,y,Cx,y) és C2x,2y =(Cx,y,-Cx,y)
Látszik, hogy 2n hosszú kódból 2n darab van.
Ortogonálitás bizonyítása: teljes indukcióval

# Mi a keverő kódolás célja?
A keverő kódok csak kvázi ortogonálisak egymásra, ugyanakkor önmaguk időbeli eltoltjára is kvázi ortogonálisak. Fajtájuk ún. pseudo-noise, „ál-zaj” kódok, nevük Gold kód.
Célja az adóberendezések megkülönböztetése. Adónként van egy ilyen kód: lefele irány: cellák (azaz Node B-k) elkülönítése, felfele irány: végberendezések elkülönítése. Nem igényelnek szinkronizációt a források között, azonban nem teljes az ortogonalitás: a vevő az egyik forrás jelének dekódolásakor a többi forrás jelét enyhe zajnak érzékeli. A cella kapacitását itt az szabja meg, hogy meddig nem zavaró még ez a zaj a dekódolásban.
Az NOT(XOR(a,b)) szorzás itt bitenként történik: egy bit a kódolandó jelfolyamból, egy bit a kódból. A kódszavak hossza: lefele: 38 400 bit (10 msec-enként ismétlődik), felfele: 38 400 bit, vagy 256 bit. Ez utóbbi, ha a Node B speciális vevővel rendelkezik (ún. rake vevő).







































