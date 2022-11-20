# TO DO: VERIFICAR RETORNO DO BFS E DEFINIR GRAFO
graph = {}

def graph(graph, first, second):
    inQueue = []
    visited = []
    begin = first
    end = second
    visited.append(begin)
    inQueue.append(begin)

    while inQueue:
            aux = inQueue.pop(0)

            for neighbour in graph[aux]:
                if neighbour not in visited and neighbour != end:
                    visited.append(neighbour)
                    inQueue.append(neighbour)
                return composition

def checkRelationship(userTyped):
    connectedGodOne = random.choice(god)
    connectedGodTwo = random.choice(god)
    oldconnectedGodOne = ''
    oldconnectedGodTwo = ''
    attempts = 1
    godsAttemps = []

    while connectedGodOne == connectedGodTwo:
        connectedGodTwo = random.choice(god)

    if connectedGodOne != connectedGodTwo:
        oldConnectedGodOne = connectedGodOne
        oldConnectedGodTwo = connectedGodTwo
        search = graph(connectedGodOne, connectedGodTwo)
        if search:
            while connectedGodOne != connectedGodTwo:
                searchBegin = graph(connectedGodOne, userTyped)
                searchEnd = graph(userTyped, connectedGodTwo)
                if len(searchBegin) == 1 and len(searchEnd) != 1:
                    connectedGodOne = userTyped
                    attempts+=1
                    return userTyped
                elif len(searchEnd) == 1 and len(searchBegin) != 1:
                    connectedGodTwo = userTyped
                    attempts+=1
                    return userTyped
                elif len(searchEnd) == 1 and len(searchBegin) == 1: 
                    connectedGodTwo = userTyped
                    connectedGodOne = userTyped
                    attempts+=1
                    message = f'Você conectou os deuses {oldConnectedGodOne} e {oldConnectedGodTwo} em {attempts} tentativas!'
                    return message
                else:
                    message = f'Os deuses {oldConnectedGodOne},{oldConnectedGodTwo} e {userTyped} não possuem ligação direta'
                        return message

#TO DO: IMPORTAR A LISTA DE DEUSES GREGOS E RECEBER O INPUT DO FRONT