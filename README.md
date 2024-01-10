### Restaurant menu API project with DRF

#### Features of the API
- Create menu item
- List menu items
- Edit menu items
- Delete menu items
- Get random menu item for Chef's special

#### Steps 

1. First create a model in models.py. Now make the migrations and migrate them. 
2. Next create a serializers object in the app level as serializers.py.Serializers helps to convert model instances into Python datatypes that can be displayed as JSON or XML. It also helps you to convert HTTP request body into Python datatypes and make them to a model instance.
3. Then update the views.py.
4. Create a urls.py to include the paths in app level.
5. Add the app level paths in urls.py in project level.
6. Now use command 'python3 manage.py runserver' to view the created REST API.
6. View the output using this url - 'http://127.0.0.1:8000/api/menu-items'  
![Alt text](<Screen Shot 2024-01-05 at 1.10.10 PM.png>)
7. View the details of one item using this url - http://127.0.0.1:8000/api/menu-items/1
![Alt text](<Screen Shot 2024-01-05 at 1.09.54 PM.png>)