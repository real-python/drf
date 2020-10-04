from PIL import Image

def process_image(file_path):
    foo = Image.open(file_path)
    foo.save(file_path, quality=40)