import argparse
import cv2
import os

def convert_video_to_images(video_path, out_dir, ext='jpg', 
                            height=None, width=None):
    cap = cv2.VideoCapture(video_path)
    t = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            return

        # Center-cropping to adjust the size
        H, W, _ = frame.shape
        if height is not None:
            if height > H:
                raise ValueError
            H0 = (H - height) // 2
            H1 = H0 + height
            frame = frame[H0:H1]

        if width is not None:
            if width > W:
                raise ValueError
            W0 = (W - width) // 2
            W1 = W0 + width
            frame = frame[:, W0:W1]

        cv2.imwrite(f'{out_dir}/{t:010d}.{ext}', frame)
        t += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, required=True)
    parser.add_argument('--video_ext', type=str, default='mp4')
    parser.add_argument('--image_ext', type=str, default='jpg')
    parser.add_argument('--height', type=int)
    parser.add_argument('--width', type=int)
    args = parser.parse_args()

    image_dir = os.path.join(args.data_dir, 'image')
    os.makedirs(image_dir, exist_ok=True)
    for file_name in os.listdir(args.data_dir):
        base, ext = os.path.splitext(file_name)
        if ext[1:] != args.video_ext:
            continue
        
        print(f"Transforming {file_name}")
        video_path = os.path.join(args.data_dir, file_name)
        out_dir = os.path.join(image_dir, base)
        os.makedirs(out_dir, exist_ok=True)
        convert_video_to_images(video_path, out_dir, args.image_ext,
                                args.height, args.width)
    print("All done!")
