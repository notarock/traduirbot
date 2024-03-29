package ocr

import "github.com/otiai10/gosseract/v2"

type OcrClient struct {
	storage string
}

func New(path string) OcrClient {
	return OcrClient{
		storage: path,
	}
}

func (o OcrClient) ReadText(imagePath string) ([]gosseract.BoundingBox, error) {
	client := gosseract.NewClient()
	defer client.Close()
	client.SetImage(imagePath)
	return client.GetBoundingBoxes(gosseract.RIL_PARA)
}
