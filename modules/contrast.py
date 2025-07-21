# Contrast adjustment module
import cv2
import numpy as np

def to_grayscale_or_yuv(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    yellow_detected = False

    # Convert to YUV to detect yellow lines
    img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    u_channel = img_yuv[:, :, 1]
    v_channel = img_yuv[:, :, 2]

    yellow_mask = (u_channel - v_channel) < -15
    yellow_ratio = np.sum(yellow_mask) / (yellow_mask.shape[0] * yellow_mask.shape[1])

    if 0.01 < yellow_ratio < 0.15:
        yellow_detected = True
        return img_yuv[:, :, 0], yellow_detected  # Use Y channel from YUV
    else:
        return img_gray, yellow_detected
