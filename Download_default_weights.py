import os
import subprocess
import time
import argparse

FLAGS = None

root_folder = os.path.dirname(os.path.abspath(__file__))
download_folder = os.path.join(root_folder, "Keras_yolov3", "src", "keras_yolo3")
data_folder = os.path.join(root_folder, "Data")
model_folder = os.path.join(data_folder, "Model_Weights")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YOLOv3 weights and convert to h5 format.")
    
    parser.add_argument(
        "--download_folder",
        type=str,
        default=download_folder,
        help="Folder to download weights to. Default is " + download_folder,
    )

    parser.add_argument(
        "--is_tiny",
        default=False,
        action="store_true",
        help="Use the tiny Yolo version for better performance and less accuracy. Default is False.",
    )

    FLAGS = parser.parse_args()

    if not FLAGS.is_tiny:
        weights_file = "yolov3.weights"
        h5_file = "yolo.h5"
        cfg_file = "yolov3.cfg"
        weights_url = "https://pjreddie.com/media/files/yolov3.weights"
    else:
        weights_file = "yolov3-tiny.weights"
        h5_file = "yolo-tiny.h5"
        cfg_file = "yolov3-tiny.cfg"
        weights_url = "https://pjreddie.com/media/files/yolov3-tiny.weights"

    weights_path = os.path.join(download_folder, weights_file)

    if not os.path.isfile(weights_path):
        print(f"\nDownloading Raw {weights_file}\n")
        start = time.time()
        subprocess.call(["wget", "-O", weights_path, weights_url])
        end = time.time()
        print(f"Downloaded Raw {weights_file} in {end - start:.1f} seconds\n")

        convert_command = f"python convert.py {cfg_file} {weights_file} {h5_file}"
        subprocess.call(convert_command, shell=True, cwd=download_folder)
