""" Генератор случайных аватарок """
import random
import math
import hashlib
import argparse
from PIL import Image, ImageOps

IMAGE_SIZE = 5
IMAGE_SIZE_HALF = int(math.ceil(IMAGE_SIZE / 2))

BACKGROUND_COLOR = 250, 251, 253


def generate_avatar(name: str, filename: str = None):
    filename = filename or f"{name}.png"

    seed = hashlib.md5(name.encode('utf-8')).digest()
    random.seed(seed)

    foreground_color = random.randint(100, 200), \
                       random.randint(100, 200), \
                       random.randint(100, 200)

    with Image.new('P', (IMAGE_SIZE, IMAGE_SIZE), 0) as img:
        img.putpalette(BACKGROUND_COLOR + foreground_color)

        px = img.load()
        for _ in range(random.randint(5, 12)):
            x = random.randrange(0, IMAGE_SIZE_HALF)
            y = random.randrange(0, IMAGE_SIZE)
            px[x, y] = 1
            px[-1 - x, y] = 1

        img = img.resize((IMAGE_SIZE * 2, IMAGE_SIZE * 2), Image.NEAREST)
        img = ImageOps.expand(img, 1, 0)
        img.save(filename)

    print("Ваша аватарка сохранена с именем", filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Генератор случайных аватарок")
    parser.add_argument("name", action="store")
    args = parser.parse_args()

    generate_avatar(args.name)
