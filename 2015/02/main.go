package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	L = 0
	W = 1
	H = 2
)

func parseDimmensions(line string) (int, int, int, error) {
	measurements := strings.Split(line, "x")
	length, err := strconv.Atoi(measurements[L])
	if err != nil {
		log.Fatal(err)
		return 0, 0, 0, err
	}
	width, err := strconv.Atoi(measurements[W])
	if err != nil {
		log.Fatal(err)
		return 0, 0, 0, err
	}
	height, err := strconv.Atoi(measurements[H])
	if err != nil {
		log.Fatal(err)
		return 0, 0, 0, err
	}
	return length, width, height, nil
}

func getTotalWrappingPapperNeeded(width int, length int, height int) int {
	side1 := length * width
	side2 := width * height
	side3 := height * length
	slack := min(side1,side2,side3)
	total := (side1 + side2 + side3)*2 + slack
	return total
}

func getTotalRibbonNeeded(width int, length int, height int) int {
	sides := []int{width,length,height}
	sort.Ints(sides)
	return sides[0] * 2 + sides[1] * 2 + sides[0]*sides[1]*sides[2]
}

func main() {
	data, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer data.Close()
	scanner     := bufio.NewScanner(data)
	totalPaper  := 0
	totalRibbon := 0
	for scanner.Scan() {
		line := scanner.Text()
		length, width, height, err := parseDimmensions(line)
		if err != nil {
			log.Fatal(err)
		}
		totalPaper += getTotalWrappingPapperNeeded(length, width, height)
		totalRibbon += getTotalRibbonNeeded(length,width,height)
	}
	fmt.Println("Total wrapping paper area needed: ", totalPaper)
	fmt.Println("Total Ribbon needed: ", totalRibbon)
}
