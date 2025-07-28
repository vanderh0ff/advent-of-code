from collections import defaultdict, deque
import unittest

def parse(file_location):
    ordering_rules = defaultdict(list)
    pre_rules = defaultdict(list)
    page_updates = []

    with open(file_location) as f:
        for line in f.readlines():
            if "|" in line:
                pre, post = list(map(int,line.split("|")))
                ordering_rules[post].append(pre)
                pre_rules[pre].append(post)
            if "," in line:
                page_updates.append(list(map(int,line.split(","))))

    return ordering_rules, pre_rules, page_updates

def topo_sort_khan(graph):
    in_degree = defaultdict(int)
    nodes = set()
    # calculate the in degree of each node
    for u in graph:
        nodes.add(u)
        for v in graph[u]:
            in_degree[v] += 1
            nodes.add(v)

    for node in nodes:
        if node not in in_degree:
            in_degree[node] = 0

    print(in_degree)
    queue = deque()
    topological_order = []
    processed_count = 0

    # start with leaf nodes in the graph
    for node in nodes:
        if in_degree[node] == 0:
            queue.append(node)

    # remove leaf from graph, decrement in count of parent nodes
    while queue:
        u = queue.popleft()
        topological_order.append(u)
        processed_count += 1

        for v in graph[u]:
            in_degree[v] -= 1
            # if node is now a leaf add to queue 
            if in_degree[v] == 0:
                queue.append(v)

    return topological_order

def validate_line(ordering_rules, page_update):
    invalid_pages = set()
    for page in page_update:
        for rule in ordering_rules[page]:
            invalid_pages.add(rule)
        if page in invalid_pages:
            return False
    return True

def sort_line(ordering_rules, page_update):
    order = []
    page_set = set(page_update)
    while len(page_set) > 0:
        for page in page_set:
            if len(set(ordering_rules[page]).intersection(page_set)) == 0:
                order.append(page)
                page_set.remove(page)
                break
    return order

def sum_valid_middle(file_location):
    ordering_rules, pre_rules, page_updates = parse(file_location)
    total = 0
    for page_update in page_updates:
        if validate_line(ordering_rules, page_update):
            total += page_update[len(page_update)//2]
    return total

def sum_invalid_middle(file_location):
    ordering_rules, pre_rules, page_updates = parse(file_location)
    total = 0
    for page_update in page_updates:
        if not validate_line(ordering_rules, page_update):
            page_update = sort_line(ordering_rules, page_update)
            total += page_update[len(page_update)//2]
    return total

# we add each pre page to the list of pages keyed by post page to a set of  pages to check againsst
# then as we go throught items in the page update list we can see if any of the pages in the set are present 
# if the pages are present then the pages are out of order
# we build the set and scan in linear time 

class TestPrinter(unittest.TestCase):
    def test_parsing(self):
        self.assertEqual(parse('unittest.txt'),(defaultdict(list,{5:[4],7:[4]}),defaultdict(list,{4:[5,7]}),[[4,6,7]]))

    def test_scanning(self):
        ordering_rules, pre_rules, page_updates = parse('unittest.txt')
        self.assertEqual((ordering_rules, page_updates),(defaultdict(list,{5:[4],7:[4]}),[[4,6,7]]))
        self.assertEqual(validate_line(ordering_rules, [4]),True)
        self.assertEqual(validate_line(ordering_rules, [4, 5]),True)
        self.assertEqual(validate_line(ordering_rules, [5, 4]),False)

    def test_valid_middle(self):
        self.assertEqual(sum_valid_middle('sample.txt'),143)


if __name__ == "__main__":
    #print(sum_valid_middle('input.txt'))
    print(sum_invalid_middle('input.txt'))

