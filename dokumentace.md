# IPK Projekt 1 - FIT VUT 2019
Pre prístup je nutná bezplatná registrácia a získánie kľúča, ktorý sa používa v dotazoch pre autentifikáciu. Ku projektu patrí zároveň aj súbor Makefile, pomocou ktorého spustíte skript formou:

    make run api_key=<API kľúč> city=<Mesto>
    
Ak chceme získať informácie o meste s viacslovným názvom, musíme názov vložiť medzi `""` . 
Iba tak sa úspešne načíta celý názov ako jeden argument.
Pre konkretizáciu mesta (existuje viacero miest s rovnakým názvom) poskytuje API možnosť pridať za názov mesta aj informáciu o krajine.
Napr. `... city=Brno,CZ` , `... city="novy hrozenkov,cz"`.

## O projekte
Skript v jazyku Python - (klient rozhrania OpenWeatherMap), ktorý pomocou HTTP dotazu získa vybrané informácie o počasí z dátového zdroja. 

### Zadanie
Projekt bol zameraný na využitie knižnice na prácu so socketmi. Cieľom bol lightweight klient s minimálnym počtom závislostí, zároveň som sa však snažil využiť možnosti vysokoúrovňového jazyka python a zjednodušiť tak prácu na projekte.

## Postup
Po načítaní argumentov vytvorím dotaz GET vo forme bajtov. Vytvorím socket a naviažem spojenie s HOSTom cez PORT. Odošlem dotaz ak som sa úspešne pripojil, ak som úspešne dostal odpoveď, hľadám v odpovedi informácie na výpis vo formáte json.

## Správanie

### Úspešné načítanie informácií
V prípade úspešného príjmu požadovaných informácií o zadanom meste skript vypíše na štandardný výstup popis počasia, teploty, vlhkosti, tlaku, rýchlosti a smeru vetra. Môže nastať prípad, kedy je v danom meste rýchlosť vetra pomerne nízka a dáta o smere vetra chýbajú. 
V tom prípade reprezentuje absentujúcu informáciu `-` . 

    Cityname: Zakopane
    Weather: few clouds
    Temperature: -3 °C
    Humidity: 68 %
    Pressure: 1032 hPa
    Wind-speed: 7.56 km/h
    Wind-degree: 360

### Nesprávne argumenty
V prípade nesprávneho kľúča API dôjde k chybovému výpisu a ukončeniu programu:

    Error: 401 Unauthorized
    
V prípade neexistujúceho zadaného mesta / mesta o ktorom nemá API informácie dôjde k chybovému výpisu a ukončeniu programu:  

    Error: 404 Not Found

## Autor
`Matej Dubec - xdubec00`

## Zdroje

[Socket Programming in Python (Guide)](https://realpython.com/python-sockets/),
[OWM API Documentation](https://openweathermap.org/current)