from collections import defaultdict
import pydot

words = ["Mark", "Kelly", "Kurt", "Terk"]

def main():
    # get first -> last letter transitions
    nodes = set()
    arcs = defaultdict(lambda: defaultdict(list))
    for word in words:
        first = word[0]
        last = word[-1]        
        nodes.add(first)
        nodes.add(last)
        arcs[first][last].append(word)

    # create a graph
    graph = pydot.Dot("Word_combinations", graph_type="digraph")
    # use letters as nodes
    for node in sorted(nodes):
        n = pydot.Node(node, shape="circle")
        graph.add_node(n)
    # use first-last as directed edges
    for first, sub in arcs.items():
        for last, wordlist in sub.items():
            count = len(wordlist)
            label = str(count) if count > 1 else ""
            e = pydot.Edge(first, last, label=label)
            graph.add_edge(e)

    # save result
    graph.set_prog("dot")
    #graph.set_shape_files("wordgraph.png")
    graph.write("wordgraph.png", prog='dot', format='png')
    #graph.write_png(, prog="dot")

if __name__=="__main__":
    main()