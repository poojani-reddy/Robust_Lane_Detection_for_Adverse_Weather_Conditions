# Bilateral filtering module
import cv2

def apply_bilateral_filter(image):
    """
    Applies bilateral filtering to retain edges while reducing noise.
    """
    filtered_image = cv2.bilateralFilter(image, 7, 25, 50)
    return filtered_image
