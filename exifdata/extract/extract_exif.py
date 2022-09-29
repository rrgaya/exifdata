from PIL.ExifTags import TAGS 


def extract_exif(name_file, exifdata):

    print(F"Extracting: {name_file}")

    if len(exifdata) == 0:
        print(f"{name_file} não possui EXIF DATA")
    for tagid in exifdata: 
        tagname = TAGS.get(tagid, tagid)
        value = exifdata.get(tagid) 
        print(f"{tagname:20}: {value}")
    
    return tagname, value