# Authorization.py
I created a `Micro-Services Project` that support the `authentication` and `Authorization` option.

## mohsen_backend_user
`mohsen_backen_user` service is included the `permission model` ,`rule model`, `user model`.
 - permission : memorize the routes details
 - rule: rule is included the groups of permissions
  to system realizing who can has a group of permissions
 - user: the details of user e.g(username,password,phon,age, etc)

## mohsen_backend_gateway
- it is a `proxy` that you must request from this service to another services.  
- as well this identify your token that do you have permission to go to the considered URL or not

## mohsen_backend_consumer
- this consume the producers. and does the work we defined for that 

### on of the works i defined for that is i defined a function, that sends the routes of services to `user service` to register them in `permission collection`

### mohsen_backend_docker
- we use this service to run all services


# running project
# First
go to env file and change the `SERVER_URL` to your ip address.

# Second
install The docker on your system


# Third
open a command on the `mohsen_backend_docker` path

# Forth
write on command `docker-compose up` and press `Enter`

# Fifth
go to a browser and search for this address `http://<your ip address>:5002/api/docs/`

# Sixth
when you go to `http://<your ip address>:5002/api/docs/`, there is a **`server` List Box** and you must choose the `http://<your ip address>:5001/api/docs/`, to have the authorization.

# Thanks A Lot, 
## enjoy of my app
