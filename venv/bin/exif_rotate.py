from PIL import Image
import piexif

def rotate_jpeg(filename):

    img = Image.open(filename)

    if "exif" in img.info:
        exif_dict = piexif.load(img.info["exif"])
        #print(exif_dict)

        if piexif.ImageIFD.Orientation not in exif_dict['0th']:

            exif_dict['0th'][piexif.ImageIFD.Orientation] = 7

            exif_bytes = piexif.dump(exif_dict)

            img.save(filename, exif=exif_bytes)


        if piexif.ImageIFD.Orientation in exif_dict["0th"]:
            orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
            exif_bytes = piexif.dump(exif_dict)
            #print("0th")

            if orientation == 2:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
                #print("2")
            elif orientation == 3:
                img = img.rotate(180)
               #print("3")
            elif orientation == 4:
                img = img.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
                #print("4")
            elif orientation == 5:
                img = img.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
                #print("5")
            elif orientation == 6:
                img = img.rotate(-90, expand=True)
                #print("6")
            elif orientation == 7:
                img = img.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
                #print("7")
            elif orientation == 8:
                img = img.rotate(90, expand=True)
                #print("8")

            img.save(filename, exif=exif_bytes)

            print("Rotated image " + filename)

        else:
            print("No orientation?")


rotate_jpeg('piCam Photos/cap3.jpg')