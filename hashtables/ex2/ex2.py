#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


tickets = [
  ['PIT', 'ORD'],
  ['XNA', 'CID'],
  ['SFO', 'BHM'],
  ['FLG', 'XNA'],
  [None, 'LAX'], 
  ['LAX', 'SFO'],
  ['CID', 'SLC'],
  ['ORD', None],
  ['SLC', 'PIT'],
  ['BHM', 'FLG'],
]

def reconstruct_trip(tickets, length):
    hash = HashTable(length)
    # hash = {}
    route = [None] * length
    # route = [None] * (len(tickets)-1)


    # for ticket in tickets:
    #     if tickets[0] == "NONE":
    #         route[0] = tickets[1]

    #     hash[tickets[0]] = tickets[1]

    # print(hash)
    # print(route)

    # for i in range(1, len(tickets)-1):
    #     route[i] = hash[route[i-1]]

    for ticket in tickets:

        hash_table_insert(hash, ticket.source, ticket.destination)
        
        start = hash_table_retrieve(hash, 'NONE')

        route[0] = start

    for i, r in enumerate(route):

        if i + 1 > len(route) - 1:
            break

        route[i + 1] = hash_table_retrieve(hash, r)

    return route

# print(reconstruct_trip(tickets))


