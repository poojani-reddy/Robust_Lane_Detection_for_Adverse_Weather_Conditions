# Tracking recovery module
import cv2
import numpy as np

def use_previous(frame, fuzzy_params):
    """
    If current frame detection fails, use previous frame's lines.
    """
    prev_lines = fuzzy_params.get("prev_lines", None)

    if prev_lines is None:
        return frame  # Nothing to track

    if 'left' in prev_lines:
        draw_line(frame, prev_lines['left'], color=(0, 0, 255))  # Red for left

    if 'right' in prev_lines:
        draw_line(frame, prev_lines['right'], color=(0, 255, 0))  # Green for right

    return frame

def draw_line(img, line, color=(0, 255, 0), thickness=3):
    rho, theta = line
    a = np.cos(theta)
    b = np.sin(theta)

    x0 = a * rho
    y0 = b * rho

    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(img, (x1, y1), (x2, y2), color, thickness)
