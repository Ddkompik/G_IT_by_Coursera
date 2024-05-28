from PIL import Image
import os

Path = "C:\\Users\\dasha\\Documents\\CODE\\GitHub\\G_IT_by_Coursera\\AutoPython\\test_jpg\\images"
New_Path = "C:\\Users\\dasha\\Documents\\CODE\\GitHub\\G_IT_by_Coursera\\AutoPython\\test_jpg\\images_jpg"

for file_count in os.listdir(Path):
    if file_count != ".DS_Store":
        im = Image.open(os.path.join(Path, file_count))
        im = im.rotate(90)
        im = im.resize((128,128))
        im = im.convert("RGB")
        im.save(os.path.join(New_Path,file_count+".jpg"))
