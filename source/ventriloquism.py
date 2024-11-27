import pygame
import sounddevice as sd
import numpy as np
import time
import sys
import json
import random

SAMPLERATE = 44100
CHANNELS = 1
BLOCKSIZE = 1024

pygame.init()

ventriloquism_config = open('./config/ventriloquism_config.json')
config = json.load(ventriloquism_config)

WIDTH, HEIGHT = config['Width'], config['Height']
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ventriloquism')
icon = pygame.image.load('./images/icon.gif')
pygame.display.set_icon(icon)
theme = config['Theme']

images = []
image_surfaces = []
blink_surfaces = []

for i in config['Images']:
    images.append(i)
    image_surfaces.append(pygame.image.load(f'./images/{theme}/{i}.png'))
    if 'b' in config['Images'][f'{i}'][0]:
        blink_surfaces.append(pygame.image.load(f'./images/{theme}/{i}_blink.png'))
    else:
        blink_surfaces.append(pygame.image.load(f'./images/{theme}/{i}.png'))


def calculate_db(data):
    rms = np.sqrt(np.mean(np.square(data)))
    if rms == 0:
        return -np.inf
    db = 20 * np.log10(rms)
    return db

def audio_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    global current_volume
    current_volume = calculate_db(indata)

def get_image_for_volume(db, is_blink):
    if config['VolumeDisplay']: print(f'Громкость: {int(db)} дБ')
    global image_index
    image_index = 0
    for i in range(len(images)):
       if db < config['Images'][images[i]][1]:
           image_index = i
           if not is_blink: return image_surfaces[i]
           else: return blink_surfaces[i]
    if not is_blink: return image_surfaces[0]
    else: return blink_surfaces[0]

def main():
    shake_effect = False
    blink_frames = config['BlinkFrames']
    next_blink = config['BlinkInterval'] + random.randint(-config['BlinkIntervalRandom'], config['BlinkIntervalRandom'])

    with sd.InputStream(callback=audio_callback, channels=CHANNELS, samplerate=SAMPLERATE, blocksize=BLOCKSIZE):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill(config['BackgroundColor'])


            new_width = int(WIDTH * config['ImageSize'])
            new_height = int(HEIGHT * config['ImageSize'])

            image_to_display = pygame.transform.scale(get_image_for_volume(current_volume, False), (new_width, new_height))
            
            next_blink -= 1

            if blink_frames < config['BlinkFrames'] or next_blink <= 0:
                blink_frames -= 1
                if blink_frames == 0:
                    next_blink = config['BlinkInterval'] + random.randint(-config['BlinkIntervalRandom'], config['BlinkIntervalRandom'])
                    blink_frames = config['BlinkFrames']
                image_to_display = pygame.transform.scale(get_image_for_volume(current_volume, True), (new_width, new_height))
                

            x_pos = (WIDTH - new_width) // 2
            y_pos = (HEIGHT - new_height) // 2

            if 's' in config['Images'][images[image_index]][0]:
                shake_effect = True
            else:
                shake_effect = False

            if shake_effect:
                if config['ShakeDisplay']: print('Тряска включена')
                x_pos += random.randint(-config['ShakePower'], config['ShakePower'])
                y_pos += random.randint(-config['ShakePower'], config['ShakePower'])

            screen.blit(image_to_display, (x_pos, y_pos))

            pygame.display.flip()

            time.sleep(round(1 / config['FPS'], 4))

    pygame.quit()

if __name__ == '__main__':
    current_volume = 0.0
    main()

ventriloquism_config.close()