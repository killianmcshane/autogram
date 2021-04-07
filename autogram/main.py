from defines import getPaths
import contentUploader
import imgurUploader
import contentScale
from os import listdir

paths = getPaths()
post_frequency = 4  # (in hours)

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

