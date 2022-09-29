from PIL import Image 
from exifdata.engine.exif import ExifExtract
from pprint import pprint

engine = ExifExtract('images')
exidata = engine.get_exif()

exidata_2 = engine.read_exif(engine.path_images)

pprint(exidata_2)
