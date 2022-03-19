# Girvan-Newman Algorithm (Community Detection)

# 1. For every edge in a graph, calculate the edge betweennes centrality (edge_betweenness_centrality)
# EBC - the number of the shortest paths that pass through an edge
# Each edge is given an EBC score based on the shortest paths among all the nodes in the graphs
# 2. Remove the edge with the highest betweenness centrality
# 3. Calculate the betweennes centrality for every remaining edge
# 4. Repeat steps 2-4 until there are no more edges left


import networkx as nx


# the function that reads a graph in gml format
# input: file
# output: the graph
def ReadNetwork(file):
    G = nx.read_gml(file, label='id')
    return G


# the function that returns the edget to delete from the graph
# input: graph
# output: edge() - tuple
def EdgetToDelete(graph):
    # EBC - numarul celor mai scurte drumuri care trec printr-o muchie  a grafului
    # (1,2): EBC
    graph_dict = nx.edge_betweenness_centrality(graph)
    # edge (a;b) - tuple
    edge_to_delete = ()

    # extract the edge with highest edge betweenness centrality score
    # sortez descrescator muchiile dupa EBC
    graph_dict = sorted(graph_dict.items(), key=lambda item: item[1], reverse=True)
    for key, val in graph_dict:
        edge_to_delete = key
        break

    return edge_to_delete


# Girvan-Newman Algorithm to determine divide a graph in no_communities given
# input: graph, no_communities
# output: the given graph divided in no_communities communities
# complexity: O(m^2*n), O(n^3) - sparse graph
def GirvanNewman(graph, no_communities):
    # the number of connected components
    comm_no = nx.number_connected_components(graph)

    while comm_no != no_communities:
        # iau muchia de eliminat
        edge = EdgetToDelete(graph)
        # varful1 al muchiei de eliminat
        vertex1 = edge[0]
        # varful2 al muchiei de eliminat
        vertex2 = edge[1]
        # sterg muchia cu highest betweennes centrality
        graph.remove_edge(vertex1, vertex2)
        # sg = nx.connected_components(graph)
        # print("connected components = ")
        # print((list(sg)))
        comm_no = nx.number_connected_components(graph)

    return nx.connected_components(graph)


# sort a dict by key
# input: dictionary
# output: sorted dictionary
def sor_dic_key(diction):
    lista = []
    diction2 = {}
    for x in diction:
        lista.append([x, diction[x]])
    lista.sort(key=lambda x: x[0])
    for l in lista:
        diction2[l[0]] = l[1]
    return diction2


# the function that finds the nodes forming the communities
# input: com - the list with the community distribution
# output: vertex, comm - the nodes distribution in n communities
def communityDistribution(com):
    vertex = []
    # ex. [1,2,3,1,1]
    communities = {}
    k = 0

    for item in com:
        k = k + 1
        vertex.append(list(item))
        for y in list(item):
            communities[y] = k

    communities = sor_dic_key(communities)
    comm = []

    for item in communities.values():
        comm.append(item)

    return list(vertex), comm


#  #  #                  TESTS                   #  #   #

# test Karate
file_karate = "data//real//karate//karate.gml"
G_karate = ReadNetwork(file_karate)
print("Karate Graph: ")
print(len(G_karate.nodes))
print(len(G_karate.edges))

# testDolphins
file_dolphins = "data//real//dolphins//dolphins.gml"
G_dolphins = ReadNetwork(file_dolphins)
print("Dolphins Graph: ")
print(len(G_dolphins.nodes))
print(len(G_dolphins.edges))

# # testFootball
# file_football = "data//real//football//football.gml"
# G = read_graph(file_football)
# print(len(G.nodes))
# print(len(G.edges))
#
# test krebs
file_krebs = "data//real//krebs//krebs.gml"
G_krebs = ReadNetwork(file_krebs)
print("Krebs Graph: ")
print(len(G_krebs.nodes))
print(len(G_krebs.edges))

# test barbell
G_barbell = nx.barbell_graph(5, 0)
print("Barbell Graph: ")
print(len(G_barbell.nodes))
print(len(G_barbell.edges))

# test lollipop
G_lollipop = nx.lollipop_graph(10, 20)
print("Lollipop Graph: ")
print(len(G_lollipop.nodes))
print(len(G_lollipop.edges))

# test barabasi_albert
G_barabasi_albert = nx.barabasi_albert_graph(5, 4)
print("Lollipop Graph: ")
print(len(G_barabasi_albert.nodes))
print(len(G_barabasi_albert.edges))

# # find communities in the graph
c_karate = GirvanNewman(G_karate.copy(), 3)
c_dolphins = GirvanNewman(G_dolphins.copy(), 3)
# # c_football = girvan_newman(G_football.copy())
c_krebs = GirvanNewman(G_krebs.copy(), 3)
c_barbell = GirvanNewman(G_barbell, 4)
c_lollipop = GirvanNewman(G_lollipop, 2)
c_barabasi_albert = GirvanNewman(G_barabasi_albert, 3)

#  #  #                  TESTS                   #  #   #


print("Node groups Karate Graph:")
vertex_distr, communities = communityDistribution(c_karate)
print("nodes distribution:")
print(vertex_distr)
print(communities)
#
print("Node groups Dolphins Graph:")
vertex_distr, communities = communityDistribution(c_dolphins)
print("nodes distribution:")
print(vertex_distr)
print(communities)
#
print("Node groups Krebs Graph:")
vertex_distr, communities = communityDistribution(c_krebs)
print("nodes distribution:")
print(vertex_distr)
print(communities)

# 3 new graphs
print("Node groups Barbell Graph:")
vertex_distr, communities = communityDistribution(c_barbell)
print("nodes distribution:")
print(vertex_distr)
print(communities)

print("Node groups Lollipop Graph:")
vertex_distr, communities = communityDistribution(c_lollipop)
print("nodes distribution:")
print(vertex_distr)
print(communities)

print("Node groups Barabasi Albert Graph:")
vertex_distr, communities = communityDistribution(c_barabasi_albert)
print("nodes distribution:")
print(vertex_distr)
print(communities)
