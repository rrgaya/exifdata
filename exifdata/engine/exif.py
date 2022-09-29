import  os
from PIL.ExifTags import TAGS 
from PIL import Image 
import exifread



class ExifExtract:
    """ Esta classe é o motor de extração EXIF DATA de imagens
        param:
            directory_images: str
    """
    path_images = []

    def __init__(self, directory_images: str) -> None:
        try:
            self.directory_images = directory_images
            self.path_images = [os.path.join(directory_images, nome) for nome in os.listdir(directory_images)]
        except FileNotFoundError as error:
            raise Exception("f{error}")

    def get_exif(self) -> dict:
        """ Esta classe é o motor de extração EXIF DATA de imagens
            param:
                
            return:
                Retorna um dict de EXIF DATA por imagem
        """
        exif_data = {}
        for name in self.path_images:
            try:
                image = Image.open(name) 
                exifdata = image.getexif()
                exif_data[name] = exifdata
            except:
                print("Deu ruim ao abrir.")
        
        print(f"<<GET EXIF>>")
        
        for img in exif_data:
            print(f"{img:35}", exif_data[img])
        return exif_data

    def read_exif(self, files_path):
        tags_by_file = {}
        for file in files_path:
            try:
                f = open(file, 'rb')
                tags = exifread.process_file(f)
                tags_by_file[file] = tags
            except:
                print(f"Não foi possivel ler o exif dessa imagem.")
            
        return tags_by_file