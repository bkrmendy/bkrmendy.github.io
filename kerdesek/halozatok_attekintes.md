# Mi a cellás elv?
A cellás elvben a frekvencia-tartomány X részre van felosztva, mindegyik cellában a frekvenciatartomány 1/X-ed részét használják.
Mivel az azonos frekvenciákat használó cellák nem fedik át egymást, nincs interferencia közöttük.

# Mi a különböző cellaméretek előnyei/hátrányai?
A kisebb cellák előnye, hogy kis adóteljesítmény elég (kisebb élettani kockázat, kisebb fogyasztás), és hogy nagyobb forgalom bonyolítható adott területen (nagyobb forgalomsűrűség).
Hátránya, hogy sok bázisáloomásra van szükség (rontja a látképet, drága felépíteni).

# Mik az 1G rendszerek jellemzői?
1970-80-as években alakultak ki.
Analóg rendszer, sok, egymással nem kompatiblis megvalósítása volt (Nordic Mobile Telephone System).
Viszonylag nagy (35-50 km) átmérőjű cellákból állt, jellemzően 450 MHz körüli frekvenciasávval.
Gyenge volt a beszédátviteli minőség, kevés szolgáltatásfajtát támogatott.

# Mik a 2G rendszerek jellemzői?
Az 1990-es évek elejétől jelentek meg, és az 1G-vel szemben már digitális rendszerek voltak. 

# Mik az új koncepciók a GSM rendszerben?
A GSM egy közös, európai rendszernek lett tervezve, ahol csak a hívó fél fizet a hívásért.
Elérhető szolgáltatás volt a roaming, az SMS és a titkosított beszédátvitel.
Az előfizetőket SIM kártya azonosította, így adataik készülékfüggetlenek maradtak.

# Mik a GSM rendszer paraméterei (sugárzási teljesítmény, cella nagysága)?
Sugárzási teljesítmény: 2 W és adaptív, azaz csak a minimális szükségessel ad a végberendezés. Ez kíméli a telefon akkumulátorát, minimalizálja az élettani kockázatot és nem zavarja a többi cellát.
A cella átmérője 500m és 35 km között változhat (tervezői döntés az adott tartományon belül, függ a frekvenciától, forgalomsűrűségtől, terjedési viszonyoktól).

# Milyen multiplexálási stratégiákat használ a GSM?
TDMA és FDMA (Time Division Multiple Access és Frequency Division Multiple Access).

# Mik a GSM 900 jellemzői?
A mobil adó 890-915 MHz, bázisállomás 935-960 MHz-en ad (e tartományban kisebb frekvencia kisebb csillapítást szenved, így kisebb teljesítményt igényel, ezért a mobil adóé az alsó sáv).
25 MHz-es sáv, egy vivő 200 kHz -> 124 vivő  (FDMA).  Ezen az összes helyi szolgáltató osztozik, hazánkban kb. 40 vivő (frekvenciasáv)/szolgáltató e sávban.
Vivőnként 8 db időrést (TDMA) ajánl fel. 40*8/10 ~ 32 csatorna / cella (10 féle frekvenciakiosztású cella létezik).
Kb. 32 egyidejű beszélgetés folyhat egy cellában. Half Rate kódolással kétszer annyi csatorna érhető el (de rosszabb minőséggel, így ezt nem minden esetben használják, a GSM 1800 orvosolja ezt a problémát).
Maximum 35 km a cellaátmérő, mivel a 900 MHz körüli hullámok valamelyest követik a földfelszínt. Így országos lefedésre alkalmas a technológia.

# Mik a GSM 1800 jellemzői?
A mobil adó: 1710-1785 MHz, bázisállomás: 1805-1880 MHz-en ad. 75 MHz-es sáv (plusz háromszoros kapacitás a GSM 900-hoz képest), de rosszabb a hullámterjedése (egyenesen terjed, gyorsabban csillapodik). Emiatt országos lefedésre nem, csak nagy forgalmú kis területek ellátására alkalmas.

# Hogy működik a GSM átadás?
A GSM valós áramkörkapcsolás, így ha a mobil végberendezés átmegy egy másik cellába: átadás (handover v. handoff) történik, közben nem szakad meg a kapcsolat.
Három handover stratégia létezik:
1. a mobil végberendezés irányításával: méri, mikor erősebb egy másik cella jele
2. a hálózat irányításával: az dönt a jelerősség és esetleg más információk (pl. cella terheltsége) alapján
3. a hálózat irányításával, a mobil készülék segítségével: a hálózat megkéri a végberendezést, hogy küldjön jelerősségi információt, de a döntést a hálózat hozza.
A GSM-ben a 3. típusú van megvalósítva (így pl. egy leterhelt cellába csak később lépteti be a hálózat az oda közeledő végberendezést).

# Hogy épül fel a GSM hálózat?
(2. diasor -> 16-17. dia)

# Mi a bázisállomás-alrendszer (BTS) feladata?
A BTS egy vagy több elemi adó/vevőből (elementary transmitter/receiver) áll.
A bázisállomás-vezérlő (BSC) egy vagy több bázisállomást vezérel, 1) a beszédcsatornák összekötését (kapcsolás), 2) a rádiócsatorna-hozzárendelést, 3) és a hívásátadás-vezérlést kezeli (kapcsolás), 

