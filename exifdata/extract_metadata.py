import exifread
from PIL import Image 
from engine.exif import ExifExtract


engine = ExifExtract('images')
exidata = engine.get_exif()

exidata_2 = engine.read_exif()

print(engine.exif_read(engine.path_images[0]))

# path_images = [os.path.join("images", nome) for nome in os.listdir("images")]


for name in path_images:
    try:
        f = open(name, 'rb')
        tags = exifread.process_file(f)

        print(f"{name} = {tags}")
        image = Image.open(name) 
        exifdata = image.getexif()
        extract_exif(name, exifdata)
    except:
        print("Deu ruim ao abrir.")
import exifread




