from flask import Flask
from flask import request
import json
import create_user
import delete_user
import postgres
import os

app = Flask(__name__)

def authenticate(username,password):
    connection=postgres.get_connection()
    cursor=connection.cursor()
    cursor.execute("SELECT username,password,groupid FROM users WHERE username=%s",(username,))
    returned_data=cursor.fetchall()
    if len(returned_data)==1:
        print(returned_data)
        returned_username=returned_data[0][0]
        returned_password=returned_data[0][1]
        groupid=returned_data[0][2]
        if returned_password==password:
            cursor.execute("SELECT permissions FROM usergroups WHERE groupid=%s",(groupid,))
            returned_group_permission=cursor.fetchall()
            print(returned_group_permission)
            if returned_group_permission[0][0]==777:
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
        else:
            cursor.close()
            connection.close()
            return False
    else:
        cursor.close()
        connection.close()
        return False

@app.route('/')
def index():
    return "You're using the API wrong if you can see this"

@app.post('/create_user')
def cmd_createUser():

    data=json.loads(request.data.decode())
    username=data["authentication"]["username"]
    password=data["authentication"]["password"]
    if authenticate(username,password):
        try:
            create_user.create_user(data["data"]["username"],data["data"]["password"],data["data"]["groupname"])
            return {"result":"user created"}

        except KeyError as e:

            return {"result":f"You haven't provided the necessary key {e}"}
    else:
        return {"result":"UnAuthroized"}

@app.post('/delete_user')
def cmd_deleteUser():

    data=json.loads(request.data.decode())
    username=data["authentication"]["username"]
    password=data["authentication"]["password"]
    if authenticate(username,password):
        try:
            delete_user.delete_user(data["data"]["username"])
            return {"result":"user deleted"}

        except KeyError as e:

            return {"result":f"You haven't provided the necessary key {e}"}
    else:
        return {"result":"UnAuthroized"}

@app.get('/update_api')
def update_api():


    data=json.loads(request.data.decode())
    username=data["authentication"]["username"]
    password=data["authentication"]["password"]
    if authenticate(username,password):
        try:
            output=(os.system('git pull'))
            return {"result":f"command ran {output}"}

        except KeyError as e:

            return {"result":f"You haven't provided the necessary key {e}"}
    else:
        return {"result":"UnAuthroized"}

    # print(data["username"],data["password"])
    # return 'Hello, World'