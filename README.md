# Daily Sync

## Table of Contents
* [About](#about)
* [Project Goals](#project-goals)
    * [User Goals](#user-goals)
    * [Site Owners Goals](#site-owners-goals)
* [User Experience](#user-experience-ux)
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


## Information Architecture

### Database
### Data Relationships
### Data Modeling

#### Models

In no particular order these are the following models created for the Daily Sync web app.

1. Posts

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|||||

2. Comments

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|||||

2. Messages

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|||||

4. Profiles

| Name | Database Key | Field Type | Validation |
|---|---|---|---|
|||||

### Flow Charts

## Features
## Testing
## Validation

## Bugs

| Issue ID | Bug | Fix |
|---|---|---|
| [#13](https://github.com/KristianColville1/daily-sync/issues/13) |'auth.User.none' showing in place of where the number of likes should be Should be blank if not a number | Added count() to function call on count likes in post model to display a number |
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