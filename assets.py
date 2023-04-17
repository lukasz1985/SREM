import pygame.image

images = {} # The cache of images

def load_image(path):
    if not path in images:
        # If the image is not cached load it and add to the cache:
        try:
            image = pygame.image.load(path).convert_alpha()
        except:
            print("Cant load image: " + path)
        images[path] = image
        return image
    else:
        # Else just return the cached image:
        return images[path]


fonts = {}

def load_font(path, size):
    key = path + str(size)
    if not key in fonts:
        font = pygame.font.Font(path, size)
        fonts[key] = font
        return font
    else:
        return fonts[key]


sounds = {}
def load_sound(path):
    if not path in sounds:
        sound = pygame.mixer.Sound(path)
        sounds[path] = sound
        return sound
    else:
        return sounds[path]
