import networkx as nx
from matplotlib import pyplot as plot

templates = {
    "1": {
        "name": "Square",
        "edges": {
            ("A", "B"),
            ("A", "C"),
            ("B", "D"), 
            ("C", "D"),
        },

        "pos": {
               # col row
            "A": (0, 0),
            "B": (1, 0),
            "C": (0, 1),
            "D": (1, 1),
        }
    },

    "2": {
        "name": "Triangle",
        "edges": {
            ("A", "B"),
            ("A", "C"),
            ("B", "C"), 
        },

        "pos": {
               # col row
            "A": (1, 0),
            "B": (0, -1),
            "C": (2, -1),
        }
    },

    "3": {
        "name": "Star",
        "edges": {
            ("A", "B"),
            ("A", "C"),
            ("A", "D"), 
            ("A", "E"), 
        },

        "pos": {
               # col row
            "A": (0, 0),
            "B": (1, 1),
            "C": (1, -1),
            "D": (-1, -1),
            "E": (-1, 1),
        }
    },

    "4": {
        "name": "parallelogram",
        "edges": {
            ("A", "B"),
            ("A", "C"),
            ("B", "D"), 
            ("C", "D"), 
        },

        "pos": {
               # col row
            "A": (0, 0),
            "B": (1.4, 0),
            "C": (-0.4, -0.5),
            "D": (1, -0.5),
        }
    },

    "5": {
        "name": "Heart",
        "edges": {
            ("A", "B"),
            ("B", "C"),
            ("C", "D"), 
            ("D", "E"), 
            ("E", "F"), 
            ("F", "A"), 
        },

        "pos": {
               # col row
            "A": (-1.5, 3),
            "B": (-1, 3),
            "C": (0, 2.5),
            "D": (1, 3),
            "E": (1.5, 3),
            "F": (0, 1),
        }
    },

    "6": {
        "name": "semicircle",
        "edges": {
            ("A", "B"),
            ("B", "C"),
            ("C", "D"), 
            ("D", "E"), 
            ("E", "F"), 
            ("F", "G"), 
        },

        "pos": {
           # col row
            "A": (0.0, 0.77),
            "B": (0.2, 0.44),
            "C": (0.3, 0.22),
            "D": (0.35, 0.0),
            "E": (0.3, -0.22),
            "F": (0.2, -0.44),
            "G": (0.0, -0.77),
        }
    },
}

grap = nx.Graph()

choice = input("choice template: (1..6): ")

if choice in templates:
    print(f"{templates[choice]["name"]}")
    graph = nx.Graph()
    graph.add_edges_from(templates[choice]["edges"])

    nx.draw(graph, templates[choice]["pos"], with_labels=True)

    plot.xlim(-1, 2)     # left, right
    plot.ylim(-1, 1)     # bottom, top
    plot.axis("equal")   # same scale for x and y
    plot.tight_layout()  # reduce extra whitespace

    plot.show()
