package main

import (
	"fmt"
	"log"
	ocr "notarock/traduirbot/pkg/OCR"
)

func main() {
	c := ocr.New("/tmp/traduir")
	texts, err := c.ReadText("/app/image.jpg")
	if err != nil {
		log.Fatal(err)
	}
	for _, text := range texts {
		fmt.Printf("%+v", text)
	}
}
