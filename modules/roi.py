# Adaptive ROI module
import cv2
import numpy as np

vanishing_point_history = []

def get_adaptive_roi(height, width, fuzzy_params):
    global vanishing_point_history

    if fuzzy_params.get("reset_history", False):
        vanishing_point_history.clear()

    default_x = width // 2
    default_y = int(height * fuzzy_params["roi_y"])

    if fuzzy_params["left_detected"] and fuzzy_params["right_detected"]:
        tip_x = default_x
    elif fuzzy_params["left_detected"]:
        tip_x = int(width * 0.4)
    elif fuzzy_params["right_detected"]:
        tip_x = int(width * 0.6)
    else:
        tip_x = default_x

    tip_y = default_y

    vanishing_point_history.append((tip_x, tip_y))
    if len(vanishing_point_history) > 30:
        vanishing_point_history.pop(0)

    avg_x = int(np.mean([pt[0] for pt in vanishing_point_history]))
    avg_y = int(np.mean([pt[1] for pt in vanishing_point_history]))

    bottom_left = (0, height)
    bottom_right = (width, height)
    tip = (avg_x, avg_y)

    mask = np.zeros((height, width), dtype=np.uint8)
    roi_corners = np.array([[bottom_left, tip, bottom_right]], dtype=np.int32)
    cv2.fillPoly(mask, roi_corners, 255)

    return mask
