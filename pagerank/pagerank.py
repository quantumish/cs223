class Website():
    def __init__(self, name, incoming, outgoing): # takes string name, list incoming, list outgoing
        self.name = name
        self.incoming = incoming
        self.outgoing = outgoing
    def append_incoming(self, items):
        for item in items:
            self.incoming.append(item)
    def append_outgoing(self, items):
        for item in items:
            self.outgoing.append(item)

def PageRank(d, node, prev_round): # takes integer d, Website node, and dictionary prev_round
    current_round = {}
    score = (1-d)
    for i in node.incoming:
        prev_score = prev_round[i.name]
        outgoing = len(i.outgoing)
        score += (d*(prev_score/outgoing))
    return score

def iterate(d, supernode, prev_round, iterations):
    for i in range(iterations):
        current=prev_round.copy()
        current["super"] = PageRank (d, supernode, prev_round)
        for node in supernode.outgoing:
            current[node.name] = PageRank(d, node, prev_round)
        prev_round=current.copy()
    return current

supernode = Website("super", [], [])
a = Website("a", [], [])
b = Website("b", [], [])
c = Website("c", [], [])
d = Website("d", [], [])
supernode.append_incoming([a,b,c,d])
supernode.append_outgoing([a,b,c,d])
a.append_incoming([c,supernode])
a.append_outgoing([c,b,supernode])
b.append_incoming([a,supernode])
b.append_outgoing([c,supernode])
c.append_incoming([a,b,d,supernode])
c.append_outgoing([a,supernode])
d.append_incoming([supernode])
d.append_outgoing([c,supernode])
initial_round = {"super":0.2, "a":0.2, "b":0.2, "c":0.2, "d":0.2}
print (iterate(0.85, supernode, initial_round, 1000))
