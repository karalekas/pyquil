import networkx as nx
from . import Device
from ._specs import Specs
from ._isa import ISA, isa_from_graph, isa_from_digraph


def ibmq_ourense():
    graph = nx.from_edgelist([
        (0, 1), (1, 0),
        (1, 2), (2, 1),
        (1, 3), (3, 1),
        (3, 4), (4, 3)
    ])
    print(isa_from_digraph(graph, twoq_type='CNOT').to_dict())
    return Device(name="ibmq_ourense",
                  raw={"isa": isa_from_digraph(graph, twoq_type='CNOT').to_dict(),
                       "specs": Specs().to_dict()})


def ibmq_yorktown():
    graph = nx.from_edgelist([
        (0, 1), (0, 2),
        (1, 2), (3, 2),
        (3, 4), (4, 2)
    ])
    return isa_from_digraph(graph, twoq_type='CNOT')
