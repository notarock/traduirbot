package main

import (
	"fmt"
	"log"
	ocr "notarock/traduirbot/pkg/OCR"

	"gopkg.in/gographics/imagick.v2/imagick"
)

func main() {
	c := ocr.New("/tmp/traduir")
	boundingBox, err := c.ReadText("/app/image.jpg")
	if err != nil {
		log.Fatal(err)
	}
	for _, text := range boundingBox {
		fmt.Printf("%+v", text)
	}
	imagick.Initialize()
	defer imagick.Terminate()

	mw := imagick.NewMagickWand()
	defer mw.Destroy()
}
