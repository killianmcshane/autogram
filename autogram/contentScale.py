from defines import getPaths
from os import path, listdir, system, remove, rename
import shutil
import re
import mimetypes
import cv2

paths = getPaths()
Executable = paths['ffmpeg']


def scaleImage(file):
    """
    Scales/pads the first image file in the pre-processing directory to match Instagram's requirements.

    :param file: The first image file in the pre-processing directory.
    :return:
    """
    content_path = paths['content_preprocessing_path'] + file
    output_path = paths['content_upload_path'] + path.splitext(file)[0] + ".jpeg"

    image = cv2.imread(content_path)
    h, w = image.shape[:2]
    aspect_ratio = w / h

    # 0.8 to 1.91
    if aspect_ratio < 0.8:
        # Vertical Image
        new_width = h * 0.85
        top, bottom = 0, 0
        left, right = int((new_width - w) / 2), int((new_width - w) / 2)
        new_im = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        cv2.imwrite(content_path, new_im)
        print("Pad Type: 9/16 (vertical) [", file, "]")
        shutil.move(content_path, output_path)

    elif aspect_ratio > 1.9:
        # Horizontal Image
        new_height = w / 1.85
        top, bottom = int((new_height - h) / 2), int((new_height - h) / 2)
        left, right = 0, 0
        new_im = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        cv2.imwrite(content_path, new_im)
        print("Pad Type: 16/9 (horizontal) [", file, "]")
        shutil.move(content_path, output_path)

    else:
        shutil.move(content_path, output_path)


def scaleVideo(file):
    """
    Scales/pads the first video file in the pre-processing directory to match Instagram's requirements.

    :param file: The first video file in the pre-processing directory.
    """
    content_path = paths['content_preprocessing_path'] + file
    output_path = paths['content_upload_path'] + path.splitext(file)[0] + ".mp4"

    vcap = cv2.VideoCapture(content_path)
    aspect_ratio = 1

    if vcap.isOpened():
        w = vcap.get(3)
        h = vcap.get(4)
        aspect_ratio = float("%.2f" % (w / h))
        vcap.release()

    # 0.56 to 1.77
    if aspect_ratio < 0.6:  # (~ 9/16)
        cmd = " -y -loglevel error -vf split[original][copy];[copy]scale=ih*4/5:-1,crop=h=iw*5/4,gblur=sigma=20[blurred];[" \
                  "blurred][original]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2 -c:v libx264 -c:a aac -crf " \
                  "17 -preset slow -profile:v high -level 4.0 -color_primaries 1 -color_trc 1 -colorspace 1 " \
                  " -movflags +faststart -b:a 128k "

        pad_cmd = Executable + " -y -loglevel error -i " + content_path + cmd + output_path
        system(pad_cmd)
        remove(content_path)
        print("Pad Type: 9/16 (vertical) [", file, "]")

    elif aspect_ratio > 1.75:  # (~ 16/9)
        cmd = " -y -loglevel error -lavfi [0:v]scale=iw:2*trunc(iw*9/16),boxblur=luma_radius=min(h\," \
                  "w)/20:luma_power=1:chroma_radius=min(cw\,ch)/20:chroma_power=1[bg];[bg][0:v]overlay=(W-w)/2:(" \
                  "H-h)/2,setsar=1 -c:v libx264 -c:a aac -crf 17 -preset slow -profile:v high -level 4.0 " \
                  "-color_primaries 1 -color_trc 1 -colorspace 1 -movflags +faststart -b:a 128k "

        pad_scale = Executable + " -y -loglevel error -i " + content_path + cmd + output_path
        system(pad_scale)
        remove(content_path)
        print("Pad Type: 16/9 (horizontal) [", file, "]")

    else:
        shutil.move(content_path, output_path)


def scaleContent():
    """
    Scans each file in the 'pre-processing' folder and calls its corresponding
    padding/scaling function. File names are formatted to remove all whitespace first,
    so that the ffmpeg executable is able to handle them.

    After processing, each file is moved to the 'uploads' folder.

    """

    file = listdir(paths['content_preprocessing_path'])[0]
    formatted_file = re.sub("[^a-zA-Z0-9 \n\.']", '', file).replace(" ", "_")
    rename(paths['content_preprocessing_path'] + file, paths['content_preprocessing_path'] + formatted_file)

    mimetypes.init()
    mimestart = mimetypes.guess_type(formatted_file)[0]

    if mimestart is not None:
        mimestart = mimestart.split('/')[1]

        if mimestart == "jpeg" or mimestart == "png":
            scaleImage(formatted_file)

        elif mimestart == "gif":
            scaleVideo(formatted_file)

        elif mimestart == "mp4":
            scaleVideo(formatted_file)

        else:
            print("File type not found.")
