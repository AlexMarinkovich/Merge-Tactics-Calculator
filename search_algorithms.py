def generate_connected_subgraphs(graph: dict[object, set], k: int):
    """Enumerate all induced connected subgraphs of size `k` from adjacency list `graph`."""
    def backtrack(unvisited: set, subgraph: list, neighbours: set):
        if len(subgraph) == k:
            yield tuple(subgraph)
            return
        
        # Determine a candidate to explore next
        candidates = unvisited & neighbours if subgraph else unvisited
        if not candidates: return
        v = next(iter(candidates))
        unvisited.remove(v)
        
        # Case 1: Exclude v
        yield from backtrack(unvisited, subgraph, neighbours)

        # Case 2: Include v
        subgraph.append(v)
        yield from backtrack(unvisited, subgraph, neighbours | graph[v])
        subgraph.pop()

        # Backtrack
        unvisited.add(v)
        
    yield from backtrack(set(graph.keys()), [], set())

# ---------- EVERYTHING BELOW IS FOR TESTING ----------

if __name__ == "__main__":
    import itertools
    from troops import Troop
    from collections import defaultdict, Counter
    import time
    from teams import Team

    def is_connected(subgraph, graph):
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour in subgraph and neighbour not in visited:
                    dfs(neighbour)
        dfs(subgraph[0])
        return len(visited) == len(subgraph)

    def naive_generate_subgraphs(graph, k):
        return [c for c in itertools.combinations(graph.keys(), k) if is_connected(c, graph)]

    k = 7
    troop_graph = defaultdict(set)
    for t1 in Troop.all_troops:
        for t2 in Troop.all_troops:
            if t1 == t2: continue
            if {t1.trait1, t1.trait2} & {t2.trait1, t2.trait2}:
                troop_graph[t1].add(t2)
                troop_graph[t2].add(t1)

    start = time.time()
    result = list(generate_connected_subgraphs(troop_graph, k))
    print(f"{time.time() - start:.6f} seconds - Generating subgraphs ({len(result)})")

    start = time.time()
    naive_result = naive_generate_subgraphs(troop_graph, k)
    print(f"{time.time() - start:.6f} seconds - Naive subgraphs ({len(naive_result)})")

    start = time.time()
    combinations = list(itertools.combinations(Troop.all_troops, k))
    print(f"{time.time() - start:.6f} seconds - Itertools combinations ({len(combinations)})")

    start = time.time()
    troop_selection = list(Troop.all_troops)[0:k]
    for i in range(len(combinations)):
        _ = Team(troop_selection, None)
    print(f"{time.time() - start:.6f} seconds - Making team objects ({len(combinations)})")

    # Verify correctness of generate_connected_subgraphs
    print(Counter(frozenset(i) for i in naive_result) == Counter(frozenset(i) for i in result))