import random
from graph import checkRelationship
from graph import graph
from godList import god
from Godgraph import G

connectedGodOne = random.choice(god)
connectedGodTwo = random.choice(god)

search = graph(G, connectedGodOne, connectedGodTwo)

while connectedGodOne == connectedGodTwo or connectedGodTwo in search:
    connectedGodTwo = random.choice(god)

if connectedGodOne != connectedGodTwo and connectedGodTwo not in search:
    print('')
    print('Digite os seres mitologicos com a primeira letra maiúscula. Se precisar da lista de seres digite lista!')
    final = checkRelationship(connectedGodOne, connectedGodTwo)