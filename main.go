package main

import (
	"fmt"
	"log"
	ocr "notarock/traduirbot/pkg/OCR"
	"notarock/traduirbot/pkg/image"
)

func main() {
	c := ocr.New("/tmp/traduir")
	texts, err := c.ReadText("/app/images/hat.jpg")
	if err != nil {
		log.Fatal(err)
	}
	for _, text := range texts {
		fmt.Printf("%+v", text)
	}

	t := texts[0]
	image.CoverText("/app/images/hat.jpg", t, "/app/images/out.png")
	if err != nil {
		log.Fatal(err)
	}

}
