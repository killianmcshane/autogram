# autogram
The autogram script lets you streamline and automate content publishing legally via The Instagram Graph API.

By scaling, padding and converting content to meet Instagram's requirements, it takes all the hard work out of running an Instagram business profile. Simply drop your files into the *'pre-processing'* folder and select your post frequency and let autogram do the rest.

The set-up process may seem tricky but once completed, you'll be effortlessly running an automatic Instagram page in no time.

<br><br>

<h1 align="center">
	<img width="140" src="images/heart3.png" alt="Donations"><p>
</h1>
<p align="center";style="font-size:12px">
	<b> If you like the application, use the link below to help support me with the cost of my tuition!</b>
	<br><br>
	<b> Even donating as little as a coffee means so much to me. 😇</b>
</p>

<p align="center">
	<a href="https://www.paypal.com/donate?hosted_button_id=924J8K3PC7NR6"><img width="140" src="https://img.shields.io/badge/Donate-PayPal-blue.svg" alt="Badge"></a>
<br><br>
</p>

<br>
<br>

## REQUIREMENTS
In the autogram directory, run the following command:

> ```sh
> pip install -r requirements.txt
> ```

<br>

>
> unzip ffmpeg.zip to the autogram directory.
>

<br>
<br>

## BEFORE YOU START

**This is essential. If you skip this section, the application will not run.**

Before you can start using the application, the following steps ***must*** be completed as stated in the Instagram Graph API documentation.

||Getting Started | Links | Pics |
|---|------|---|---|
|`1.`|Create an Instagram account and switch it to **business**. This **will not work** for other account types.|[Here](https://help.instagram.com/502981923235522 "Instagram Business Account Link")|[Here](https://i.imgur.com/ExoeMld "Instagram Business Account")|
|`2.`|Create a Facebook page [like so](https://imgur.com/MZu7rNN) & **connect it to your Instagram business account** via the Instagram mobile app. |[Here](https://help.instagram.com/399237934150902 "Connecting Your Page Link")|[Here](https://i.imgur.com/JQTr0LO "Connecting Your Page")|
|`3.`|Log into Facebook's Developer Site with the same Facebook account used to register the Facebook page in step 2. |[Here](https://developers.facebook.com/docs/development/register/ "Facebook Developer Account Link")|[Here](https://imgur.com/mbeak12 "Facebook Developer Account")|
|`4.`|Set up a Facebook Developer App and save your Facebook/Instagram Client ID and Client Secret somewhere. |[Here](https://developers.facebook.com/docs/development/create-an-app "Developer App Link")|[Here](https://imgur.com/W83DEWl "Developer App")|
|`5.`|Give your new developer app [these](https://github.com/killianmcshane/autogram "App Permissions") permissions through the API Explorer Tool. |[Here](https://developers.facebook.com/tools/explorer/ "Add Permissions Using Explorer Tool Link")|[Here](https://imgur.com/PjDuude "Permissions")|
|`6.`|Register for Imgur, you'll then be asked to set up a developer app. Set the callback URL to 'https://oauth.pstmn.io/v1/browser-callback'. Save your Imgur Client ID and Client Secret somewhere. |[Here](https://api.imgur.com/oauth2/addclient "Imgur API Link")|[Here](https://imgur.com/BSrUIxx "Imgur's API")|
|`7.`|Click the link, select 'Run In Postman' (top right) and obtain the access token for your Imgur application by selecting Type: OAuth2.0 .|[Here](https://apidocs.imgur.com/ "Postman Link")|[Here](https://imgur.com/Si6J0Ny "Postman For Imgur")<br>[Here](https://imgur.com/JtjfW5O "Type")|
|`8.`|Enter a name for your token. For the Auth URL enter: 'https://api.imgur.com/oauth2/authorize' and for the Access Token URL enter: 'https://api.imgur.com/oauth2/token'. Finally, enter your Imgur Client ID and Client Secret from before and hit enter.||[Here](https://imgur.com/kYqDV7C "Generating Your Access Token")|
|`9.`|After this, you'll be given your Imgur Access Token, save all the information somewhere. |||
|`10.`|Enter all your newly obtained Instagram and Imgur details into the *defines.py* file. See image below! |||
<br>
<br>


> Updating defines.py with the newly obtained API credentials.


![defines](https://user-images.githubusercontent.com/63755344/113907439-46fce200-97cd-11eb-8e60-7f8dd82d969a.png)


<br>
The steps above can seem somewhat confusing. To help you complete them, I'm in the process of making a quick tutorial. I'd strongly recommend that you give it a watch when I've published it.

w.i.p. ***[insert video here]***

<br>
<br>

## RUNNING THE APPLICATION
Simply drag all the files you want to upload into the *'pre-processing'* folder, run the command below.

> ```sh
> python main.py -f 4
> ```

The *'-f'* argument sets the post frequency (in hours).

Images, GIFs and videos will be automatically scaled, padded and converted to meet Instagram's specifications. Processed content will be moved to the *'uploads'* folder where they will automatically be uploaded to Instagram.


<br>
<br>

## HOW IT WORKS
The Instagram Graph API only uploads content using URLs hosted from public servers. 

By using Imgur's API, we can automate the generation of these URLs from content on our computers.

The automatic scaling and padding is achieved through the use of FFmpeg, a free, open source command-line software for handling media.
