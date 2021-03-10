#Credits: My team members
import networkx as nx
import matplotlib.pyplot as plt
import sys
from matplotlib import animation,rc

rc('animation', html='html5')


# utility function that returns the minimum distance node
def minDistance(dist, sptSet, V):
    min = sys.maxsize  # assigning largest numeric value to min
    for v in range(V):
        if sptSet[v] == False and dist[v] <= min:
            min = dist[v]
            min_index = v
    return min_index


# function that performs dijsktras algorithm
def dijsktras(G, source, pos):
    V = len(G.nodes())
    dist = []
    parent = [None] * V  # parent[i] will hold the node from which i is reached to, in the shortest path from source
    sptSet = []  # sptSet[i] will hold true if vertex i is included in shortest path tree
    # initially, for every node, dist[] is set to maximum value and sptSet[] is set to False
    for i in range(V):
        dist.append(sys.maxsize)
        sptSet.append(False)
    dist[source] = 0
    parent[source] = -1  # source is itself the root, and hence has no parent
    for count in range(V - 1):
        u = minDistance(dist, sptSet, V)  # pick the minimum distance vertex from the set of vertices
        sptSet[u] = True
        # update the vertices adjacent to the picked vertex
        for v in range(V):
            if (u, v) in G.edges():
                if sptSet[v] == False and dist[u] != sys.maxsize and dist[u] + G[u][v]['weight'] < dist[v]:
                    dist[v] = dist[u] + G[u][v]['weight']
                    parent[v] = u
    # marking the shortest path from source to each of the vertex with red, using parent[]
    for X in range(V):
        if parent[X] != -1:  # ignore the parent of root node
            if (parent[X], X) in G.edges():
                print(spt_edges)
                spt_edges.add(tuple([parent[X],X,G[parent[X]][X]['weight']]))
                #nx.draw_networkx_edges(G, pos, edgelist=[(parent[X], X)], width=2.5, alpha=1, edge_color='red')
                #yield spt_edges
    final = set()
    for e in spt_edges:
        final.add(e)
        yield final
    #return


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
    #print("Updated",mst_edges)
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

    graph = nx.Graph()

    define_graph(graph, NUM_NODES)
    pos = nx.spring_layout(graph)
    fig, ax = plt.subplots(figsize=(6, 4))
    labels = nx.get_edge_attributes(graph, 'weight')
    all_edges = set(
        tuple(sorted((n1, n2))) for n1, n2 in graph.edges()
    )
    spt_edges = set()
    source = int(input("Enter source node\n"))
    ani = animation.FuncAnimation(
        fig,
        update,
        init_func=do_nothing,
        frames=dijsktras(graph,source,pos),
        interval=1000,
    )
    #dijsktras(graph, source, pos)
    plt.show()