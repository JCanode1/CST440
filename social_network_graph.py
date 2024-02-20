import networkx as nx
import matplotlib.pyplot as plt
import mpld3


def main(dataset_path):
    with open(dataset_path, 'r', encoding='iso-8859-1') as file:
        lines = file.readlines()

    # Create Graph instance
    G = nx.Graph()

    # Parse the data and add edges to the graph
    for line in lines[3:]:  # Skipping the first three metadata and header lines
        parts = line.strip().split('\t')
        if len(parts) >= 3:
            node1, node2, cost = parts
            G.add_edge(int(node1), int(node2), weight=int(cost))

    # Draw the network graph
    fig, ax = plt.subplots(figsize=(30, 30))
    nx.draw(G, ax=ax, with_labels=True, node_size=50, font_size=8)
    plt.title("Social Network Graph")

    # Save the mpld3 interactive plot to an HTML file
    mpld3.save_html(fig, "social_network_graph.html")
    print("Interactive graph saved to social_network_graph.html")

    # Graph's structure summary
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    print(f"Graph Summary:\n- Number of Nodes: {num_nodes}\n- Number of Edges: {num_edges}")


if __name__ == "__main__":
    dataset_path = './inst_v200_s1.dat'
    main(dataset_path)
