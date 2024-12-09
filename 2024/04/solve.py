import unittest

def check_x_mas(area):
    if area[0][0] == "M" and area [0][2] == "M" and area[1][1] == "A" and area[2][2] == "S" and area [2][0] == "S" :
           return 1
    if area[0][0] == "S" and area [0][2] == "S" and area[1][1] == "A" and area[2][2] == "M" and area [2][0] == "M" :
           return 1
    if area[0][0] == "M" and area [2][0] == "M" and area[1][1] == "A" and area[2][2] == "S" and area [0][2] == "S" :
           return 1
    if area[0][0] == "S" and area [2][0] == "S" and area[1][1] == "A" and area[2][2] == "M" and area [0][2] == "M" :
           return 1
    return 0

def check_xmas_diagonal(area):
    count = 0
    if area[0][0] == "X" and area[1][1] == "M" and area[2][2] == "A" and area[3][3] == "S":
        count += 1
    if area[3][3] == "X" and area[2][2] == "M" and area[1][1] == "A" and area[0][0] == "S":
        count += 1
    if area[0][3] == "X" and area[1][2] == "M" and area[2][1] == "A" and area[3][0] == "S":
        count += 1
    if area[3][0] == "X" and area[2][1] == "M" and area[1][2] == "A" and area[0][3] == "S":
        count += 1 
    return count

def check_xmas_horizontal(area):
    if area[0] == "XMAS" or area[0] == "SAMX":
        return 1
    return 0

def check_xmas_vertical(area):
    count = 0
    if len(area) != 4:
        return 0
    if area[0][0] == "X" and area[1][0] == "M" and area[2][0] == "A" and area[3][0] == "S":
        count += 1
    if area[3][0] == "X" and area[2][0] == "M" and area[1][0] == "A" and area[0][0] == "S":
        count += 1
    return count

def check_xmas(area):
    """
    check for xmas in 4x4 area of text
    """
    count = 0

    "0123"
    "1..."
    "2..."
    "3..."
    return count

def parse(file_location):
    with open(file_location) as f:
        return f.readlines()

def extract(wordsearch, top, left, height, width):
    selection = []
    for i in range(height):
        selection.append(wordsearch[top+i][left:left+width])
    return selection


class TestXMAS(unittest.TestCase):

    def text_extract(self):
        all_xmas_backward =  ["SAMX","SAMX","SAMX","SAMX"]
        self.assertEqual(extract(all_xmas_backward,0,0,1,4),["XMAS"])

    def test_check_xmas_backward(self):
        all_xmas_backward =  ["SAMX","SAMX","SAMX","SAMX"]
        self.assertEqual(check_xmas_horizontal(all_xmas_backward),1)

    def test_check_xmas_forward(self):
        all_xmas_forward = ["XMAS","XMAS","XMAS","XMAS"]
        self.assertEqual(check_xmas_horizontal(all_xmas_forward),1)

    def test_check_xmas_vertical(self):
        all_xmas_vertical = ["XXXX",
                             "MMMM",
                             "AAAA",
                             "SSSS"]
        self.assertEqual(check_xmas_vertical(all_xmas_vertical),1)

    def test_check_xmas_upsidedown(self):
                             
        all_xmas_upsidedown = ["SSSS",
                               "AAAA",
                               "MMMM",
                               "XXXX"]
        self.assertEqual(check_xmas_vertical(all_xmas_upsidedown),1)

    def test_check_xmas_diagonal_backward(self):
        xmas_diagonal_backward =  ["SooX",
                                   "oAMo",
                                   "oAMo",
                                   "SooX"]
        self.assertEqual(check_xmas_diagonal(xmas_diagonal_backward),2)

    def test_check_xmas_diagonal_forward(self):
        xmas_diagonal_forward  =  ["XooS",
                                   "oMAo",
                                   "oMAo",
                                   "XooS"]
        self.assertEqual(check_xmas_diagonal(xmas_diagonal_forward),2)

    def test_check_x_mas(self):
        x_mas_1 = [ "MMM", "AAA", "SSS"]
        self.assertEqual(check_x_mas(x_mas_1), 1)
        x_mas_2 = [ "MAS", "MAS", "MAS"]
        self.assertEqual(check_x_mas(x_mas_2), 1)
        x_mas_3 = ["SAM"]*3
        self.assertEqual(check_x_mas(x_mas_3), 1)
        x_mas_4 = ["SSS","AAA","MMM"]
        self.assertEqual(check_x_mas(x_mas_4), 1)

def main():
    wordsearch = parse('input.txt')
    width = len(wordsearch[0])
    height = len(wordsearch)
    print(f' searching \nwidth: {width} \nheight: {height}')
    total = 0
    total_xmas = 0
    for i in range(width):
        for j in range(height):
            if i < width - 3:
                found = check_xmas_horizontal(extract(wordsearch,j,i,1,4))
                if found > 0:
                    print(f'found horizontal at {i},{j}')
                    total+=found
            if j < height - 3 :
                found = check_xmas_vertical(extract(wordsearch,j,i,4,1))
                if found > 0:
                    print(f'found vertical at {i},{j}')
                    total+=found
            if i < width - 3 and j < height - 3:
                found = check_xmas_diagonal(extract(wordsearch,j,i,4,5))
                if found > 0:
                    print(f'found diagonal at {i},{j}')
                    total+=found
            if i < width - 2 and j < height - 2:
                total_xmas += check_x_mas(extract(wordsearch,j,i,3,4))
    print(total)
    print(total_xmas)


if __name__ == "__main__":
    main()

