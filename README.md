# WideFind

Alla komponenter går att starta var för sig. Enklast är att använda docker-compose vilket skapar små virtuella maskiner som automatiskt säkerställer dependencies för modulerna och sätter upp kommunikation mellan dessa.

Detta rekommenderas dock inte under utveckling när man hela tiden testar väldigt små förändringar då byggtiden kan ta en del tid. Kolla istället in avsnittet nedan om hur man startar enskilda komponenter.

För att lägga in demodata kör man förslagsvis följande kommando via GraphQL:
```
mutation{
  m0:CreateMarker(id:"0",x:1,y:1){id,x,y}
  m1:CreateMarker(id:"1",x:2,y:2){id,x,y}
  m2:CreateMarker(id:"2",x:3,y:3){id,x,y}
  m3:CreateMarker(id:"3",x:4,y:4){id,x,y}
  m4:CreateMarker(id:"4",x:5,y:5){id,x,y}

  mmr0: AddMarkerNeighbors(from:{id:"0"}, to:{id:"1"}){from{id}to{id}}
  mmr1: AddMarkerNeighbors(from:{id:"1"}, to:{id:"2"}){from{id}to{id}}
  mmr2: AddMarkerNeighbors(from:{id:"2"}, to:{id:"3"}){from{id}to{id}}
  g0: CreateGateway(uuid:"hex0"){uuid}
  g1: CreateGateway(uuid:"hex1"){uuid}
  g2: CreateGateway(uuid:"hex2"){uuid}
  g3: CreateGateway(uuid:"hex3"){uuid}

  CreateStatic(id: 0, marker_counter: 5, relation_counter: 6){id}
  CreateConnected(id:0){id}
  CreateUnconnected(id:0){id}

AddGatewayMarker(from:{uuid:"hex0"}, to:{id:"0"}){from{uuid}to{id}}
  AddMarkerGateway(from:{id:"0"}, to:{uuid:"hex0"}){from{id}to{uuid}}
}
```

## Docker (Compose)

För att starta med Docker-Compose måste man först säkerställa:
1. Att man har Docker och Docker-Compose installerat (se nedan).
2. Frontend/app/main/functions.py
   1. URL ska vara "http://api"+str(port)
3. Backend/api/.env
   1. NEO4J_URI ska vara bolt://neo4j:7678

Docker-Compose är tacksamt då det startar upp alla enskilda containers automatiskt och sätter upp internt nätverk mellan dessa. Projektet bygger de enskilda komponenterna med vanliga Dockerfiles, så det går att utesluta Compose-funktionaliteten. Då måste man dock gå igenom docker-compose-filen och ersätta en del av funktionaliteten som finns där till antingen Dockerfilerna, och/eller kommandon som startar containrarna. 

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

För att starta komponenterna enskilt utan Docker måste man säkerställa:
1. Frontend/app/main/functions.py
   1. URL ska vara "http://localhost"+str(port)
2. Backend/api/.env
   1. NEO4J_URI ska vara bolt://localhost:7678

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

## Användning

### Event notification

I Backend/api/.env finns en variabel som heter "OBSERVER_IP". Denna bör ändras till det IP som man vill ska lyssna efter nya Event-händelser i databasen. Se GraphQL-avsnittet under om hur man gör för att skapa sådana objekt. Innehållet i "content" är det som kommer skickas som en URL-request.

OBS! Denna del bör egentligen implementeras för fler typer av händelser i databasen. Hur man lägger till liknande funktionalitet för andra typer av händelser kan man se i Backend/api/src/resolvers.js

### GraphQL

Lättaste sättet att sätta sig in i GraphQL för detta projektet är att besöka localhost:4000 när projektet är uppsatt. Där finns en playground som innehåller alla objekt i databasschemat och dokumentation.

### Neo4j

För att komma åt databasen direkt kan man navigera till localhost:7474. Default-lösenordet är "letmein" om man inte ändrat detta i Backend/api/.env.

Bra Cypherkoder att kunna är
```
MATCH (a) RETURN a; // Returnerar hela databasen.
```