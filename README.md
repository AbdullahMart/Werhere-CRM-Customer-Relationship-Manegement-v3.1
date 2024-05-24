CRM.V2

CRM Project (Customer Relationship Management)

General
Nowadays, many organizations use Google Drive and its components because it offers free options for managing and storing data to some extent. Various organizations conduct a series of processes, including mentoring interviews and project and interview phases, for individuals of refugee origin who want to work in the IT field, and these processes are carried out on Google Drive. To make it easier to keep track of candidates, a user-friendly application has been designed to facilitate tasks such as constantly keeping sessions open on the drive, dealing with the complexity of Excel texts, and quickly accessing the desired data.

User Interface Details
Login Window

![login windows](https://github.com/AbdullahMart/Werhere-CRM-Customer-Relationship-Manegement-v3.1/assets/164740171/902e6048-c0ad-417e-97b9-140fb0838837)


1-)Username and Password
Access should be granted to those with usernames and passwords registered by the main Gmail account user of Google Drive. These credentials are stored in the Users file. If the user's access level is Admin, they should be directed to the Preferences - Admin menu; if the access level is User, they should be directed to the Preferences menu.

A customized login page should be created for the application, containing the following features:

Two separate input elements for username and password.
A login button that reacts to these two pieces of information.
A warning message indicating whether the login was successful or not.
Optionally, another button can be added to close the application and remove the window display.
Customized login windows should be created using consistent background colors, box edge shapes, button properties (hover, pressed, round edges), and different fonts and colors for texts.

Tip: First, place a frame and then place elements on it. You can create dynamic sizes using both the frame and the elements placed on it by using layout and spacer.

Preferences


A-) Preferences Admin


![admin preference menu](https://github.com/AbdullahMart/Werhere-CRM-Customer-Relationship-Manegement-v3.1/assets/164740171/cbeec75f-217e-41b6-bc7a-7d6983cfe550)


1- Applications
The Applications button should direct the admin to the initial application window.

2- Mentor Interview
The Mentor Interview button should direct the admin to the mentor window.

3- Interviews
The Interviews button should direct the admin to the interviews window.

4- Admin Menu
The Admin button should direct the admin to the Admin window.



B-) Preferences

