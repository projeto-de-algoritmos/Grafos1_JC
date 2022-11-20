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
    attempts = 1
    newConnectedGodOne = ''
    newconnectedGodTwo = '1'
    godsAttemps = []

    if connectedGodOne != connectedGodTwo:
        search = graph(connectedGodOne, connectedGodTwo)
        if search:
            while newConnectedGodOne != newconnectedGodTwo:
                searchBegin = graph(connectedGodOne, userTyped)
                searchEnd = graph(userTyped, connectedGodTwo)
                if len(searchBegin) == 1 and len(searchEnd) != 1:
                    newConnectedGodOne = userTyped
                    attempts+=1
                    return userTyped
                elif len(searchEnd) == 1 and len(searchBegin) != 1:
                    newconnectedGodTwo = userTyped
                    attempts+=1
                    return userTyped
                elif len(searchEnd) == 1 and len(searchBegin) == 1: 
                    newconnectedGodTwo = userTyped
                    newConnectedGodOne = userTyped
                    attempts+=1
                    message = f'Você conectou os deuses {connectedGodOne} e {connectedGodTwo} em {attempts} tentativas!'
                    return message
                else:
                    message = f'Os deuses {connectedGodOne},{connectedGodTwo} e {userTyped} não possuem ligação direta'
                        return message

#TO DO: IMPORTAR A LISTA DE DEUSES GREGOS E RECEBER O INPUT DO FRONT