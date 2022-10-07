import os
import pathlib
from argparse import ArgumentParser

from gossip import GossipNode
from pycape import FunctionRef

# port = 5000
# # ports for the nodes connected to this node
# connected_nodes = [5010, 5020]

# node = GossipNode(port, connected_nodes)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", type=int, help="port")
    parser.add_argument("-n", "--node-list", nargs="+", default=[])
    args = vars(parser.parse_args())
    # print(args)
    function_json = os.environ.get("FUNCTION_JSON", "leader_election.json")
    function_json = pathlib.Path(__file__).parent.absolute() / function_json

    function_ref = FunctionRef.from_json(function_json)
    node = GossipNode(
        args["p"],
        connected_nodes=list(map(int, args["node_list"])),
        function_ref=function_ref,
    )
