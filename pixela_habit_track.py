import requests
from datetime import datetime

"""https://pixe.la/v1/users/kush9/graphs/graph20.html"""

TOKEN="bciew98we21ej"
USERNAME="kush9"
GRAPH="graph20"

user_endpoint="https://pixe.la/v1/users"
parameters={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response=requests.post(url=user_endpoint,json=parameters)
# print(response.text)

graph_endpoint=f"{user_endpoint}/{USERNAME}/graphs"
create_graph={
    "id":GRAPH,
    "name":"Programming",
    "unit":"commit",
    "type":"int",
    "color":"momiji",
}
headers={
    "X-USER-TOKEN":TOKEN
}
# response=requests.post(url=graph_endpoint,json=create_graph,headers=headers)
# print(response.text)

today=datetime(year=2024,month=7,day=12)
user_input=input("What do you want to do?'add','update' or 'delete':").lower()

if user_input=="add":
    pixel_endpoint=f"{user_endpoint}/{USERNAME}/graphs/{GRAPH}"
    pixel_create={
        "date":today.strftime("%Y%m%d"),
        "quantity":input("How many commit do you done today:"),
        }
    response=requests.post(url=pixel_endpoint,json=pixel_create,headers=headers)
    print(response.text)
elif user_input=="update":
    update_pixel_endpoint=f"{user_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"
    update_pixel_create={
        "quantity":input("Changes how many commit you done today:"),
        }
    response=requests.put(url=update_pixel_endpoint,json=update_pixel_create,headers=headers)
    print(response.text)
elif user_input=="delete":
    delete_endpoint=f"{user_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"
    response=requests.delete(url=delete_endpoint,headers=headers)
    print(response.text)
else:
    print("You typed invalid key")




