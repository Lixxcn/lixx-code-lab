package main

import (
	"fmt"
	"time"
)

func main() {
	ch1 := make(chan int)
	ch2 := make(chan int)

	go func() {
		fmt.Println("goroutine")
		v := 1
		ch1 <- v
		ch2 <- 0
		// v2 := <-ch2
		fmt.Println(v)
	}()

	time.Sleep(1 * time.Second)
}
