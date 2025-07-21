# main.py
import cv2
import os
import argparse
from modules import preprocess

def process_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"❌ Cannot open video file {video_path}")
        return

    frame_width = 640
    frame_height = 360
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0 or fps is None:
        fps = 20

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    fuzzy_params = {
        "high_thresh": 100,
        "low_thresh": 33,
        "roi_x": 0.5,
        "roi_y": 0.6,
        "left_detected": True,
        "right_detected": True,
        "prev_lines": None,
        "reset_history": True
    }

    frame_num = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (frame_width, frame_height))
        frame_out, fuzzy_params = preprocess.pipeline(frame.copy(), fuzzy_params, frame_num)

        out.write(frame_out)
        frame_num += 1

        if frame_num % 10 == 0:
            print(f"📽️ Processed frame {frame_num}")

    cap.release()
    out.release()
    print(f"✅ Video processing completed. Output saved at {output_path}")

def process_image(image_path, output_path):
    frame = cv2.imread(image_path)
    if frame is None:
        print(f"❌ Cannot load image {image_path}")
        return

    fuzzy_params = {
        "high_thresh": 100,
        "low_thresh": 33,
        "roi_x": 0.5,
        "roi_y": 0.6,
        "left_detected": True,
        "right_detected": True,
        "prev_lines": None,
        "reset_history": True
    }

    frame = cv2.resize(frame, (640, 360))
    result, _ = preprocess.pipeline(frame.copy(), fuzzy_params, 0)

    cv2.imwrite(output_path, result)
    print(f"✅ Image processed and saved at {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fuzzy Lane Detection System")
    parser.add_argument("--video", type=str, help="Path to video file (e.g., assets/video.mp4)")
    parser.add_argument("--image", type=str, help="Path to single image file (e.g., assets/frame.jpg)")
    parser.add_argument("--output", type=str, default="output/output_result", help="Output path (auto extension)")

    args = parser.parse_args()
    os.makedirs("output", exist_ok=True)

    if args.video:
        output_video_path = args.output
        if not output_video_path.endswith(".mp4"):
            output_video_path += ".mp4"
        process_video(args.video, output_video_path)
    elif args.image:
        output_image_path = args.output
        if not (output_image_path.endswith(".png") or output_image_path.endswith(".jpg")):
            output_image_path += ".jpg"
        process_image(args.image, output_image_path)
    else:
        print("⚠️ Please provide either --video <path> or --image <path>")