# Mik tartoznak a hálózati alrendszerhez (MSC)?
Az MSC egy hagyományos telefonközpont, mobil-specifikus bővítésekkel: authentikáció, helyzetnyilvántartás, hívásátadás BSC-k között, barangolás stb.
Az MSC tartalmazza a látogatói helyregisztert (VLR) is. A VLR a HLR információinak egy részét tárolja ideiglenesen (ami a hívásfelépítéshez szükséges) az ott tartózkodó mobil állomásokról.
A HLR az előfizetőre vonatkozó adatokat, szolgáltatási jogosultságokat, tartózkodási helyet tárolja. Hálózatonként egy HLR van jelen.
Ezen kívül a hitelesítő központ (Authentication Center, AuC) is az MSC része.

# Milyen azonosítók léteznek a GSM-ben?
MSISDN: Mobile Station ISDN Number, mobil állomás ISDN szám. Ez a jól ismert mobil telefonszám, egyedi a világon. Előállítása: országkód (Mo.: 36) + hálózatkijelölő szám (Mo:20/30/70) + előfizetői szám.
IMSI: International Mobile Subscriber Identity, nemzetközi mobil előfizető azonosító. A GSM hálózatokban elsősorban ez azonosítja az előfizetőt: az adatbázisok ezzel vannak indexelve. A SIM kártyához van rendelve, egyedi a világon. Előállítása: IMSI = mobil országkód (Mo: 216) + mobil hálózati kód (Mo.:01/30/70) + 10 jegyű mobil előfizető azonosító szám. szolgáltatóváltásnál az MSISDN maradhat, de a SIM kártyát és ezzel együtt az IMSI-t cserélni kell.
IMEI: International Mobile Equipment Identity, nemzetközi mobilkészülék-azonosító. A végberendezést azonosítja, egyedi a világon. Előállítása: <készülékazonosító> (8 jegyű) + <gyári szám> (6 jegyű) + <ellenőrző számjegy> (1 jegyű) (+<szoftver verzió>). Lekérdezése: *#06#
MSRN: Mobile Station Roaming Number, barangoló szám. Egy VLR-hez tartozó helyi címtartományba tartozó telefonszám, amit az arra járó GSM készülék ideiglenesen használ. A felhasználó számára transzparens, nem látszik. Ez teszi lehetővé, hogy a szám utaljon a földrajzi helyre: ebből a számból már tudni, hogy merre kell keresni az adott készüléket, ha felhívja valaki.

# Hogy van nyilvántartva a végberendezés helye a GSM-ben?
Cella szinten való nyilvántartással az a gond, hogy túl gyakran kéne frissíteni, és nagy hálózati forgalom alakulna ki.
Országos szinten nyilvántartáskor túl nagy területen kéne keresni (pl. beérkező híváskor), és szintén túl nagy a forgalom.
A probléma megoldására egy kompromisszum alakult ki: a Location Area. Néhány (tipikusan 20-30) cella együttese, a köztük való cellaváltáskor nincs helyzetfrissítés (Location update). Csak LA váltáskor van helyzetfrissítés. Bejövő híváskor/SMS-kor broadcast keresési üzenet (paging) a Location Area-ban. Alapvetően ennél pontosabban nem tárolja a hálózat, hogy hol vagyunk!

# Milyen GSM szolgáltatások léteznek?
Beszédátvitel: a kodek sebessége 13 kb/s (később: 5,6 kb/s is). Kompromisszum: viszonylag gyenge hangminőség, jobb a frekvenciakihasználtság.
SMS: Short Message Service, rövid szöveges üzenet szolgáltatás, maximum 160 karakteres üzeneteket lehet küldeni.
Adatátvitel: kezdetben 9,6 kb/s, később 14,4 kb/s, majd ez folyamatosan nőtt.
MMS: Multimedia Messaging Service, multimédia üzenetküldő szolgáltatás: multimédia üzenet: kép, írott szöveg, hang együtt, 2002-től elérhető.

# Miben egészítette ki a GPRS a GSM-et?
GPRS (General Packet Radio Service, általános csomag alapú rádiós szolgáltatás), csomagkapcsolt adatátvitellel egészítette ki a GSM-et. Előnye a jobb kihasználtság, és fizetés kilobájt alapon, nem perc szerint. Adatsebesség kb. 60-80 kb/s. Komoly hálózatfejlesztést igényelt.

# Hogy néz ki a GSM/GPRS hálózat?
(2/27-28)

# Miben egészítette ki az EDGE a GSM-et?
Az EDGE (Enhanced Data Rate for Global/GSM Evolution) 2003-ban jelent meg, javított modulációs eljárást hozott be: eredetileg 1 bit/szimbólum volt (Gaussian minimum shift keying, GMSK), és ezt javította 8PSK, 3 bit/szimbólumra (háromszoros adatátviteli sebesség). Ez csak jobb jel/zaj viszony esetén működik (kevésbé zavartűrő). Az adatsebesség kb. 150-180 kb/s lett.
