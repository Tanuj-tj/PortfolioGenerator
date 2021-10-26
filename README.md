# PortfolioGenerator

**Example of urls.py file :**

![005 URLs and Views](https://user-images.githubusercontent.com/63875409/135449864-f52055ba-fb9d-48f5-99d8-6367ef735277.jpg)

**Section 2**

* Specify views.py in main project folder if required
* Specify urls.py in the app folder as it cleans up the code 
* Use include inside urls.py on main project folder .
* Template foder can be created either seperately and specifies under DIRS(inside settings) or can be created seperately inside each app .


Get familier with
* views and urls
* Templates
* Jinja syntax => include , extends


---------
**Section 3**

* Creating a super user means we now have a admin level permission and we can access the admin panel

* We can perform basic crud operations with the help of admin panel .

----

**Example of Django Models :**

![image](https://user-images.githubusercontent.com/63875409/137577269-9e3b5c8d-c1f4-4431-a7cc-43e6215f0d53.png)

* Once we migrate our Model class it turns into a database table 

* auto_now_add=True Means whenever this model instance will be created generate a DateTime accordingly

* Create a model class -> makemigrations -> migrate -> register the model with the admin panel 


----

**Relationships**

![image](https://user-images.githubusercontent.com/63875409/137578318-6abd3221-e28b-47cf-888d-09e2c03a8b91.png)

* One to Many Example 

![image](https://user-images.githubusercontent.com/63875409/137578588-003dde6f-2b61-47dc-a06b-325172eab861.png)

* Many to Many Example

![image](https://user-images.githubusercontent.com/63875409/137578718-f99acf7d-0171-4329-afbb-71b7ed52a19d.png)

![image](https://user-images.githubusercontent.com/63875409/137581078-4d6037f9-83dd-4da4-b57f-12e4d127b19f.png)
----

### How a Standatd Query Works

![image](https://user-images.githubusercontent.com/63875409/137580485-cb7045c0-32b1-4f5d-9735-72d7b778a4b8.png)


----

* CSRF Token ensures that our data wasn't manipulated and it is safe and clean .

**Section 4**

* Static files are any external files like css,js etc .
* create a folder 
static 
    -> images
    -> css
    -> js

* Configure the statuc dir path in settings.py

* Added a featured_image column in project table 

* Configure the media upload path in settings.py

* When we put our project in production then we cannot access the static files so we need to define STATIC_ROOT in settings.py

-> STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
-> After creating the above file we neet to use python manage.py collectstatic command

* So our static files are bundled up but we still need a third party  library to access the files .

* pip install whitenoise , Whitenoise is a library which allows us to access the static files 

----
### Database Schema

![image](https://user-images.githubusercontent.com/63875409/137578201-0f762510-672e-4358-8fc1-8d9af6325318.png)
 
----------


Section 5

(Theam installation)

* Applying Themes to the project

*  {% for tag in projects.tags.all %}
        <span style="border:1px solid grey">{{ tag }}</span>
    {% endfor %}

    Allows us to access many to many relationship

* If more then one vote is there then we will pluralize the vote 
 Vote{{ project.vote_total | pluralize:"s" }}

* Worked with the Themes


----------

Section 6

(Adding more apps)

* Create a new app users

- Configure the app in setting.py file
- Added template->users->profiles.html
- added a function profiles in views.py file which renders the page profiels.html
- create a urls.py file and pass an empty path
- In the main project folders inside urls.py file set the patters users/   

* Profile has one to one relatio with the user 

* Every time we create a user , a profile is automatically generated

* models.py -> Profile Class

* Create a many to one relationship in project to profile by specifing a foreign key in owner column 

* Import the template for users page

*  {{ profile.bio|slice:"150" }} Limit the characters

* Create Skills model inside users app

**Add and render profiles**

* topSkills = profile.skill_set.exclude(description_exact="")
  -> If skills does not have a description do not includ it

* otherSkills = profile.skill_set.filter(description="")
  -> Include the skills which has an empty description

* Error in
```href="{% url 'user-profile' project.owner.id %}" ```

**Signals**

* When a user registers itself and is added to the database so we want to fire up some event to let them know via email that they now have an account in some website .

* Signals are the way to listen the actions performed in our website

![image](https://user-images.githubusercontent.com/63875409/138898735-b13f597b-f0c4-4bbc-b974-37027f2080e6.png)

* Create signals insider users -> models.py

from django.db.models.signals import post_save

def profileUpdated(sender, instance, created, **kwargs):
    print("Profile Saved!")

post_save.connect(profileUpdated, sender=Profile)

* Some issue in creating profile automatically

Rewatch the signals video