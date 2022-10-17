import requests

data_={
    "authentication":{
        "username":"nate",
        "password":"dumbledoor"
    },
    "data":{
        "username":"temp2",
        "password":"temp2",
        "groupname":"general"
    }


}
result=requests.post("http://localhost:5000/create_user",json=data_)
print(result.json())