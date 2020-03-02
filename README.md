# WideFind

Alla komponenter går att starta var för sig, men enklast är att använda docker-compose vilket skapar små virtuella maskiner som automatiskt säkerställer dependencies för modulerna och sätter upp kommunikation.

## Docker

### Windows/Mac

Installera Docker Desktop. Programmet finns att hämta här: https://www.docker.com/products/docker-desktop

### Linux

Se först till att du har docker installerat. Förslagsvis från din pakethanterare. Annars är Google din vän.

Läs instruktionerna hur du installerar docker-compose här: https://linuxize.com/post/how-to-install-and-use-docker-compose-on-ubuntu-18-04/ eller här: https://computingforgeeks.com/how-to-install-latest-docker-compose-on-linux/ 

## Starta hela systemet
Navigera till projektets hemmapp i en terminal. Samma mapp där du finner filen docker-compose.yml. Kör kommandot:
```
> docker-compose up -d
```

### Starta enskilda komponenter
```
> docker-compose up neo4j/api/ui -d
```

## Bygg om projektet
Måste köras när du ändrat i koden. Bygg bara om projektet som du ändrat för att spara tid. Det kan ta en stund.
```
> docker-compose up --build -d neo4j/api/ui
```

## Starta utan docker / docker-compose
För att fungera på localhost måste två filer ändras.
1. Frontend/app/main/functions.py
   1. Byt ut url till http://localhost+str(port)
2. Backend/api/.env
   1. Byt ut NEO4J_URI till bolt://localhost:7687

Sedan kan frontenden startas med Flask som vanligt och backenden startas med vanlig neo4j desktop samt att starta API:et med npm start.