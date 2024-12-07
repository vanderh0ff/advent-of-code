import unittest


def check_xmas(area):
    """
    check for xmas in 4x4 area of text
    """
    count = 0
    "0123"
    "1..."
    "2..."
    "3..."
    for i in range(4):
        if area[i] == "XMAS" or area[i] == "SAMX":
            count += 1
        if area[0][i] == "X" and area[1][i] == "M" and area[2][i] == "A" and area[3][i] == "S":
            count += 1
        if area[3][i] == "X" and area[2][i] == "M" and area[1][i] == "A" and area[0][i] == "S":
            count += 1
    if area[0][0] == "X" and area[1][1] == "M" and area[2][2] == "A" and area[3][3] == "S":
        count += 1
    if area[3][3] == "X" and area[2][2] == "M" and area[1][1] == "A" and area[0][0] == "S":
        count += 1
    if area[0][3] == "X" and area[1][2] == "M" and area[2][1] == "A" and area[3][0] == "S":
        count += 1
    if area[3][0] == "X" and area[2][1] == "M" and area[1][2] == "A" and area[0][3] == "S":
        count += 1 
    return count

def parse(file_location):
    with open(file_location) as f:
        return f.readlines()

def extract(wordsearch, top, left):
    selection = []
    for i in range(4):
        selection.append(wordsearch[top+i][left:left+4])
    print(selection)
    return selection


class TestXMAS(unittest.TestCase):

    def test_check_xmas_backward(self):
        all_xmas_backward =  ["SAMX","SAMX","SAMX","SAMX"]
        self.assertEqual(check_xmas(all_xmas_backward),6)

    def test_check_xmas_forward(self):
        all_xmas_forward = ["XMAS","XMAS","XMAS","XMAS"]
        self.assertEqual(check_xmas(all_xmas_forward),6)

    def test_check_xmas_vertical(self):
        all_xmas_vertical = ["XXXX",
                             "MMMM",
                             "AAAA",
                             "SSSS"]
        self.assertEqual(check_xmas(all_xmas_vertical),6)

    def test_check_xmas_upsidedown(self):
                             
        all_xmas_upsidedown = ["SSSS",
                               "AAAA",
                               "MMMM",
                               "XXXX"]
        self.assertEqual(check_xmas(all_xmas_upsidedown),6)

    def test_check_xmas_diagonal_backward(self):
        xmas_diagonal_backward =  ["SooX",
                                   "oAMo",
                                   "oAMo",
                                   "SooX"]
        self.assertEqual(check_xmas(xmas_diagonal_backward),2)

    def test_check_xmas_diagonal_forward(self):
        xmas_diagonal_forward  =  ["XooS",
                                   "oMAo",
                                   "oMAo",
                                   "XooS"]
        self.assertEqual(check_xmas(xmas_diagonal_forward),2)

def main():
    wordsearch = parse('test.txt')
    width = len(wordsearch[0])
    height = len(wordsearch)
    total = 0
    for i in range(width - 4):
        for j in range(height - 4):
            total += check_xmas(extract(wordsearch,i,j))
    print(total)


if __name__ == "__main__":
    main()

