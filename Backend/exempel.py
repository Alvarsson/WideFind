import requests

port = 4000
url = "http://127.0.0.1:" + str(port)
print(url)

"""
I GraphQL så väljer du vilken information du vill hämta. I det första exemplet precis under så väljer vi att hämta
id, active (boolean) id på alla neighbors (länkade gateways). En lista med alla attributer finns i 
/api/src/schema.graphql under "type Gateway".
"""

"""
Frågar efter alla gateways i databasen.
"""
query_all_gateways = """
{
    Gateway
    {
        id
        active
        neighbors {
            _id   
        }
    }
}
"""

"""
Frågar efter alla gateways som är inactiva. Andra parametrar går också att sätta såklart.
"""
query_specific_gateways = """
{
    Gateway(active: false)
    {
        id
        active
        neighbors {
            id   
        }
    }
}
"""

"""
Skapa en ny !!tom!! gateway som sedan returneras.
    tom = alla attributer förutom id är "null". Id är auto generated och är en lång jobbig String.
Vill ni skapa en gateway med vissa parametrar så lägger man bara till dom, t.ex:
    CreateGateway(active: false, ...)
"""
mutation_create_gateway = """
mutation {
    CreateGateway {
        id
    }
}
"""


"""
Uppdatera attributer för en given gateway. "id" parametern behövs för att identifiera vilken gateway som ska uppdateras.
Resten av parametrarna uppdateras till angivna värden. 
Returnerar den uppdaterade gatewayen.
"""
mutation_update_gateway = """
mutation {
    UpdateGateway(id: "...", x: 2) {
        id
        x
    }
}
"""

"""
Lägg till en länk. Noder som är länkade till varandra är sparade i varandras "neighbor" lista. 
Det spelar ingen roll vilken nod som är i "from" och "to", relationen är "bidirectional".
Returnerar gateways "from" och "to".
"""
mutation_add_relationship = """
mutation {
  AddGatewayNeighbors(from: {id: "..."}, 
                      to: {id: "..."}
  ) {
    from {
      id
    }
    to {
      id
    }
  }
}
"""

"""
Ta bort en länk på samma sätt som du lägger till dom
Returnerar gateways "from" och "to".
"""
mutation_remove_relationship = """
mutation {
  RemoveGatewayNeighbors(from: {id: "..."}, 
                      to: {id: "..."}
  ) {
    from {
      id
    }
    to {
      id
    }
  }
}
"""

parameters = {"query": query_all_gateways}

result = requests.post(url, json=parameters)
print(result.text)