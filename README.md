# habit-forma

### Simple habit tracking app

The intended purpose of the app is to allow users to enter habits that they wish to develop and mark them as complete each day to keep track of progress.

## URL

The app can be accessed via the following link: https://habit-forma-32fb84497168.herokuapp.com/

## Planning

A project board has been used to track must-have, should-have and could-have items, and to aid in application on AGILE methodology:

A screenshot of the board, in progress, is provided below:

![image](https://github.com/user-attachments/assets/f28ef02d-3db4-4d77-8df3-fe45f9737fc3) 

The board is available here:  https://github.com/PeaJaySee/habit_project


Below are some early diagrams of how I intended the habit entry form and the list view of habits to look:

![hfp-diagram](https://github.com/user-attachments/assets/8c520749-071e-4e6a-9928-2d5664fec402)



## Description

This app is intended to help people to develop new habits by allowing them to enter the habit description and indicate when they have completed the habit to track their progress. 

The app as an MVP will have a list view of entered habits, a form to enter new habits, and the ability to delete or edit existing habits.

Screenshot of MVP:

![image](https://github.com/user-attachments/assets/328c4a9e-1727-41f8-a818-259970934ad9)


A possible future feature would be visual representation of progress (e.g. a graph showing progress over time).

## Colour Palette

![image](https://github.com/user-attachments/assets/d042dc67-9447-47f5-8dcd-056eb41dac99)


## Technologies Used / Acknowledgements

The site was created primarily using Django, HTML and CSS. 

Bootstrap and Copilot AI have been used to assist and to generate some of the content (particularly user stories and acceptance criteria for the project board) and to provide the framework. Copilot has also been used to troubleshoot through suggestions in the chat window and to provide guidance with aspects such as setting up user authentication and adding CRUD functionality via the relevant forms and buttons. 

In terms of code generation, the majority of JS code was AI generated, then checked for errors / conflicts before being added. AI guidance was used in setting up back end admin. authentication and account set-up functionality.

Identification and resolution of bugs and code errors was augmented by AI. Prompts were used, along the lines of "Why is x (aspect of the app) behaving in y (manner)?". A valuable lesson regarding blind reliance on AI for bug fixes was learned along the way - a database issue was exacerbated by implementing an AI suggestion of file deletion. The timely intervention of a human tutor remedied this!

Copilot was asked for advice on creation of an app with a tabular layout and on how to provide user feedback (e.g. pop-ups asking for confirmation of data deletion). UX suggestions from AI that were considered in the design of the app were a minimalist design, with plenty of white space to keep the interface feeling approachable and the use of universally recognised icons (e.g. a bin for deletion, a tick to confirm, a cross to cancel).

As previously mentioned, AI aided workflow by helping with the generation of user stories, acceptance criteria and related tasks. In the planning stage, Copilot provided advice on potential features that could be implemented beyond MVP.

Bootstrap was invaluable in styling the app and making it responsive across different devices; an example of this being the table of habits on the home page.

Fonts were imported from Google Fonts, and the logo icon and action button icons were sourced from FontAwesome.

Thanks to Alexander Tastad for general support and advice, particularly around documentation. Also thanks to John Rearden for help with database issues close to deadline.

## Testing / Validation

CSS checked with W3C validator:

![image](https://github.com/user-attachments/assets/ab6c15a2-44ed-46db-be75-2341885bd47d)

Automated testing was created for both models and views, based on copilot suggestions:

![image](https://github.com/user-attachments/assets/464ffe9d-bac1-40ae-87e6-104dd782fb86)

Lighthouse scores for the main page were as follows:

Desktop:

![image](https://github.com/user-attachments/assets/81106db1-16d7-41df-98ae-353b9fc42bac) 

Functionality has been tested with creation of test users:

- Registration, Login and Logout work as expected
- Creation of new records works and required fields are active and prevent creation if not complete
- Updating records works
- Deletion of records working, and confirmation message pops up when delete button is pressed
- Task complete button works and is disabled until next day to prevent duplicate recording of completion
- Only logged in user's habits are shown, and main page is personalised with user name

Mobile:

![image](https://github.com/user-attachments/assets/4e6ba896-07ec-476c-84b2-c7902b47e770)



