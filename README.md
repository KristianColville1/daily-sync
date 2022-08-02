# Daily Sync

Developer: Kristian Colville

[Visit this website](https://daily-sync123.herokuapp.com/)

<br>

## Table of Contents

* [Project Goals](#project-goals)
    * [User Goals](#user-goals)
    * [Site Owners Goals](#site-owners-goals)
* [User Experience](#user-experience)
    * [Target Audience](#target-audience)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
    * [User Stories](#user-stories)
* [Technologies & Tools](#technologies--tools)
* [Design](#design)
    * [Color Scheme](#color-scheme)
    * [Typography](#typography)
    * [Structure](#structure)
        * [Wireframes](#wireframes)
* [Information Architecture](#information-architecture)
    * [Database](#database)
    * [Data Relationships](#data-relationships)
    * [Data Modeling](#data-modeling)
    * [Flow Charts](#flow-charts)
* [Features](#features)
* [Testing](#testing)
* [Validation](#validation)
* [Bugs](#bugs)
* [Development & Deployment](#deployment--deployment)
    * [Version Control](#version-control)
    * [Cloning this Repository](#cloning-this-repository)
    * [Heroku](#heroku)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

## Project Goals

The goal of this project was to create a social media website that takes advantage of good UX design principles and can clearly indicate to a global audience it's purpose.

### User Goals

- Create a social media account on Daily Sync
- Add friends, expand a network and post content that reaches my network
- Have the ability to personalize a profile
- Have the ability to message friends and family

### Site Owners Goals

- Create a social media website that has the look and presentation of an experienced brand
- Allow users to use create, read, update and delete functionality throughout the website to keep people engaged in a meaningful and interactive way
- Provide authority for content that might offend or discriminate to ensure users that this is what family friendly social media website looks like
- Build a responsive and accessible website for a wide audience and build it with the latest tools and technology this world has to offer
- Bring attention to detail and provide a great user experience

## User Experience
### Target Audience
### User Requirements and Expectations
### User Stories

| Issue ID | User Story |
|---|---|
|[#1](https://github.com/KristianColville1/daily-sync/issues/1)| As a user I can navigate around the website when I am logged in so that I find what I am looking for within the website |
|[#2](https://github.com/KristianColville1/daily-sync/issues/2)| As a new user I can identify the purpose of this website so that I can choose whether I want to sign up for this website if it interests me |
|[#3](https://github.com/KristianColville1/daily-sync/issues/3)| As a user I can create a post so that I can notify my network of my activity and share experiences |
|[#4](https://github.com/KristianColville1/daily-sync/issues/4) | As a new user I can create an account so that I can save my personal information and share it with my network |
|[#5](https://github.com/KristianColville1/daily-sync/issues/5)|As a returning user I can log in and access my account so that I can keep an account on this website|
|[#6](https://github.com/KristianColville1/daily-sync/issues/6)|As a user I can click on a post in order to view it differently so that I can expand the post and see additional information such as all the comments/ conversations within a post|
|[#7](https://github.com/KristianColville1/daily-sync/issues/7)|As a user I can create a comment on a post so that I can express myself and interact with my network|
|[#8](https://github.com/KristianColville1/daily-sync/issues/8)|As a user I can like or unlike a post so that I can share my opinion and appreciation for content on the website created by my network that I like|
|[#9](https://github.com/KristianColville1/daily-sync/issues/9)|As a registered user I can I can create my own profile so that I can share my personal information with my network and help others to identify me within the social media website|
|[#10](https://github.com/KristianColville1/daily-sync/issues/10)|As a registered user I can use a search mechanism so that I can find things like people or groups|
|[#11](https://github.com/KristianColville1/daily-sync/issues/11)|As a registered user I can add my friends so that I can contact them, and view their profiles and posts|
|[#12](https://github.com/KristianColville1/daily-sync/issues/12)|As a registered user I can quickly identify that I have new notifications so that I can act accordingly and respond to notifications like comments on a post, people liking my posts or messages from friends|
|[#16](https://github.com/KristianColville1/daily-sync/issues/16)| As a user I can check how many hours or days since a post was created so that I understand the time frame when a particular post was created and can identify between new and old content |
|[#17](https://github.com/KristianColville1/daily-sync/issues/17)| As a registered user I can upload a photo to use on my profile as a profile picture so that I can help others identify me on the network and have the ability to add more personalization |
|[#19](https://github.com/KristianColville1/daily-sync/issues/19)| As a user I can report a post to inform the admin of the site of content that might have bad intentions and be clearly identified as a misuse of the purpose of the website so that I can enjoy a pleasant experience on the website free from bad actors and possible malicious content |
|||
|||
|||
|||

## Technologies & Tools
## Design
### Color Scheme
### Typography
### Structure
#### Wireframes
## Information Architecture

### Database
### Data Relationships
### Data Modeling

#### Models

In no particular order these are the following models created for the Daily Sync web app.

1. Posts

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
| Author | **author** | ForeignKey | User, on_delete=models.CASCADE, related_name="user_posts", null=True |
|Title| **title**| TextField |max_length=200|
|Slug| **slug** | AutoSlugField |populate_from='title', unique_with='author'|
|Content| **content** | TextField |max_length=500|
|Created on| **created_on** | DateTimeField |auto_now_add=True|
|Updated on| **updated_on** | DateTimeField |auto_now_add=True|
|Edited| **edited** | BooleanField |default=False|
|Likes| **likes** | ManyToManyField |User, related_name='post_likes', blank=True|
| Status| **status** | IntegerField |choices=STATUS, default=1|

<br>

2. Comments

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|||||

<br>

3. Messages

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|||||

<br>

4. Profiles

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|||||

<br>

### Flow Charts

## Features
## Testing
## Validation

## Bugs

| Issue ID | Bug | Fix |
|---|---|---|
| [#13](https://github.com/KristianColville1/daily-sync/issues/13) |'auth.User.none' showing in place of where the number of likes should be Should be blank if not a number | Added count() to function call on count likes in post model to display a number |
| [#14](https://github.com/KristianColville1/daily-sync/issues/14) | An issue with migrating the comment model in posts/models.py. Planned to migrate new changes and it's refusing to do so because of the name field not having a default. My observation and knowledge tell me this is incorrect as I should not need a default on the name field | I found a simple fix from stack overflow suggesting deleting all migrations as this is a common issue encountered when working with django and to not delete the folder or __init__.py file and it solved the issue |
|[#15](https://github.com/KristianColville1/daily-sync/issues/15) | Unable to delete posts in admin after creating comment model | Temporally removed comment model and then deleted all posts and added back all comment modal data, comment post ID was causing the issue |
|[#18](https://github.com/KristianColville1/daily-sync/issues/18) | Unable to create a post that has the same title as a published post | I thought the issue was with the slug but after removing unique=true from the title variable in the post model this helped fix posting new posts with the same title but with a unique slug link |
||||
||||
||||
||||

## Development & Deployment
### Version Control
I used [Visual Studio Code](https://code.visualstudio.com/) as a local repository and IDE & [GitHub](https://github.com/) as a remote repository.

1. Firstly, I needed to create a new repository on Github [daily-sync](https://github.com/KristianColville1/daily-sync).
2. I opened that repository on my local machine by copying the URL from that repository and cloning it from my IDE for use.
3. Visual Studio Code opened a new workspace for me.
4. I created files and folders to use.
5. To push my newly created files to GitHub I used the terminal by pressing Ctrl + shift + `.
6. A new terminal opened and then I used the below steps.

    - git add (name of the file) *This selects the file for the commit*
    - git commit -m "Commit message: (i.e. Initial commit)" *Allows the developer to assign a specific concise statement to the commit*
    - git push *The final command sends the code to GitHub*

### Cloning this Repository
If you would like to clone this repository please follow the bellow steps.

Instructions:

1. Log into GitHub
2. Navigate to the repository you want to clone
3. Click on the green button labelled 'Code'
4. Copy the URL under the HTTPS option
5. Open an IDE of your choosing that has Git installed
6. Open a new terminal window in your IDE
7. Type this exactly: git clone the-URL-you-copied-from-GitHub
8. Hit Enter

You should have a local copy of the repository to use on your machine.

### Heroku
As a deployment solution I chose [Heroku](https://dashboard.heroku.com).

To deploy a project using Heroku follow these steps:

- Log into heroku
- Go to the heroku dashboard
- Create a new app by selecting 'New'
- Give your application a name and select a preferred location
- Click the 'Create app' button
- If you have config variables in your application
    - Click on settings
    - Click 'Reveal config vars'
    - Input your deployment variables

- If you need specific build packs
    - Click on settings
    - Click on build pack
    - Add your packs as needed (Please be aware that the order matters)
    - No specific build packs were selected for this project as Django used.

- Once these steps are completed
    - Go to the deploy section
    - Select your version control system
    - For Daily Sync, GitHub was selected

- Connect your version control system
- Add your repository
- Connect the app selecting 'connect'
- Either choose automatic deployment or manual deployment
- Once all these steps are completed and the build is successful
    - You can click the 'view' button
    - It will reveal your deployed app
    
[Back to Top](#table-of-contents)