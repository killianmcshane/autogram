# autogram
Autogram lets you streamline and automate content publishing legally via The Instagram Graph API.

By scaling, padding and converting content to meet Instagram's requirements, it takes all the hard work out of running an Instagram business profile. Simply drop your files into the *'pre-processing'* folder and select your post frequency and let autogram do the rest.
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



## REQUIREMENTS
In the autogram directory, run the following command:

> ```sh
> pip install -r requirements.txt
> ```

Download and install FFMPEG [here](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z). 

Add its executable path to the defines.py file under the paths dictionary.

e.g. ***[insert image here]***



## BEFORE YOU START

**This is essential. If you skip this section, the application will not run.**

Before you can start using the application, the following steps ***must*** be completed as stated in the Instagram Graph API documentation.

||Getting Started |Links|
|---|------|---|
|`1.`|Create an Instagram **business** account. |[Here](https://help.instagram.com/502981923235522)|
|`2.`|Create a Facebook page & **connect it to your Instagram business account** via the Instagram mobile app. |[Here](https://help.instagram.com/399237934150902)|
|`3.`|Apply for a Facebook developer account with the same Facebook account used to register the Facebook page in step 2. |[Here](https://developers.facebook.com/docs/development/register/)|
|`4.`|Register a Facebook developer app with *'basic'* settings configured.|[Here](https://developers.facebook.com/docs/development/create-an-app)|

The steps above can seem somewhat confusing. To help you complete them, I've made a quick tutorial below. I'd strongly recommend that you give it a watch.

***[insert video here]***



## RUN APPLICATION
Simply drag all the files you want to upload into the 'pre-processing' folder, run the command below.

> ```sh
> python main.py
> ```


Images, GIFs and videos will be automatically scaled, padded and converted to meet Instagram's specifications. Processed content will be moved to the 'uploads' folder where they will automatically be uploaded to Instagram.

The default post frequency is set to 4hrs however, you can easily update this by editing it at the top of main.py file.
<br><br><br>
