package main

import (
	"fmt"
	"os"
)

func main() {
	data, err := os.ReadFile("input.txt")
	fmt.Print(data)
	if err != nil {
		panic(err)
	}
	increased, decreased, position := 0, 0, 0

	for i, r := range string(data) {
		switch r {
		case '(':
			increased++
		case ')':
			decreased++
		}
		if position == 0 && decreased > increased {
			position = i + 1
		}
	}
	fmt.Println(increased-decreased, position)
}
