# PostCRUDApiApp
PostCRUD API application. Implemented by Django.
*There is no production version, if you need, change Debug to 0 in .env.dev file or create other envfile if you want to deploy this project on prod.*
#### You can try it in live by link below
**Live version: http://185.65.244.208:8000/postcrud/api/posts**

# Deploy guide

Build the images and run the containers:

$ docker-compose up -d --build

##### It's better to be in dir UsersGroupsAppReact/

Test it out at http://127.0.0.1:8000

### If you have some problems with deploy try to use command:

$ docker-compose down -v

And try to deploy again

# Postman data - Documentation
##### Postman collection with requests for PostCRUDAPI App:
https://github.com/AlexDolls/PostCRUDApiApp/blob/3a37ad11244011773b8caf0a224601d5827a8d59/postcrudapi/postman_data/PostCRUDApp.postman_collection.json
###### Or get it via JSON link:
https://www.getpostman.com/collections/36925b2d44dd0c006c29

##### Postman 'Deploy' environment with variables:
https://github.com/AlexDolls/PostCRUDApiApp/blob/3a37ad11244011773b8caf0a224601d5827a8d59/postcrudapi/postman_data/Deploy.postman_environment.json

##### Postman 'Develop' environment with variables:
https://github.com/AlexDolls/PostCRUDApiApp/blob/3a37ad11244011773b8caf0a224601d5827a8d59/postcrudapi/postman_data/Develop.postman_environment.json

