import cv2
import numpy as np
from collections import Counter


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])


def get_most_common_colors(image_path, num_colors=300):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        print(f"Error: Unable to load the image from {image_path}.")
        return []

    print("Image loaded successfully.")

    # Convert the image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reshape the image to a 2D array of pixels
    pixels = image_rgb.reshape((-1, 3))

    # Convert to a list of tuples (R, G, B)
    pixels = [tuple(pixel) for pixel in pixels]

    # Use Counter to count the occurrences of each color
    color_counter = Counter(pixels)

    # Get the most common colors
    most_common_colors = color_counter.most_common(num_colors)

    # Convert RGB to hex and include both RGB and hex in the result
    most_common_colors_formatted = [(rgb, rgb_to_hex(rgb), count) for rgb, count in most_common_colors]

    return most_common_colors_formatted
