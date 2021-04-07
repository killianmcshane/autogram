# autogram
The autogram script lets you streamline and automate content publishing legally via The Instagram Graph API.

By scaling, padding and converting content to meet Instagram's requirements, it takes all the hard work out of running an Instagram business profile. Simply drop your files into the *'pre-processing'* folder and select your post frequency and let autogram do the rest.

The set-up process may seem tricky but once completed, you'll be effortlessly running an automatic Instagram page in no time.
<br><br><br>

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
<br>

## BEFORE YOU START

**This is essential. If you skip this section, the application will not run.**

Before you can start using the application, the following steps ***must*** be completed as stated in the Instagram Graph API documentation.

||Getting Started | Links | How |
|---|------|---|---|
|`1.`|Create an Instagram **business** account. This **will not work** for other account types.|[Here](https://help.instagram.com/502981923235522 "Instagram Business Account")|[Here](https://i.imgur.com/ExoeMld "Instagram Business Account")|
|`2.`|Create a Facebook page [like so](https://imgur.com/MZu7rNN) & **connect it to your Instagram business account** via the Instagram mobile app. |[Here](https://help.instagram.com/399237934150902 "Connecting Your Page")|[Here](https://i.imgur.com/JQTr0LO "Connecting Your Page")|
|`3.`|Log into Facebook's Developer Site using the same Facebook account used to register the Facebook page in step 2. |[Here](https://developers.facebook.com/docs/development/register/ "Facebook Developer Account")|[Here](https://imgur.com/mbeak12 "Facebook Developer Account")|
|`4.`|Create a developer app, then give it [these](https://github.com/killianmcshane/autogram "App Permissions") permissions through the API Explorer Tool [here](https://developers.facebook.com/tools/explorer/ "Add Permissions Using Explorer Tool"). |[Here](https://developers.facebook.com/docs/development/create-an-app "Developer App")|[Here](https://imgur.com/W83DEWl "Developer App")<br>[Here](https://imgur.com/nyuZqmM "Explorer Tool")<br>[Here](https://imgur.com/PjDuude "Permissions")|
|`5.`|Register an Imgur account, and an Imgur developer app through postman. |[Here](https://apidocs.imgur.com/ "Imgur API")||
|`6.`|Enter your newly obtained details into the *defines.py* file. |||

The steps above can seem somewhat confusing. To help you complete them, I've made a quick tutorial below. I'd strongly recommend that you give it a watch.

e.g. ***[insert image here]***

e.g. ***[insert video here]***

<br>
<br>

## RUN APPLICATION
Simply drag all the files you want to upload into the *'pre-processing'* folder, run the command below.

> ```sh
> python main.py
> ```


Images, GIFs and videos will be automatically scaled, padded and converted to meet Instagram's specifications. Processed content will be moved to the *'uploads'* folder where they will automatically be uploaded to Instagram.

The default post frequency is set to every 4hrs however, you can easily update this by changing it at the top of the *main.py* file.

<br>
<br>

## HOW IT WORKS
The Instagram Graph API only uploads content using URLs hosted from public servers. 

By using Imgur's API, we can automate the generation of these URLs from content on our computers.

The automatic scaling and padding is achieved through the use of FFmpeg, a free, open source command-line software for handling media.
