import json
from random import sample, randrange
from uuid import uuid4

def merge(a, b):
    if b['uuid'] not in a:
        a[b['uuid']] = b
        return

    if a[b['uuid']]['generation'] < b['generation']:
        a[b['uuid']] = b
        return

    return

def random_events(uuid, count, nodes):
    return [ {"uuid": uuid, "generation": x, "neighbors": sorted(sample(nodes, randrange(len(nodes))))} for x in range(count) ]

if __name__ == "__main__":
    all = {}
    count = 5
    ids = [ str(uuid4()) for x in range(count) ]
    events = [ item for id in ids for item in random_events(id, 5, [*range(count)]) ]

    for ev in events:
        merge(all, ev)

    print(json.dumps(events))
