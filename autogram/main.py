from defines import getPaths
import argparse
import contentUploader
import imgurUploader
import contentScale
from os import listdir

parser = argparse.ArgumentParser(description="Post Frequency")
parser.add_argument("-f", help="The post frequency (in hours).", type=int)

paths = getPaths()
post_frequency = parser.parse_args()    # (in hours)

while len(listdir(paths['content_preprocessing_path'])) != 0:
    contentScale.scaleContent()

if len(listdir(paths['content_preprocessing_path'])) == 0:
    print("Content pre-processing complete.")

while len(listdir(paths['content_upload_path'])) != 0:
    imgurUploader.uploadContentToImgur()
    url, title = imgurUploader.fetchURL()
    contentUploader.postContent(url, title, post_frequency)

    if len(listdir(paths['content_upload_path'])) == 0:
        print("Content uploading complete.")

