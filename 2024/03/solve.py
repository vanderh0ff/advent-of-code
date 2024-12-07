import re

def parse(file_location):
    with open(file_location) as f:
        return f.read()

def part1():
    input = parse("input.txt")
    mul = re.compile(r'mul\((\d+),(\d+)\)')
    return sum(map(lambda x: int(x[0]) * int(x[1]),mul.findall(input)))

def part2():
    input = parse("input.txt")
    mul = re.compile(r'(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))')
    enabled = True
    total = 0
    for match in mul.findall(input):
        if match[0][0] == 'm' and enabled:
            total += int(match[1])*int(match[2])
        elif match[0] == 'do()':
            enabled = True
        else:
            enabled = False
    return total



    #return sum(map(lambda x: int(x[0]) * int(x[1]),mul.findall(input)))

def main():
    print(part1())
    print(part2())
    



if __name__ == "__main__":
    main()
