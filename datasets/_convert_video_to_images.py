import argparse
import cv2
import os

def convert_video_to_images(video_path, out_dir, ext='jpg'):
    cap = cv2.VideoCapture(video_path)
    t = 0
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(f'{out_dir}/{t:010d}.{ext}', frame)
            t += 1
        else:
            return

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--video_path', type=str, required=True)
    # parser.add_argument('--out_dir', type=str)
    # parser.add_argument('--ext', type=str, default='jpg')
    # args = parser.parse_args()

    # if args.out_dir is None:
    #     args.out_dir = os.path.splitext(args.video_path)[0]
    # os.makedirs(out_dir, exist_ok=True)

    # convert_video_to_images(args.video_path, args.out_dir, ext)

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, required=True)
    parser.add_argument('--video_ext', type=str, default='mp4')
    parser.add_argument('--image_ext', type=str, default='jpg')
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
        convert_video_to_images(video_path, out_dir, args.image_ext)
