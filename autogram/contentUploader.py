from defines import getPaths, getInstagramCreds, makeApiCall
from os import path, listdir
import time

insta_creds = getInstagramCreds()
paths = getPaths()


def uploadVideoToInstagram(url, title):
    """
    Fetches the titles, authentication credentials & URLs that were uploaded to Imgur,
    so that the Instagram Graph API can publish the video content to Instagram.

    Don't forget to change the hashtags and final caption in videoMediaObjectEndpointParams['caption'].

    :param url: The video url of our content.
    :param title: The video title of our content.
    """

    hashtags = " #dankmemes #memes #meme #edgymemes #offensivememes #cutememes #explore #darkhumor #comedy #fortnite #style #offensive #cringymemes #wholesomememes #darkmemes #surrealmemes #deepfriedmemes"

    # Using the URL and title, we form a 'video object'.

    videoMediaObjectEndpoint = insta_creds['endpoint_base'] + insta_creds['instagram_account_id'] + '/media'

    videoMediaObjectEndpointParams = dict()
    videoMediaObjectEndpointParams['access_token'] = insta_creds['access_token']
    videoMediaObjectEndpointParams['video_url'] = str(url)
    videoMediaObjectEndpointParams['caption'] = (str(title) + " @ai.replicant " + hashtags)
    videoMediaObjectEndpointParams['media_type'] = "VIDEO"

    videoMediaObjectResponseArray = makeApiCall(videoMediaObjectEndpoint,  videoMediaObjectEndpointParams, "POST")

    videoMediaObjectStatusCode = 'IN_PROGRESS'

    # Using the 'video object', we obtain a 'media object' and wait for its status
    # to update from 'IN_PROGRESS' to 'FINISHED'.
    while (videoMediaObjectStatusCode != 'FINISHED'):
        videoMediaObjectStatusEndpoint = insta_creds['endpoint_base'] + videoMediaObjectResponseArray['json_data']['id']
        videoMediaObjectStatusEndpointParams = dict()
        videoMediaObjectStatusEndpointParams['fields'] = 'status_code'
        videoMediaObjectStatusEndpointParams['access_token'] = insta_creds['access_token']
        videoMediaObjectResponseArray = makeApiCall(videoMediaObjectStatusEndpoint, videoMediaObjectStatusEndpointParams, 'GET')
        videoMediaObjectStatusCode = videoMediaObjectResponseArray['json_data']['status_code']
        time.sleep(3)

    # We're now ready to publish the content to Instagram.
    videoMediaObjectId = videoMediaObjectResponseArray['json_data']['id']
    publishVideoEndpoint = insta_creds['endpoint_base'] + insta_creds['instagram_account_id'] + '/media_publish'

    publishVideoEndpointParams = dict()
    publishVideoEndpointParams['creation_id'] = videoMediaObjectId,
    publishVideoEndpointParams['access_token'] = insta_creds['access_token']
    publishVideoResponseArray = makeApiCall(publishVideoEndpoint, publishVideoEndpointParams, 'POST')

    print("Posting video: [", title, "] to Instagram. \n")


def uploadImageToInstagram(url, title):
    """
    Fetches the titles, authentication credentials & URLs that were uploaded to Imgur,
    so that the Instagram Graph API can publish the video content to Instagram.

    Don't forget to change the hashtags and final caption in videoMediaObjectEndpointParams['caption'].

    :param url: The image url of our content.
    :param title: The image title of our content.
    """
    imagesEndpointFormat = 'https://graph.facebook.com/v5.0/{ig-user-id}/media?image_url={image-url}&caption={caption}&access_token={access-token}'

    hashtags = " #dankmemes #memes #meme #edgymemes #offensivememes #cutememes #explore #darkhumor #comedy #fortnite #style #offensive #cringymemes #wholesomememes #darkmemes #surrealmemes #deepfriedmemes"

    # Using the URL and title, we form a 'video object'.

    imageMediaObjectEndpoint = insta_creds['endpoint_base'] + insta_creds['instagram_account_id'] + '/media'

    imageMediaObjectEndpointParams = dict()
    imageMediaObjectEndpointParams['access_token'] = insta_creds['access_token']
    imageMediaObjectEndpointParams['image_url'] = str(url)
    imageMediaObjectEndpointParams['caption'] = (str(title) + " @ai.replicant " + hashtags)
    imageMediaObjectEndpointParams['media_type'] = "IMAGE"

    imageMediaObjectResponseArray = makeApiCall(imageMediaObjectEndpoint, imageMediaObjectEndpointParams, "POST")

    imageMediaObjectStatusCode = 'IN_PROGRESS'

    # Using the 'image object', we obtain a 'media object' and wait for its status
    # to update from 'IN_PROGRESS' to 'FINISHED'.
    while (imageMediaObjectStatusCode != 'FINISHED'):
        imageMediaObjectStatusEndpoint = insta_creds['endpoint_base'] + imageMediaObjectResponseArray['json_data']['id']
        imageMediaObjectStatusEndpointParams = dict()
        imageMediaObjectStatusEndpointParams['fields'] = 'status_code'
        imageMediaObjectStatusEndpointParams['access_token'] = insta_creds['access_token']
        imageMediaObjectResponseArray = makeApiCall(imageMediaObjectStatusEndpoint,
                                                    imageMediaObjectStatusEndpointParams, 'GET')
        imageMediaObjectStatusCode = imageMediaObjectResponseArray['json_data']['status_code']
        time.sleep(3)

    # We're now ready to publish the content to Instagram.
    imageMediaObjectId = imageMediaObjectResponseArray['json_data']['id']
    publishImageEndpoint = insta_creds['endpoint_base'] + insta_creds['instagram_account_id'] + '/media_publish'

    publishImageEndpointParams = dict()
    publishImageEndpointParams['creation_id'] = imageMediaObjectId,
    publishImageEndpointParams['access_token'] = insta_creds['access_token']
    publishImageResponseArray = makeApiCall(publishImageEndpoint, publishImageEndpointParams, 'POST')

    print("Posting image: [", title, "] to Instagram. \n")


def postContent(url, title, post_frequency):
    n = post_frequency * 3600

    if ".mp4" in (path.splitext(url)[1]):
        uploadVideoToInstagram(url, title)

    else:
        uploadImageToInstagram(url, title)

    if len(listdir(paths['content_upload_path'])) != 0:
        print("Uploading next image to Instagram in " + str(post_frequency) + " hours.")
        time.sleep(n)
