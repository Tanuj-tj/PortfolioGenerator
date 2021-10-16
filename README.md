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
 

