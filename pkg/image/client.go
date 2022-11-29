package image

import (
	"fmt"
	"image"
	"os"

	"github.com/fogleman/gg"
	"github.com/otiai10/gosseract/v2"
)

type ImageHandler struct {
	path    string
	context gg.Context
}

// func (i ImageHandler) Save(path string) error {
// }

func (i *ImageHandler) CoverText(bb gosseract.BoundingBox, path string) error {
	i.context.SetHexColor("#ff0000")
	i.context.SetLineWidth(100)
	i.context.DrawLine(
		float64(bb.Box.Min.X),
		float64(bb.Box.Min.Y),
		float64(bb.Box.Max.X),
		float64(bb.Box.Max.Y),
	)

	return i.context.SavePNG(path)
}

func ReadFile(path string) (i ImageHandler, err error) {
	catFile, err := os.Open(path)
	if err != nil {
		return i, err
	}
	defer catFile.Close()

	imData, imType, err := image.Decode(catFile)
	if err != nil {
		return i, err
	}

	if imType != "jpeg" {
		fmt.Println("image format is not jpeg")
		return i, fmt.Errorf("image format is unsupported")
	}

	return ImageHandler{
		path:    path,
		context: *gg.NewContextForImage(imData),
	}, err
}
