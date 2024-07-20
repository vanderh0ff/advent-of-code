package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
)

func readInput() ([][]byte, error) {
	f, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	var strings [][]byte

	start := 0
	for i, v := range f {
		if v == '\n' {
			strings = append(strings, f[start:i])
			start = i + 1
		}
	}
	return strings, err

}

func checkRepeats(b []byte) bool {
	prev := b[0]
	for i := 1; i < len(b); i++ {
		if b[i] == prev {
			return true
		}
		prev = b[i]
	}
	return false
}

func checkDoubleDoubles(b []byte) bool {
	for i := 0; i < len(b)-3; i++ {
		for j := i + 2; j < len(b)-1; j++ {
			if b[i] == b[j] && b[i+1] == b[j+1] {
				return true
			}
		}
	}
	return false
}

func checkSurrounded(b []byte) bool {
	for i := 0; i < len(b)-2; i++ {
		if b[i] == b[i+2] {
			return true
		}
	}
	return false
}

func main() {
	strings, err := readInput()
	if err != nil {
		log.Fatal(err)
	}
	checkThreeVowels, err := regexp.Compile("[aeiou].*[aeiou].*[aeiou]")
	if err != nil {
		log.Fatal(err)
	}
	checkBannedSequence, err := regexp.Compile("(ab|cd|pq|xy)")
	if err != nil {
		log.Fatal(err)
	}
	good1 := 0
	good2 := 0
	for v := range strings {
		if !checkBannedSequence.Match(strings[v]) && checkThreeVowels.Match(strings[v]) && checkRepeats(strings[v]) {
			good1++
		}
		if checkDoubleDoubles(strings[v]) && checkSurrounded(strings[v]) {
			good2++
		}
	}
	fmt.Println("part 1: ", good1)
	fmt.Println("part 2: ", good2)

}
