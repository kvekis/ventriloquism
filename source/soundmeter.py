import pygame
import sounddevice as sd
import numpy as np
import time
import sys
import json

SAMPLERATE = 44100
CHANNELS = 1
BLOCKSIZE = 1024

pygame.init()

soundmeter_config = open('./config/soundmeter_config.json')
config = json.load(soundmeter_config)

WIDTH, HEIGHT = config['Width'], config['Height']
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Soundmeter')

icon = pygame.image.load('./images/icon.gif')
pygame.display.set_icon(icon)

font = pygame.font.SysFont(config['Font'], config['FontSize'])

def calculate_db(data):
    rms = np.sqrt(np.mean(np.square(data)))
    if rms == 0:
        return -np.inf
    db = 20 * np.log10(rms)
    return db

def audio_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    volume_db = calculate_db(indata)
    global current_volume
    current_volume = volume_db

current_volume = 0.0

def main():
    with sd.InputStream(callback=audio_callback, channels=CHANNELS, samplerate=SAMPLERATE, blocksize=BLOCKSIZE):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill(config['BackgroundColor'])

            volume_text = f'Громкость: {current_volume:.2f} dB'
            volume_surface = font.render(volume_text, True, config['FontColor'])

            screen.blit(volume_surface, (20, HEIGHT // 2))

            pygame.display.flip()

            time.sleep(0.1)

    pygame.quit()

if __name__ == '__main__':
    main()
    
soundmeter_config.close()