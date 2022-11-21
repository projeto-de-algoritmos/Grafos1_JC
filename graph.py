import os
from Godgraph import G
from godList import god

def graph(G, first, second):
    inQueue = []
    visited = []
    begin = first
    end = second
    visited.append(begin)
    inQueue.append(begin)

    while inQueue:
            aux = inQueue.pop(0)

            for neighbour in G[aux]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    inQueue.append(neighbour)
            return visited

def checkRelationship(connectedGodOne, connectedGodTwo):
    oldConnectedGodOne = connectedGodOne
    oldConnectedGodTwo = connectedGodTwo
    attempts = 0
    first = []
    second = []
    userTyped = ''

    while connectedGodOne != connectedGodTwo:
        if connectedGodOne == userTyped and userTyped != '':
            print('')
            print(oldConnectedGodOne + " "*15 + oldConnectedGodTwo)
            print(*first, sep = "\n")
            for i in second:
                print(" "*20 + i)
            print('')
        elif connectedGodTwo == userTyped and userTyped != '':
            print('')
            print(oldConnectedGodOne + " "*15 + oldConnectedGodTwo)
            print(*first, sep = "\n")
            for i in second:
                print(" "*20 + i)
            print('')    
        else:
            if first or second:
                print('')
                print(oldConnectedGodOne + " "*15 + oldConnectedGodTwo)
                print(*first, sep = "\n")
                for i in second:
                    print(" "*20 + i)
                print('')
            else:
                print('')
                print(oldConnectedGodOne + " "*15 + oldConnectedGodTwo)
                print('')

        userTyped = input(f'Conecte os seres mitologicos {oldConnectedGodOne} e {oldConnectedGodTwo}: ')
        if userTyped == 'lista':
            print(*god, sep = ", ")
        elif userTyped in god and userTyped not in first and userTyped not in second and userTyped != oldConnectedGodOne and userTyped != oldConnectedGodTwo:
            searchBegin = graph(G, connectedGodOne, userTyped)
            searchEnd = graph(G, connectedGodTwo, userTyped)
            if first == []:
                first.append(userTyped)
            if second == []:
                second.append(userTyped)
            for element in first: 
                searchBegin2 = graph(G, oldConnectedGodOne, element)
            for element2 in second:
                searchEnd2 = graph(G, oldConnectedGodTwo, element2)

            if (userTyped in searchBegin or userTyped in searchBegin2) and (userTyped in searchEnd or userTyped in searchEnd2): 
                connectedGodTwo = userTyped
                connectedGodOne = userTyped
                attempts+=1
                messageSuccess = 'Você conectou os deuses ' + oldConnectedGodOne + ' e ' + oldConnectedGodTwo + ' em ' + str(attempts) + ' tentativas!'
                if attempts == 1:
                    messageSuccess = 'Você conectou os deuses ' + oldConnectedGodOne + ' e ' + oldConnectedGodTwo + ' pelo menor caminho! Parabéns!'
                os.system('clear')
                print(oldConnectedGodOne + " "*15 + oldConnectedGodTwo)
                print('')
                print(*first, sep = "\n")
                for i in second:
                    print(" "*20 + i)
                print(" "*10 + userTyped)
                print('')
                print(messageSuccess)
            elif (userTyped in searchBegin or userTyped in searchBegin2) and (userTyped not in searchEnd or userTyped not in searchEnd2):
                messageSuccessOne = 'Você conectou os deuses ' + connectedGodOne + ' e ' + userTyped + '. Continue para chegar em: ' + oldConnectedGodTwo
                if userTyped == first[0] and len(first) == 1:
                    first.pop()
                if userTyped == second[0] and len(second) == 1:
                    second.pop()
                if userTyped not in first:
                    first.append(userTyped)
                connectedGodOne = userTyped
                attempts+=1
                os.system('clear')
                print(messageSuccessOne)
            elif (userTyped not in searchBegin or userTyped not in searchBegin2) and (userTyped in searchEnd or userTyped in searchEnd2):
                messageSuccessTwo = 'Você conectou os deuses ' + connectedGodTwo + ' e ' + userTyped + '. Continue para chegar em: ' + oldConnectedGodOne
                if userTyped == first[0] and len(first) == 1:
                    first.pop()
                if userTyped == second[0] and len(second) == 1:
                    second.pop()
                if userTyped not in second:
                    second.append(userTyped)
                connectedGodTwo = userTyped
                attempts+=1
                os.system('clear')
                print(messageSuccessTwo)
            else:
                if userTyped == first[0] and len(first) == 1:
                    first.pop()
                if userTyped == second[0] and len(second) == 1:
                    second.pop()
                messageFail = 'Os deuses ' + oldConnectedGodOne + ', ' + oldConnectedGodTwo + ' e ' + userTyped + ' não possuem ligação direta'
                os.system('clear')
                print(messageFail)
        else:
            os.system('clear')
            print(f'Ser mitologico {userTyped} já digitado ou não existe, digite outro:')
