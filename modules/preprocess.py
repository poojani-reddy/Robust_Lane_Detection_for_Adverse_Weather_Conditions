# Preprocess pipeline logic
import cv2
import numpy as np
from modules import fuzzy_controller, contrast, filters, roi, line_detection, tracking

def pipeline(frame, fuzzy_params, frame_num):
    # Step 1: Contrast Adjustment (detect yellow lines)
    processed_frame, yellow_detected = contrast.to_grayscale_or_yuv(frame)

    # Step 2: Noise Reduction
    filtered_frame = filters.apply_bilateral_filter(processed_frame)

    # Step 3: Fuzzy Logic (update Canny thresholds)
    high_thresh = fuzzy_controller.tune_threshold(fuzzy_params)
    low_thresh = int(high_thresh / 3)
    fuzzy_params["high_thresh"] = high_thresh
    fuzzy_params["low_thresh"] = low_thresh

    # Step 4: Edge Detection
    edges = cv2.Canny(filtered_frame, low_thresh, high_thresh)

    # Step 5: Adaptive ROI
    mask = roi.get_adaptive_roi(frame.shape[0], frame.shape[1], fuzzy_params)
    edges_roi = cv2.bitwise_and(edges, edges, mask=mask)

    # Step 6: Line Detection
    result_img, line_data = line_detection.detect_lines(frame, edges_roi, mask)

    if line_data is None:
        result_img = tracking.use_previous(result_img, fuzzy_params)
        fuzzy_params["left_detected"] = False
        fuzzy_params["right_detected"] = False
    else:
        fuzzy_params["prev_lines"] = line_data
        fuzzy_params["left_detected"] = 'left' in line_data
        fuzzy_params["right_detected"] = 'right' in line_data

    return result_img, fuzzy_params

import cv2
import numpy as np

def get_lane_masks(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Yellow mask
    lower_yellow = np.array([15, 80, 80])
    upper_yellow = np.array([35, 255, 255])
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # White mask
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 30, 255])
    white_mask = cv2.inRange(hsv, lower_white, upper_white)
    # Combine masks
    combined_mask = cv2.bitwise_or(yellow_mask, white_mask)
    return combined_mask

def enhance_contrast(frame):
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl,a,b))
    enhanced = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return enhanced
