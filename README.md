# The_Gram_Master
An Instagram clone developed using django framework

## Author and contact details
* MungaiKeren
Email: wambukeren@gmail.com

# Project Description
A user of the application should be able to:

1. Sign in to the application to start using.
2. Upload their pictures to the application.
3. See their profile with all my pictures.
4. Follow other users and see their pictures on my timeline.
5. Like a picture and leave a comment on it.
A search functionality is implemented where one can search for the different users  and their images.

# SetUp and installation requirements
You need to have the following installed:
* Python3+
* Pip ```curl https://bootstrap.pypa.io/get-pip|python```
* Virtual ```$ python3.6 -m venv pip virtual```
* Activate the virtual environment ```source virtual/bin/activate```
* Django 1.11.5 ```(virtual)$ pip install django==1.11.5```
* Get all requirements ```pip freeze > requirements.txt```

### Running the server
```python manage.py runserver```

# Behaviour Driven Development

| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Visit instagram-clone site| Various images are displayed  | User can comment and like images |
| Click on image| Image expand with details displayed | Image details displayed |
| Search user | Images for user are displayed | App gets the images for the searched user |
| Visit profile | Images posted by user are displayed | App gets images for user |
| Visit Admin | Prompts for admin credentials | Admin dashboard displayed |


## Technologies used
* Django a python frame-work
* Javascript
* Html
* Bootstrap

# Development
It would be so great to have your contributions! Just follow the instructions below.

Fork the repo
* Clone the repo in your machine but ensure you have all the necessary modules.(You can find them in the set up instructions above) git clone https://github.com/MungaiKeren/Me-gallery.git
* Create a new branch git branch contributions
* Edit your changes in your branch
* Run the application
* Push your changes so we can have a view!

# Live development
Currently the app is deployed to heroku. You can find it [here](https://gram-clone.herokuapp.com/)

## Known Bugs
The applications likes and followers are not working
One can view all images for all users in the app


## Visual Representation
<img src="https://github.com/MungaiKeren/My-Shoe-images/blob/master/me%20gallery.png?raw=true" height = "400px">

### LICENSE
[MIT](https://github.com/MungaiKeren/The_Gram_Master/blob/master/LICENSE)