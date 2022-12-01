package image

import (
	"strings"

	"github.com/fogleman/gg"
	"github.com/otiai10/gosseract/v2"
)

const (
	PATH_TO_IMPACT_FONT_TTF = "/app/resources/impact.ttf"
)

func CoverText(input string, bb gosseract.BoundingBox, path string) error {
	image, err := gg.LoadImage(input)
	if err != nil {
		return err
	}
	dc := gg.NewContextForImage(image)

	if err := dc.LoadFontFace(PATH_TO_IMPACT_FONT_TTF, 96); err != nil {
		return err
	}

	dc.SetRGB(0, 0, 0)

	textToWrite := strings.Replace(bb.Word, "\n", ", ", -1)

	n := 6 // "stroke" size
	x := float64(bb.Box.Min.X)
	y := float64(bb.Box.Min.Y)

	for dy := -n; dy <= n; dy++ {
		for dx := -n; dx <= n; dx++ {
			if dx*dx+dy*dy >= n*n {
				// give it rounded corners
				continue
			}
			dc.DrawStringAnchored(textToWrite, x, y, 0.5, 0.5)
		}
	}
	dc.SetRGB(1, 1, 1)
	dc.DrawStringAnchored(textToWrite, x/2, y/2, 0.5, 0.5)
	dc.SavePNG(path)

	return nil
}
