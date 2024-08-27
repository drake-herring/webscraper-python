import cv2
import numpy as np

def analyze_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded properly
    if image is None:
        print("Error loading image")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale image
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Detect edges using the Canny edge detector
    edges = cv2.Canny(blurred_image, 50, 150)

    # Display the original image
    cv2.imshow('Original Image', image)

    # Display the grayscale image
    cv2.imshow('Grayscale Image', gray_image)

    # Display the edges
    cv2.imshow('Edges', edges)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
analyze_image('path/to/your/image.jpg')
