from tesserocr import PyTessBaseAPI

images = ['1.png', '2.png']

with PyTessBaseAPI() as api:
    for img in images:
        api.SetImageFile(img)
        print api.GetUTF8Text()
        print api.AllWordConfidences()