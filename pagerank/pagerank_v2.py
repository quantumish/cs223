import random
import math
import networkx as nx
import json 
import matplotlib.pyplot as plt

class Website():
    def __init__(self, name, incoming, outgoing): # takes string name, list incoming, list outgoing
        self.name = name
        self.incoming = incoming
        self.outgoing = outgoing
    def append_incoming(self, items):
        for item in items:
            if item not in self.incoming:
                self.incoming.append(item)
            if self not in item.outgoing: # prevent inconsistencies
                item.outgoing.append(self)
    def append_outgoing(self, items):
        for item in items:
            if item not in self.outgoing:
                self.outgoing.append(item)
            if self not in item.incoming: # prevent inconsistencies
                item.incoming.append(self)

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

def create_network(G, nodes, probability, iterations, layout): # takes Graph G, int nodes, float probability, int iterations, and string layout
    sites = []
    supernode = Website("super", [], [])
    for i in range(nodes):
        site = Website(str(i), [], [])
        sites.append(site)
        G.add_node(site.name) # add nodes to graph visualization
    supernode.append_incoming(sites)
    supernode.append_outgoing(sites)
    for i in sites:
        G.add_edge("s",i.name) # add edges to graph visualization
    for site in sites:
        other_sites=sites[:]
        other_sites.remove(site)
        randomnum = random.random()
        if randomnum <= probability: # make the graphs look more diverse/customize how sparse it looks
            random_outgoing = random.sample(other_sites, k=random.randint(0, nodes-1))
            for i in random_outgoing:
                G.add_edge(site.name,i.name) # add edges to graph visualization
            site.append_outgoing(random_outgoing)
        site.append_incoming([supernode])
        site.append_outgoing([supernode])
    for site in sites: # mostly a debug feature but provides a textual representation of network
        print ("Name: %s" % site.name)
        for i in site.incoming:
            print("Incoming: %s" % i.name)
        for i in site.outgoing:
            print("Outgoing: %s" % i.name)
        print ("---------------")
    sites.append(supernode)
    initial_round = {}
    initial_score = 1/len(sites)
    for e in sites:
        initial_round.update({e.name:initial_score})
    # return [initial_round, supernode]

    rank = iterate(0.85, supernode, initial_round, iterations)
    clean_rank = rank
    for i in clean_rank.keys():
        clean_rank[i] = round(clean_rank[i],2)

    plt.title("Sparsity: %s, Count: %s, Iterations: %s, Layout: %s\n%s" % (sparsity,count,iterations,layout,json.dumps(rank)), wrap=True)

    if layout == "Random":
        pos=nx.random_layout(G) 
    elif layout == "Spectral":
        pos=nx.spectral_layout(G) # a significant amount of time was put into figuring out which layout looked best. this proved to be the most readable
    colors = ["#139ae8"] * nodes + ["#6cad50"] # make supernode readable
    nx.draw_networkx(G, arrows = True, pos=pos, node_color=colors) 



G=nx.DiGraph()
sparsity = 0.5
count = 10
iterations = 1000
layout = "Random" # Change to 'Spectral' for another (potentially more readable) view 
network = create_network(G,count,sparsity,iterations, layout)
# print (network[0])
# print (iterate(0.85, network[1], network[0], 1000))
# nx.draw_networkx(G, arrows = True)
plt.show()