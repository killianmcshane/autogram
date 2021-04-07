import requests
import json


def getPaths():
    """
    Initialises directory paths.

    :return paths: Dictionary paths needed globally.
    :rtype: Dictionary
    """
    paths = dict()
    # Update the path below to where you saved autogram to on your computer.
    paths['base_path'] = 'C:\\Users\\Killian\\Documents\\autogram\\'

    paths['content_upload_path'] = paths['base_path'] + 'content\\upload\\'
    paths['content_archive_path'] = paths['base_path'] + 'content\\archive\\'
    paths['content_preprocessing_path'] = paths['base_path'] + 'content\\preprocessing\\'
    paths['contentID_path'] = paths['base_path'] + 'content\\contentIDs.txt'
    paths['ffmpeg'] = paths['base_path'] + "ffmpeg\\bin\\ffmpeg.exe"

    return paths


def getInstagramCreds():
    """
    Initialises Instagram credentials required for use in the scripts.

    :return insta_creds: Dictionary credentials needed globally.
    :rtype: Dictionary
    """

    insta_creds = dict()
    # Fill in the details below.
    insta_creds['client_id'] = ''  # Client ID obtained from basic settings from fb developer app.
    insta_creds['client_secret'] = ''  # Client Secret obtained from basic settings from fb developer app.
    
    # Enter your Short Lived Access Token below.
    # You need to generate a Long Lived Access Token from your
    # Short lived Access Token by running getLongLivedAccessToken.py
    # Simply paste the Long Lived Token over the short one below.
    insta_creds['access_token'] = ''  

    insta_creds['page_id'] = ''  # Get your Page ID by running getInstagramAccount.py
    insta_creds['instagram_account_id'] = ''  # Get your Business ID by running getInstagramAccount.py
    insta_creds['ig_username'] = ''  # Just your IG username

    # You can ignore these.
    insta_creds['graph_domain'] = 'https://graph.facebook.com/'
    insta_creds['graph_version'] = 'v10.0'
    insta_creds['endpoint_base'] = insta_creds['graph_domain'] + insta_creds[
                'graph_version'] + '/'
    insta_creds['debug'] = 'no'

    return insta_creds


def getImgurCreds():
    """
    Initialises Imgur credentials required for use in the scripts.

    :return imgur_creds: Dictionary imgur_creds: credentials needed globally.
    :rtype: Dictionary
    """

    imgur_creds = dict()
    # Fill in the details below; you get all of these after the postman setup.
    imgur_creds['client_id'] = ''
    imgur_creds['client_secrets'] = ''
    imgur_creds['access_token'] = ''
    imgur_creds['expires_in'] = '315360000'
    imgur_creds['token_type'] = 'bearer'
    imgur_creds['refresh_token'] = ''
    imgur_creds['account_username'] = ''
    imgur_creds['account_id'] = ''

    return imgur_creds


# You can ignore these last two functions.
def makeApiCall(url, endpointParams, type='GET', debug='no'):
    """
    Request data from endpoint with params.

    :param url: Endpoint we're requesting.
    :param endpointParams: Endpoint parameters we're passing.
    :param type: GET or POST.
    :param debug: Verbose error option.
    :return response: Returns content.
    :rtype: Dictionary
    """
    response = dict()

    if (type == 'POST'):
        data = requests.post(url, endpointParams) # make post request

        response['url'] = url  # url we are hitting
        response['endpoint_params'] = endpointParams  # parameters for the endpoint
        response['endpoint_params_pretty'] = json.dumps(endpointParams, indent=4)  # pretty print for cli
        response['json_data'] = json.loads(data.content)  # response data from the api
        response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)  # pretty print for cli

    elif (type == 'GET'):
        data = requests.get(url, endpointParams) # make get request

        response['url'] = url  # url we are hitting
        response['endpoint_params'] = endpointParams  # parameters for the endpoint
        response['endpoint_params_pretty'] = json.dumps(endpointParams, indent=4)  # pretty print for cli
        response['json_data'] = json.loads(data.content)  # response data from the api
        response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)  # pretty print for cli



    if ('yes' == debug):  # display out response info
        displayApiCallData(response)  # display response

    return response  # get and return content


def displayApiCallData(response):
    """
    Print out to cli response from api call

    :param response: The verbose error response.
    :return: Prints error.
    :rtype: Str
    """

    print("\nURL: ")
    print(response['url'])  # display url hit
    print("\nEndpoint Params: ")  # title
    print(response['endpoint_params_pretty'])  # display params passed to the endpoint
    print("\nResponse: ")  # title
    print(response['json_data_pretty'])  # make look pretty for cli