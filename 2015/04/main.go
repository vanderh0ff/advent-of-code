package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"log"
	"os"
	"strconv"
)

func get_secret_key() string {
	file, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	return string(file)[:8]
}

func is_valid_hash(n int, key string) bool {
	h := key + strconv.Itoa(n)
	hash := md5.Sum([]byte(h))
	hexencoded := hex.EncodeToString(hash[:])
	fmt.Println(h)
	fmt.Println(hexencoded[:6])
	if hexencoded[:6] == "000000" {
		return true
	}
	return false
}

func main() {
	key := get_secret_key()
	n := 1
	for !is_valid_hash(n, key) {
		n++
		fmt.Println("trying ", n)
	}
	fmt.Println(n)
}
