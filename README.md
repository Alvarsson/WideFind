# WideFind

Alla komponenter går att starta var för sig. Enklast är att använda docker-compose vilket skapar små virtuella maskiner som automatiskt säkerställer dependencies för modulerna och sätter upp kommunikation mellan dessa.

Detta rekommenderas dock inte under utveckling när man hela tiden testar väldigt små förändringar då byggtiden kan ta en del tid. Kolla istället in avsnittet nedan om hur man startar enskilda komponenter.

## Docker

För att starta med Docker måste två filer ändras.
1. Frontend/app/main/functions.py
   1. Byt ut url från \"http://localhost\"+str(port) till \"http://api\"+str(port)
2. Backend/api/.env
   1. Byt ut NEO4J_URI från bolt://localhost:7687 till bolt://neo4j:7678

### Windows/Mac

Installera Docker Desktop. Programmet finns att hämta här: https://www.docker.com/products/docker-desktop

### Linux

Se först till att du har docker installerat. Förslagsvis från din pakethanterare. Annars är Google din vän.

Läs instruktionerna hur du installerar docker-compose här: https://linuxize.com/post/how-to-install-and-use-docker-compose-on-ubuntu-18-04/ eller här: https://computingforgeeks.com/how-to-install-latest-docker-compose-on-linux/ 

### Starta hela systemet
Navigera till projektets hemmapp i en terminal. Samma mapp där du finner filen docker-compose.yml. Kör kommandot:
```
> docker-compose up -d
```

### Starta enskilda komponenter
```
> docker-compose up neo4j/api/ui -d
```

### Bygg om projektet
Måste köras när du ändrat i koden. Bygg bara om projektet som du ändrat för att spara tid. Det kan ta en stund.
```
> docker-compose up --build -d neo4j/api/ui
```

## Enskilda komponenter

Detta rekommenderas under utveckling då man inte behöver bygga om projektet vid förändringar.

### Neo4j

#### Windows

Installera Neo4j Desktop från https://neo4j.com/download`

#### Mac

Installera neo4j förslagsvis via brew.
```
> brew install neo4j
> neo4j start
```

### API

Navigera till Backend/api och kör
```
> npm install
> npm start
```

### Frontend
Förutsatt att du använder python 3 som default. Navigera till Frontend och kör
```
> pip install -r requirements.txt
> flask run
```