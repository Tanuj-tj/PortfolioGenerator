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
### Database Schema

![image](https://user-images.githubusercontent.com/63875409/137578201-0f762510-672e-4358-8fc1-8d9af6325318.png)
 

