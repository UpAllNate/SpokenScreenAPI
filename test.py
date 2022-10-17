import requests

# data_={
#     "authentication":{
#         "username":"nate",
#         "password":"dumbledoor"
#     },
#     "data":{
#         "username":"temp2",
#         "password":"temp2",
#         "groupname":"general"
#     }


# }
# result=requests.post("https://api.upallnate.com/create_user",json=data_)
# print(result.json())
data_={
        "authentication":{
        "username":"nate",
        "password":"dumbledoor"
    }
}
result=requests.get("http://localhost:5000/update_api",json=data_)
print(result.json())