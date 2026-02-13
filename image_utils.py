from PIL import Image
import imagehash  #using for generaition of fingerprints


def generate_hash(image_path):
    image = Image.open(image_path)
    hash_value = imagehash.phash(image)
    return str(hash_value)
