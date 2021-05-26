![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# Events-Corner
Our Project,Events Corner, is a web portal where the users can create and register for the events.The user has to login or register in the site inorder to get access to site settings. The site as of now have the functionality to create event, update event or delete event if created by the user , register for the event(can only register once for an event), profile where the registered events are visible,and a usre login logout and register system.  
## Team members
1. Alfin Benild [https://github.com/AlfinBenild]
2. Hemanth Sagar J C[https://github.com/sagar1109]
3. Manu Raiphil [https://github.com/manuraiphil]
## Team Id
BFH/recH89eKsHINlKsTu/2021
## Link to product walkthrough
[https://www.loom.com/share/416bf0724b70444a8bb13dc0a506e01f]
## How it Works ?
The home page consits of mainly two options, create event or register for event. For either,creating or registering for an event the user has to login if already registered or register if a new user.The buttons are provided in the top right corner. Once logged in, if the user chose to create event, they will be directed to the page where the user is asked to enter the details of the event, all the fields are mandatory,then to post it.the user can either update or delete the event by going to the details page of the event. If the user wishes to register for an event,the event button is present on top left corner where the user can see the events registered in the portal by all the users.By clicking on the title, the user can view the whole description and details regarding the event. the register button directs the user to a form where details are asked and filing submitting it confirms the registration. if the user have already registered then they cannot register again. if the user wishes to know the registered events, they can click on the profile button and see the events registered.Finally , the user can logout using the button logout in the top right corner. 


## Libraries used
asgiref==3.3.4  
dj-database-url==0.5.0  
Django==3.2.3  
django-crispy-forms==1.11.2  
django-heroku==0.3.1  
django-phonenumber-field==5.1.0  
gunicorn==20.1.0  
phonenumbers==8.12.23  
Pillow==8.2.0  
psycopg2==2.8.6  
pytz==2021.1  
sqlparse==0.4.1  
whitenoise==5.2.0  
## How to configure
This site can be found at https://events-corner.herokuapp.com/
## How to Run
This site can be run using "python manage.py runserver" command while in the directory with manage.py file.
