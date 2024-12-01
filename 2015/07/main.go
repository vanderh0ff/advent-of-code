package main

import (
	"log"
	"os"
)

const (
	assignment = "->"
	xor        = "XOR"
	rshift     = "RSHIFT"
	lshift     = "LSHIFT"
	or         = "OR"
	and        = "AND"
	not        = "NOT"
)

type instruction struct {
	source          string
	sourceIsLiteral bool
	operation       string
	arg             string
	destinaton      string
}

func parseNextToken(line []byte, start int) (string, int) {
	var token string
	for i := start; i < len(line); i++ {
		if line[i] == ' ' {
			token = string(line[start:i])
			return token, i
		}
	}
	return token, -1
}

func parseLine(line []byte) {
	// from start to first space is src or NOT
	// src can be a literal or var
	// check if NOT
	var ins instruction
	var next_token string
	var start int
	switch line[0] {
	case 'N':
		ins.operation = not
		ins.sourceIsLiteral = false
		start = 4
		ins.source, start = parseNextToken(line, start)
		ins.destinaton, _ = parseNextToken(line, start+3)
	case '1', '2', '3', '4', '5', '6', '7', '8', '9', '0':
		ins.sourceIsLiteral = true
		ins.source, start = parseNextToken(line, start)
		next_token, start = parseNextToken(line, start)
		switch next_token {
		case assignment:
			ins.operation = assignment
			ins.destinaton, start = parseNextToken(line, start)
		case and:
			ins.operation = and

		}

	}

}

func mustReadInput() {
	f, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	vars := make(map[string]uint16)
	start := 0
	for i := range f {
		if f[i] == '\n' {
			parseLine(f[start:i])
			start = i + 1
		}
	}
	// a line will have a value 0 - 2>>16
	// a variable: combination of lowercase letters
	// logice gate: capital letters
	// -> storage operator
	// destination: lowercase letters
	//
	// we will make a map of uint16 for all variables
	// parse initial variables `

}

func main() {
	mustReadInput()
}
