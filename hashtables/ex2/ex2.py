#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    route = [None] * length  

    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    x = cache["NONE"]

    for i in range(length):
        route[i] = x
        x = cache[x]
        

    return route
