# line_detection.py
import cv2
import numpy as np

def detect_lines(frame, edges, mask):
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=50, maxLineGap=150)

    if lines is None:
        return frame, None

    left_lines = []
    right_lines = []
    left_slopes = []
    right_slopes = []

    img_center = frame.shape[1] / 2

    for line in lines:
        for x1, y1, x2, y2 in line:
            if x2 - x1 == 0:
                continue  # Skip vertical lines to avoid division by zero
            slope = (y2 - y1) / (x2 - x1)
            if abs(slope) < 0.3:  # Skip nearly horizontal lines
                continue

            if slope < 0 and x1 < img_center and x2 < img_center:
                left_lines.append((x1, y1, x2, y2))
                left_slopes.append(slope)
            elif slope > 0 and x1 > img_center and x2 > img_center:
                right_lines.append((x1, y1, x2, y2))
                right_slopes.append(slope)

    line_data = {}
    if left_lines:
        left_line = average_line(left_lines)
        cv2.line(frame, (left_line[0], left_line[1]), (left_line[2], left_line[3]), (255, 0, 0), 5)
        rho, theta = convert_to_rho_theta(left_line)
        line_data['left'] = (rho, theta)

    if right_lines:
        right_line = average_line(right_lines)
        cv2.line(frame, (right_line[0], right_line[1]), (right_line[2], right_line[3]), (0, 255, 0), 5)
        rho, theta = convert_to_rho_theta(right_line)
        line_data['right'] = (rho, theta)

    if not line_data:
        return frame, None

    return frame, line_data

def average_line(lines):
    x1s, y1s, x2s, y2s = zip(*lines)
    return (
        int(np.mean(x1s)),
        int(np.mean(y1s)),
        int(np.mean(x2s)),
        int(np.mean(y2s))
    )

def convert_to_rho_theta(line):
    x1, y1, x2, y2 = line
    dx = x2 - x1
    dy = y2 - y1
    rho = (x1 * y2 - y1 * x2) / np.sqrt(dx ** 2 + dy ** 2)
    theta = np.arctan2(dy, dx)
    return rho, theta
