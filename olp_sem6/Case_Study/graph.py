#Credits: My team members
from queue import PriorityQueue
from random import randint, uniform
from collections import defaultdict
import sys

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib import animation,rc

rc('animation', html='html5')

def random_node(NUM_NODES):
    return randint(1, NUM_NODES)

def define_graph(graph, NUM_NODES):
    n_flag = 1
    while (True):
        print('Node1:')
        while (n_flag == 1):
            node1 = int(input())
            if (abs(node1) > NUM_NODES):
                print("Out of range! Enter again.")
            else:
                n_flag = 0
        n_flag = 1
        print('Node2:')
        while (n_flag == 1):
            node2 = int(input())
            print('Edge weight:')
            if (abs(node2) > NUM_NODES):
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

def prims(NUM_NODES):
    pqueue = PriorityQueue()

    # Start at any random node and add all edges connected to this
    # node to the priority queue.
    start_node = random_node(NUM_NODES)
    for neighbor in graph.neighbors(start_node):
        edge_data = graph.get_edge_data(start_node, neighbor)
        edge_weight = edge_data["weight"]
        pqueue.put((edge_weight, (start_node, neighbor)))

    # Loop until all nodes are in the MST
    while len(nodes_on_mst) < NUM_NODES:
        # Get the edge with smallest weight from the priority queue
        _, edge = pqueue.get(pqueue)

        if edge[0] not in nodes_on_mst:
            new_node = edge[0]
        elif edge[1] not in nodes_on_mst:
            new_node = edge[1]
        else:
            # If this edge connects two nodes that are already in the
            # MST, then skip this and continue to the next edge in
            # the priority queue.
            continue

        # Every time a new node is added to the priority queue, add
        # all edges that it sits on to the priority queue.
        for neighbor in graph.neighbors(new_node):
            edge_data = graph.get_edge_data(new_node, neighbor)
            edge_weight = edge_data["weight"]
            pqueue.put((edge_weight, (new_node, neighbor)))

        # Add this edge to the MST.
        edges_in_mst.add(tuple(sorted(edge)))
        nodes_on_mst.add(new_node)

        # Yield edges in the MST to plot.
        yield edges_in_mst

#KRUSKAL's UTILITY FUNCTIONS
def getMin(G, mstFlag):
    min = sys.maxsize  # assigning largest numeric value to min
    for i in [(u, v, edata['weight']) for u, v, edata in G.edges(data=True) if 'weight' in edata]:
        if mstFlag[i] == False and i[2] <= min:
            min = i[2]
            min_edge = i
    #print("Min", min_edge)
    return min_edge


# A utility function to find root or origin of the node i in MST
def findRoot(parent, i):
    if parent[i] == i:
        return i
    return findRoot(parent, parent[i])


# A function that does union of set x and y based on the order
def union(parent, order, x, y):
    xRoot = findRoot(parent, x)
    yRoot = findRoot(parent, y)
    # Attach smaller order tree under root of high order tree
    if order[xRoot] < order[yRoot]:
        parent[xRoot] = yRoot
    elif order[xRoot] > order[yRoot]:
        parent[yRoot] = xRoot
    # If orders are same, then make any one as root and increment its order by one
    else:
        parent[yRoot] = xRoot
        order[xRoot] += 1

def kruskal(G,NUM_NODES):
    vLen = NUM_NODES  # vLen denotes the number of vertices in G
    mst = set()  # mst contains the MST edges
    mstFlag = {}  # mstFlag[i] will hold true if the edge i has been processed for MST
    for i in [(u, v, edata['weight']) for u, v, edata in G.edges(data=True) if 'weight' in edata]:
        mstFlag[i] = False
    parent = [None] * (vLen+1)  # parent[i] will hold the vertex connected to i, in the MST
    order = [None] * (vLen+1)  # order[i] will hold the order of appearance of the node in the MST
    for v in range(1,vLen+1):
        parent[v] = v
        order[v] = 0
    while len(mst) < NUM_NODES - 1:
        curr_edge = getMin(G, mstFlag)  # pick the smallest egde from the set of edges
        #print(curr_edge,mst)
        mstFlag[curr_edge] = True  # update the flag for the current edge
        y = findRoot(parent, curr_edge[1])
        x = findRoot(parent, curr_edge[0])
        # adds the edge to MST, if including it doesn't form a cycle
        if x != y:
            mst.add(tuple(curr_edge))
            union(parent, order, x, y)
            yield mst


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

if __name__=='__main__':
    print("Enter number of nodes")
    NUM_NODES = int(input())

    graph = nx.Graph()

    define_graph(graph,NUM_NODES)
    pos = nx.spring_layout(graph)
    #print(graph.nodes)

    all_edges = set(
        tuple(sorted((n1, n2))) for n1, n2 in graph.edges()
    )

    while(True):
        print("Enter <P> for Prim's Algorithm and <K> for Kruskal's Algorithm")
        choice = input()
        fig, ax = plt.subplots(figsize=(6, 4))
        if(choice == 'P'):
            edges_in_mst = set()
            nodes_on_mst = set()

            ani = animation.FuncAnimation(
                fig,
                update,
                init_func=do_nothing,
                frames=prims(NUM_NODES),
                interval=600,
            )
        elif(choice == 'K'):
            ani2 = animation.FuncAnimation(
                fig,
                update,
                init_func=do_nothing,
                frames=kruskal(graph,NUM_NODES),
                interval=600,
            )
        #plt.show()
        plt.draw()
        plt.pause(5)
        input("Press <ENTER> to close")  # this will wait for indefinite time
        plt.close(fig)
        exit = input("Press <X> to exit or any other key to try another algorithm.")
        if(exit=='X' or exit=='x'):
            break


