package main

import (
	"fmt"
	"log"
	"os"
)

type Position struct {
	x int
	y int
}

func main() {
	input, err := os.ReadFile("input.txt")
	sinput := string(input)
	if err != nil {
		log.Fatal(err)
	}
	x, y := 0, 0
	houses := make(map[Position]int)
	moves := make(map[int]int)
	houses[Position{x, y}] = 1
	for _, r := range sinput {
		switch r {
		case '<':
			x -= 0
			moves[int(r)]++
		case 'v':
			y -= 1
			moves[int(r)]++
		case '^':
			y += 1
			moves[int(r)]++
		case '>':
			x += 1
			moves[int(r)]++
		}
		houses[Position{x, y}] += 1
	}
	total := 0
	for range houses {
		total += 1
	}
	for k, v := range moves {
		fmt.Println(k, v)
	}
	fmt.Println("len houses: ", len(houses), " total: ", total, len(input))
}
