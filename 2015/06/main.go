package main

import (
	"log"
	"os"
	"strconv"
)

type area = struct {
	top    int
	left   int
	bottom int
	right  int
}

const (
	on     = 0
	off    = 1
	toggle = 2
)

type instruction = struct {
	a      area
	action int
}

func update(ins instruction, lights [][]int) {
	for i := ins.a.left; i <= ins.a.right; i++ {
		for j := ins.a.top; j <= ins.a.bottom; j++ {
			switch ins.action {
			case on:
				lights[i][j] = lights[i][j] + 1
			case off:
				lights[i][j] = max(lights[i][j]-1, 0)
			case toggle:
				lights[i][j] = lights[i][j] + 2
			}
		}
	}
}

func musReadInput() []instruction {
	f, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	instructions := make([]instruction, 0)
	start := 0
	for i, v := range f {
		if v == '\n' {
			ins, err := parseInputLine(f[start:i])
			if err != nil {
				log.Fatal("error parsing instruction", start, i)
			}
			instructions = append(instructions, ins)
			start = i + 1
		}
	}
	return instructions
}

func parseInputLine(line []byte) (instruction, error) {
	//turn on 887,9 through 959,629
	//turn off 539,243 through 559,965
	//toggle 720,196 through 897,994
	var instruct instruction
	var err error
	err = nil
	i := 0
	switch line[5] {
	case 'e':
		instruct.action = toggle
		i = 7
	case 'o':
		if line[6] == 'n' {
			instruct.action = on
			i = 8
		} else {
			instruct.action = off
			i = 9
		}
	}
	for j := i; j < len(line); j++ {
		if line[j] == ',' {
			instruct.a.top, err = strconv.Atoi(string(line[i:j]))
			if err != nil {
				log.Fatal("Error parsing top: ", err)
			}
			i = j + 1
			break
		}
	}
	for j := i; j < len(line); j++ {
		if line[j] == ' ' {
			instruct.a.left, err = strconv.Atoi(string(line[i:j]))
			if err != nil {
				log.Fatal("Error parsing left: ", err)
			}
			i = j + 9
			break
		}
	}
	for j := i; j < len(line); j++ {
		if line[j] == ',' {
			instruct.a.bottom, err = strconv.Atoi(string(line[i:j]))
			if err != nil {
				log.Fatal("Error parsing bottom: ", err)
			}
			i = j + 1
			break
		}
	}
	instruct.a.right, err = strconv.Atoi(string(line[i:]))
	if err != nil {
		log.Fatal("Error parsing left: ", err)
	}
	return instruct, err
}

func main() {
	var lights [][]int = make([][]int, 1000, 1000)
	for i := range lights {
		lights[i] = make([]int, 1000, 1000)
	}
	ins := musReadInput()
	for i := range ins {
		update(ins[i], lights)
	}
	total := 0
	for i := range lights {
		for j := range lights[i] {
			total += lights[i][j]
		}
	}
	log.Println("total: ", total)
}
