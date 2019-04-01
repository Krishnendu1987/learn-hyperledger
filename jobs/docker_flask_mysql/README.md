Running the app

In order to run the our dockerized app, we will execute the following command from the terminal:

#docker-compose up

You can see the image being built, the packages installed according to the requirements.txt, etc. If everything went right, you will see the following line:

#app_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

We can find out that everything is running as expected by typing this url in a browser or using curl, and receiving the following response:

#{"favorite_colors": [{"Lancelot": "blue"}, {"Galahad": "yellow"}]}

You can access the database directly using the mysql client and following command (make sure your client is the same version of MySQL specified in the docker-compose.yml):

#mysql --host=127.0.0.1 --port=32000 -u root -p
