package main

import (
	"fmt"
	"log"
	ocr "notarock/traduirbot/pkg/OCR"
)

func main() {
	c := ocr.New("/tmp/traduir")
	text, err := c.ReadText("/app/image.jpg")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(text)
}
