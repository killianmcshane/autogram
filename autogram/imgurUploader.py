from defines import getImgurCreds, getPaths, getInstagramCreds
from os import path, listdir, mkdir
from imgur_python import Imgur
from datetime import date
import shutil

imgurURL = ""
formattedTitle = ""
paths = getPaths()


def uploadContentToImgur(public="no"):
    """
    Uploads & archives all the files from our 'upload' folder to Imgur so that we can generate
    URLs for the Instagram Graph API's 'publish_content' endpoint.

    """
    global imgurURL, formattedTitle
    imgur_creds = getImgurCreds()
    insta_creds = getInstagramCreds()

    imgur_client = Imgur({
        'client_id': imgur_creds['client_id'],
        'client_secret': imgur_creds['client_secrets'],
        'access_token': imgur_creds['access_token'],
        'expires_in': imgur_creds['expires_in'],
        'token_type': imgur_creds['token_type'],
        'refresh_token': imgur_creds['refresh_token'],
        'account_username': imgur_creds['account_username'],
        'account_id': imgur_creds['account_id']})

    postTitles = listdir(paths['content_upload_path'])

    for i in range(len(postTitles)):
        postTitles[i] = postTitles[i].replace("_", " ")
        postTitles[i] = path.splitext(postTitles[i])[0]

    file = listdir(paths['content_upload_path'])[0]
    file_path = paths['content_upload_path'] + file
    title = postTitles[0]
    content = imgur_client.image_upload(file_path, title, "www.instagram.com/" + insta_creds['ig_username'], disable_audio=0)

    imgurURL = content['response']['data']['link']
    formattedTitle = postTitles[0]

    content_id = content['response']['data']['id']

    # Make it public
    if public == "yes":
        response = imgur_client.gallery_image(content_id, title, 1, 'funny, meme, memes')
    print("Obtaining content URL from Imgur.")

    date_str = str(date.today())
    # Once the publishing finishes, we move the files from 'upload' to 'archive'.
    uploads = paths['content_upload_path']
    archive = paths['content_archive_path']

    if path.exists(archive + date_str + "\\") is False:
        mkdir(archive + date_str + "\\")

    print("Archiving: [" + title + "].")
    postTitles.pop(0)
    shutil.move(uploads + file, archive + date_str + "\\" + file)


def fetchURL():
    """
    Fetches the title and URL of the last post uploaded to Imgur.

    :return imgurURL: The last uploaded URL.
    :return formattedTitle: The last uploaded title.
    """
    if imgurURL == "":
        print("No URLs left to upload.")

    return imgurURL, formattedTitle