![preference menu](https://github.com/AbdullahMart/Werhere-CRM-Customer-Relationship-Manegement-v3.1/assets/164740171/7c73695f-0401-4eb2-923d-394075c50219)


1- Applications
The Applications button should direct the user to the initial application window.

2- Mentor Interview
The Mentor Interview button should direct the user to the mentor window.

3- Interviews
The Interviews button should direct the user to the interviews window.

Applications

![applications](https://github.com/AbdullahMart/Werhere-CRM-Customer-Relationship-Manegement-v3.1/assets/164740171/4894de6f-28a2-4d1e-bd88-4e53d631a148)


1- Search
A button that enables searching for names and surnames in the text line entered (e.g., entering 'As' should bring up all names starting with 'As' registered in the drive).

2- All Applications
When the All Applications button is clicked, all applications recorded in the applications file on the drive should be displayed on the screen.

3- Assigned Mentor Interviews (Relevant column in the Applications file)
When the Assigned Mentor Interviews button is clicked, individuals who have been assigned a mentor interview after applying should be displayed on the screen.

4- Unassigned Mentor Interviews
When the Unassigned Mentor Interviews button is clicked, individuals who have not yet been assigned a mentor after applying should be displayed on the screen.

5- Duplicate Records Button
When the Duplicate Records Button is clicked, individuals registered with the same name and email address in the Applications file on the drive should be displayed on the screen (only repeated candidates).

6- Previous VIT Control Button
When the Previous VIT button is clicked, all candidates common to either VIT1, VIT2, or the Applications files recorded on the drive should be displayed on the screen. (The purpose here is to see if a candidate has applied to more than one VIT).

7- Unique Records Button
When the Unique Records Button is clicked, candidates who are not common to both VIT1 and VIT2 recorded on the drive should be displayed on the screen.

8- Application Filtering Button
When the Application Filtering Button is clicked, the applications in the Applications file should be filtered and displayed without duplicate records. (If a name is registered more than once, this record should only be displayed once).
(If you wish, you can also implement options 5/6/7/8 using a QComboBox instead of placing separate buttons.)

9- Return to Preferences Screen
When the Return to Preferences Screen button is clicked, the user should return to the Preferences screen.


Mentor

![mentor menu](https://github.com/AbdullahMart/Werhere-CRM-Customer-Relationship-Manegement-v3.1/assets/164740171/f544b4cb-48c8-476d-b414-6ac6897c20ee)

1- Search
A button that enables searching for names and surnames in the text line entered (e.g., entering 'As' should bring up all names starting with 'As' registered in the drive).

2- All Interviews
When the All Interviews button is clicked, all interviews recorded in the Mentor file should be displayed on the screen.

3- Multiple Tabs
Records suitable for the selected preference should be displayed in this tab.

4- Return to Preferences Screen
When the Return to Preferences Screen button is clicked, the user should return to the Preferences screen.


Interviews

![interviews page](https://github.com/AbdullahMart/Werhere-CRM-Customer-Relationship-Manegement-v3.1/assets/164740171/b5db925e-8548-4003-8a97-11b1b38dd9e7)


1- Search
A button that enables searching for names and surnames in the text line entered (e.g., entering 'As' should bring up all names starting with 'As' registered in the drive).

2- Those Sent Project (Relevant column in the Interviews file)
When the Project Sent button is clicked, candidates whose projects have been sent should be displayed on the screen.

3- Received Projects (Relevant column in the Interviews file)
When the Project Received button is clicked, candidates whose projects have been received should be displayed on the screen.

4-Return to Preferences Screen
When the Return to Preferences Screen button is clicked, the user should return to the Preferences screen.


Admin Menu

![admin menu](https://github.com/AbdullahMart/Werhere-CRM-Customer-Relationship-Manegement-v3.1/assets/164740171/1dc98241-602c-4fc3-beb2-07a772668f4b)


1- Event Registration Button
This registration should display events recorded on Google Drive.

2- Mail Button
This button should allow automatic emails to be sent to email addresses registered for the event after events are pulled from the calendar.

3- Table
A table showing the records pulled from Google Calendar.

4- Return to Preferences-Admin Screen Button
When the Return to Preferences-Admin Screen button is clicked, the admin should return to the Preferences-Admin screen.


General Information About the Project Process

* Each team will have 2 mentors.
* We will follow project task management on the "Trello Board."
* Your mentors will track your team work and tasks on Trello.
* You should also add your team mentors to Trello.
* You should hold a minimum 30-minute daily meeting with your team members every day.
* During daily meetings:

* Team members should discuss what they have completed.
* General evaluations about the project.
* Plans for the next day should be discussed.
* There will be lists named after specific dates on Trello. Details, tasks, and to-dos will be kept on this list daily on Trello.

* It is important to follow these steps to complete the project on time.

* Meetings with team mentors will be held on the dates specified below.

* Until the meeting, each step will be completed and moved on to the next step. Each student in the team will present the role they played in that step to the mentor in the meeting.

* After each meeting, the mentors will evaluate whether each team member has progressed.

* After completing the project, an online presentation of the project will be made to your mentors.
  

For the Project to be Completed


* Work in coordination with your mentors.
* Have UML diagrams made.
* Ensure the program runs as an .exe file.
* Prepare the project for presentation on time.
* Store it in GitHub with a README file.
* It is expected to be turned into an article for Medium (optional).

  
Tools to be Used for the Program


* VS Code
* JSON (for data storage)
* UML diagrams
* GitHub
* OOP
* PyQt6 and Qt Designer


Meeting Schedule

1- Online Kick-off Meeting - 12/05/2024
ASSIGN TASKS AND CREATE PROJECT TRACKING, THEN CREATE UML DIAGRAM AND CONTROL LOGIN CONNECTION, ACCESS PREFERENCES MENU AND ADMIN PREFERENCES MENU, AND ACCESS APPLICATIONS, MENTOR, INTERVIEWS, AND ADMIN MENU FROM THE PREFERENCES MENU.

2- Online Mentor Meeting - 15/05/2024
CREATE AND PRINT CODES OF DATA ON THE GOOGLE DRIVE INTERVIEWS PAGE AND MENTOR PAGE

3- Online Mentor Meeting - 18/05/2024
RETRIEVE EVENT RECORDS FROM GOOGLE CALENDAR AND DISPLAY THESE RECORDS IN THE ADMIN MENU, SEND EMAILS TO PEOPLE REGISTERED IN THE EVENT (ADMIN MENU ACTIONS)

4- Online Mentor Meeting - 21/05/2024
CREATE AND PRINT CODES IN THE APPLICATIONS MENU

5- Online Mentor Meeting - 24/05/2024
TURN THE PROJECT INTO AN ARTICLE (OPTIONAL), CREATE A PRIVATE PROJECT IN YOUR GITHUB ACCOUNT, UPLOAD README, REQUIREMENTS.TXT, AND PROJECT FILES TO GITHUB, PREPARE FOR THE PROJECT PRESENTATION

6- Final Presentation Online - 25/05/2024


Project Steps

Step 1:

* ASSIGN TASKS
* CREATE PROJECT TRACKING (TRELLO)
* DESIGN INTERFACES FOR PROJECT PAGES
* CREATE UML DESIGN (PLAN AND DRAW)
  
  Tips:

    * THIS STEP CAN BE SHARED AMONG GROUP MEMBERS.
    * THE INTERFACES IN THE PROJECT PAGES WERE DESIGNED TO GIVE IDEAS, YOU CAN ADD COLOR CHOICES, DIFFERENT DESIGNS, AND BUTTON SHADOWS OR ADD DIFFERENT VISUAL ELEMENTS.
    * FOR UML DRAWING: https://lucid.app or https://app.diagrams.net/
    * FOR PROJECT TRACKING: https://trello.com/
      
Step 2:

* WHEN THE PROGRAM IS USED, IT SHOULD BE ABLE TO PULL RELATED DATA FROM GOOGLE DRIVE AND GOOGLE CALENDAR WITHOUT ISSUES.
* COMPLETE THE REQUIRED INFORMATION IN THE ADMIN MENU.
  
  Tips:

    * THIS STEP CAN ALSO BE SHARED AMONG GROUP MEMBERS.
    * TO PULL GOOGLE CALENDAR DATA, YOU NEED TO ADD A FEW EVENTS TO THE CALENDAR AND ENTER TIME AND EMAIL ADDRESS FOR THESE EVENTS.
    * DOCUMENT DATA CAN BE PULLED WITH GSPREAD. CALENDAR DATA CAN BE PULLED WITH GOOGLEAPI, GOOGLECALENDARAPI, OR GOOGLE OAUTH2CLIENT SERVICES. USEFUL WEBSITES: https://console.cloud.google.com, https://developers.google.com/calendar/overview
    * FOR REQUIREMENTS FILE: pip freeze > requirements.txt (https://learn.microsoft.com/en-us/visualstudio/python/managing-required-packages-with-requirements-txt?view=vs-2022)
      
Step 3:

* COMPLETE THE REQUIREMENTS IN WINDOW DEFINITIONS.
* TEST TO ENSURE IT WORKS SMOOTHLY.
* CREATE REQUIREMENTS AND README FILES
* CREATE USAGE SCENARIO (TURN INTO ARTICLE)
* UPLOAD ALL PROJECT FILES TO GITHUB ACCOUNTS.
  
Final Step:

* MAKE THE PRESENTATION
