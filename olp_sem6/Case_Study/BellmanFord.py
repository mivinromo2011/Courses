#Credits: My team members
import networkx as nx
import matplotlib.pyplot as plt
import sys
from matplotlib import animation,rc

rc('animation', html='html5')

inf = sys.maxsize


def bellmanFord(G, source, pos):
    V = len(G.nodes())
    dist = []
    parent = [None] * V  # parent[i] will hold the node from which i is reached to, in the shortest path from source

    for i in range(V):
        dist.append(inf)

    parent[source] = -1;  # source is itself the root, and hence has no parent
    dist[source] = 0;
    for i in range(V - 1):
        for u, v, d in G.edges(data=True):  # Relaxation
            #print(dist[u] + d['weight'] < dist[v], u,v,d['weight'],dist[u],dist[v])
            if dist[u] + d['weight'] < dist[v]:  # Relaxation Equation
                #print(dist)
                dist[v] = d['weight'] + dist[u]
                parent[v] = u

    # marking the shortest path from source to each of the vertex with red, using parent[]
    for X in range(V):
        if parent[X] != -1:  # ignore the parent of root node
            if (parent[X], X) in G.edges():
                #print(spt_edges)
                spt_edges.add(tuple([parent[X], X, G[parent[X]][X]['weight']]))
    final = set()
    for e in spt_edges:
        final.add(e)
        print(final)
        yield final


# defines graph
def define_graph(graph, NUM_NODES):
    n_flag = 1
    while (True):
        print('Node1:')
        while (n_flag == 1):
            node1 = int(input())
            if (abs(node1) >= NUM_NODES):
                print("Out of range! Enter again.")
            else:
                n_flag = 0
        n_flag = 1
        print('Node2:')
        while (n_flag == 1):
            node2 = int(input())
            print('Edge weight:')
            if (abs(node2) >= NUM_NODES):
                print("Out of range! Enter again.")
            else:
                n_flag = 0
        n_flag = 1
        ew = int(input())
        graph.add_edge(node1, node2, weight=ew)
        print("Added!\nDo you want to add more?(Y/N)")
        response = input().lower()
        if (response == 'n'):
            break

def update(mst_edges):
    ax.clear()
    labels = nx.get_edge_attributes(graph,'weight')
    nodes ={}
    for node in graph.nodes():
        nodes[node] = node
    nx.draw_networkx_nodes(graph, pos, node_size=300, ax=ax, node_color="blue", linewidths=5)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    nx.draw_networkx_labels(graph, pos, nodes, font_color='white')
    nx.draw_networkx_edges(
        graph, pos, edgelist=all_edges-mst_edges, alpha=0.25,
        edge_color='blue', width=1, ax=ax
    )
    nx.draw_networkx_edges(
        graph, pos, edgelist=mst_edges, alpha=1.0,
        edge_color='red', width=1, ax=ax
    )

def do_nothing():
    # FuncAnimation requires an initialization function. We don't
    # do any initialization, so we provide a no-op function.
    pass

# main function
if __name__ == "__main__":
    print("Enter number of nodes")
    NUM_NODES = int(input())

    graph = nx.DiGraph()

    define_graph(graph, NUM_NODES)
    pos = nx.spring_layout(graph)
    fig, ax = plt.subplots(figsize=(6, 4))
    labels = nx.get_edge_attributes(graph, 'weight')
    all_edges = set(
        tuple((n1, n2)) for n1, n2 in graph.edges()
    )
    spt_edges= set()
    source = int(input("Enter source node\n"))
    ani = animation.FuncAnimation(
        fig,
        update,
        init_func=do_nothing,
        frames=bellmanFord(graph, source, pos),
        interval=1000,
    )
    plt.show()
