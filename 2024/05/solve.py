from collections import defaultdict
import unittest

def parse(file_location):
    ordering_rules = defaultdict(list)
    page_updates = []

    with open(file_location) as f:
        for line in f.readlines():
            if "|" in line:
                pre, post = list(map(int,line.split("|")))
                ordering_rules[post].append(pre)
            if "," in line:
                page_updates.append(list(map(int,line.split(","))))
    return ordering_rules, page_updates

def validate_line(ordering_rules, page_update):
    invalid_pages = set()
    for page in page_update:
        for rule in ordering_rules[page]:
            invalid_pages.add(rule)
        if page in invalid_pages:
            return False
    return True

def sum_valid_middle(file_location):
    ordering_rules, page_updates = parse(file_location)
    total = 0
    for page_update in page_updates:
        if validate_line(ordering_rules, page_update):
            total += page_update[len(page_update)//2]
    return total

def fix_invalid_page(ordering_rules, page_update):
    all_mentions = [k,v for k,v in ordering_rules.items()]
    possible = set(page_updates) - all_mentions
    print(possible)


    # given a list of nodes build an adj graph and find node with least edges and that will be end of list
    # then keep popping off least edges in nodes?


def sum_invalid_middle(file_location):
    ordering_rules, page_updates = parse(file_location)
    total = 0
    for page_update in page_updates:
        if not validate_line(ordering_rules, page_update):
            fix_invalid_page(ordering_rules, page_update)
    return total


# we add each pre page to the list of pages keyed by post page to a set of  pages to check againsst
# then as we go throught items in the page update list we can see if any of the pages in the set are present 
# if the pages are present then the pages are out of order
# we build the set and scan in linear time 


class TestPrinter(unittest.TestCase):
    def test_parsing(self):
        self.assertEqual(parse('unittest.txt'),(defaultdict(list,{5:[4],7:[4]}),[[4,6,7]]))

    def test_scanning(self):
        ordering_rules, page_updates = parse('unittest.txt')
        self.assertEqual((ordering_rules, page_updates),(defaultdict(list,{5:[4],7:[4]}),[[4,6,7]]))
        self.assertEqual(validate_line(ordering_rules, [4]),True)
        self.assertEqual(validate_line(ordering_rules, [4, 5]),True)
        self.assertEqual(validate_line(ordering_rules, [5, 4]),False)

    def test_valid_middle(self):
        self.assertEqual(sum_valid_middle('sample.txt'),143)


if __name__ == "__main__":
    print(sum_valid_middle('input.txt'))
    print(sum_invalid_middle('input.txt'))

