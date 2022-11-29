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

	i, err := image.ReadFile("/app/images/hat.jpg")
	if err != nil {
		log.Fatal(err)
	}

	t := texts[0]
	i.CoverText(t, "/app/images/out.jpg")
	if err != nil {
		log.Fatal(err)
	}

}
