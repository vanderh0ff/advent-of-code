class guard():
    vectors = [ (0,-1), (1,0), (0,1), (-1,0) ]

    def __init__(self, position, vector):
        self.position = position
        self.vector = vector

    def rotate(self):
        self.vector = guard.vectors[(guard.vectors.index(self.vector)+1)%len(guard.vectors)]

    def move(self):
        self.position = tuple([sum(x) for x in zip(self.position, self.vector)])


    def update(self, m):
        next_space = m.get([sum(x) for x in zip(self.position ,self.vector)])
        match next_space:
            case '.':
                self.move()
                return True
            case '#':
                self.rotate()
                return True
            case _:
                return False


class map():
    def load(self, file_location):
        self.obsticles = []
        self.data = None
        with open(file_location) as f:
            lines = f.readlines()
            for y in range(len(lines)):
                lines[y] = list(lines[y][:-1])
                for x in range(len(lines[y])):
                    match lines[y][x]:
                        case '.':
                            continue
                        case '#':
                            self.obsticles.append((x,y))
                        case '<':
                            self.guard = guard((x,y),(-1,0))
                            lines[y][x] = '.'
                        case '>':
                            self.guard = guard((x,y),(1,0))
                            lines[y][x] = '.'
                        case '^':
                            self.guard = guard((x,y),(0,-1))
                            lines[y][x] = '.'
                        case 'v':
                            self.guard = guard((x,y),(0,1))
                            lines[y][x] = '.'
                        case _:
                            continue
            return lines

    def get(self, location):
        x, y = location
        if 0 <= x < len(self.data[0]) and 0 <= y < len(self.data): 
            return self.data[y][x]
        else:
            return '@'

    def print_walked(self, walked=set()):
        for y in range(len(self.data)):
            line = []
            for x in range(len(self.data[y])):
                if (x,y) in walked:
                    line.append('X')
                else:
                    line.append(self.data[y][x])
            print("".join(line))
                    
        
    def __init__(self, file_location):
        self.data = self.load(file_location) 

    def walk(self):
        walked = set()
        walked.add(self.guard.position)
        while self.guard.update(self):
            walked.add(self.guard.position)
        return len(walked)

m = map('input.txt')
print(m.walk())
