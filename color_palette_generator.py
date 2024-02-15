import cv2
import numpy as np
from collections import Counter


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])


def calculate_distance(color1, color2):
    return np.linalg.norm(np.array(color1) - np.array(color2))


def get_most_common_colors(image_path, num_colors=300, similarity_threshold=150):
    # Read the image
    image = cv2.imread(image_path)

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

    # Filter out similar colors based on the threshold
    filtered_colors = []
    for color, count in most_common_colors:
        is_similar = any(
            calculate_distance(color, existing_color) < similarity_threshold for existing_color, _ in filtered_colors)
        if not is_similar:
            filtered_colors.append((color, count))

    # Convert RGB to hex and include both RGB and hex in the result
    most_common_colors_formatted = [(rgb, rgb_to_hex(rgb), count) for rgb, count in filtered_colors]

    return most_common_colors_formatted


# Example usage
image_path = 'static/images/index_image.jpg'
most_common_colors = get_most_common_colors(image_path)

# Display the most common colors in both RGB and hex format with a similarity threshold of 30
print("Most Common Colors:")
color_counter = 0
for rgb, color_hex, count in most_common_colors:
    if color_counter % 5 == 0:
        print(f"RGB: {rgb}, Hex: {color_hex}, Count: {count}")
    color_counter += 1
