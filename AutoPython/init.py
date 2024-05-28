from PIL import Image

with Image.open("C:\\Users\\dasha\\Documents\\CODE\\GitHub\\G_IT_by_Coursera\\AutoPython\\owl.png") as im:
    im.rotate(180).show()
