import pygame
from pygame.locals import *
from PIL import ImageGrab, Image
import pyautogui

pygame.init()
left_monitor_width, left_monitor_height = pyautogui.size()
left_monitor_rect = pygame.Rect(0, 0, left_monitor_width, left_monitor_height)
screen = pygame.display.set_mode((left_monitor_width, left_monitor_height), pygame.NOFRAME)

# Load the image with transparency
image_path = 'image.jpg'
image = Image.open(image_path)
image = image.convert("RGBA")

# Ensure image has alpha channel
if image.mode != "RGBA":
    image = image.convert("RGBA")

image = pygame.image.fromstring(image.tobytes(), image.size, image.mode).convert_alpha()

# Set the transparency level (0-255)
alpha = 50

# Increase the size of the image
# Adjust these values as needed to resize the image
image_width = image.get_width() * 3  # Doubling the image width
image_height = image.get_height() * 3  # Doubling the image height
image = pygame.transform.scale(image, (image_width, image_height))

center_x = (left_monitor_width - image_width) // 2
center_y = (left_monitor_height - image_height) // 2

mouse_cursor_image_path = 'mouse.png'  # Update this with your mouse cursor image path
mouse_cursor_image = pygame.image.load(mouse_cursor_image_path)
mouse_cursor_image = pygame.transform.scale(mouse_cursor_image, (32, 32))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    game_window_capture = ImageGrab.grab(bbox=(0, 0, left_monitor_width, left_monitor_height))
    game_window_surface = pygame.image.fromstring(game_window_capture.tobytes(), game_window_capture.size,
                                                  game_window_capture.mode).convert()
    screen.blit(game_window_surface, (0, 0))
    mouse_x, mouse_y = pyautogui.position()
    mouse_x_rel = mouse_x - left_monitor_rect.left
    mouse_y_rel = mouse_y - left_monitor_rect.top
    screen.blit(mouse_cursor_image, (mouse_x_rel, mouse_y_rel))
    image.set_alpha(alpha)
    screen.blit(image, (center_x, center_y))
    pygame.display.flip()

pygame.quit()
