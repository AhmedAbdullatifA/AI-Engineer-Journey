# Import the module of methods
import requests


# Its just some tests , the result is not actully

BASE = "https://dummyjson.com"
TIMEOUT = 10

# GET
response = requests.get(
    f"{BASE}/posts/4",
    timeout=TIMEOUT
)
response.raise_for_status()
print(response.json())

# POST
response = requests.post(
    f"{BASE}/posts/add",
    json={"title": "Ahmed", "userId": 1},
    timeout=TIMEOUT
)
response.raise_for_status()
print(response.json())

# PATCH
response = requests.patch(
    f"{BASE}/posts/4",
    json={"title": "Ahmed is Legendary"},
    timeout=TIMEOUT
)
response.raise_for_status()
print(response.json())

# PUT
response = requests.put(
    f"{BASE}/posts/4",
    json={"tags": ["French", "English", "Arabic"]},
    timeout=TIMEOUT
)
response.raise_for_status()
print(response.json())

# DELETE
response = requests.delete(
    f"{BASE}/posts/1",
    timeout=TIMEOUT
)
response.raise_for_status()
print(response.status_code)


# output 
# {'id': 4, 'title': 'All he wanted was a candy bar.', 'body': "All he wanted was a candy bar. It didn't seem like a difficult request to comprehend, but the clerk remained frozen and didn't seem to want to honor the request. It might have had something to do with the gun pointed at his face.", 'tags': ['mystery', 'english', 'american'], 'reactions': {'likes': 359, 'dislikes': 18}, 'views': 4548, 'userId': 47}
# {'id': 252, 'title': 'Ahmed', 'userId': 1}
# {'id': 4, 'title': 'Ahmed is Legendary', 'body': "All he wanted was a candy bar. It didn't seem like a difficult request to comprehend, but the clerk remained frozen and didn't seem to want to honor the request. It might have had something to do with the gun pointed athis face.", 'userId': 47, 'tags': ['mystery', 'english', 'american'], 'reactions': {'likes': 359, 'dislikes': 18}}
# {'id': 4, 'title': 'All he wanted was a candy bar.', 'body': "All he wanted was a candy bar. It didn't seem like a difficult request to comprehend, but the clerk remained frozen and didn't seem to want to honor the request. It might have had something to do with the gun pointed at his face.", 'userId': 47, 'tags': ['French', 'English', 'Arabic'], 'reactions': {'likes': 359, 'dislikes': 18}}
# 200

# Important notes :
# Essential Status Codes You Should Know
# Code	Meaning	Explanation
# 200	OK	The request was successful.
# 201	Created	A resource has been created.
# 202	Accepted	The request has been accepted for processing.
# 204	No Content	The request was successful, but there is no content to return.
# 301	Moved Permanently	The resource has been moved permanently.
# 400	Bad Request	The request is invalid.
# 401	Unauthorized	Authentication is required.
# 403	Forbidden	You do not have permission.
# 404	Not Found	The resource could not be found.
# 429	Too Many Requests	Too many requests have been made.
# 500	Internal Server Error	An internal server error occurred.
# 502	Bad Gateway	There is an issue with the response from an intermediary server (gateway).
# 503	Service Unavailable	The service is temporarily unavailable.

# Classification
# 1xx => Informational
# Information regarding the request.

# 2xx => Success
# The request was successful.

# 3xx => Redirection
# Further action (redirection) is required.

# 4xx => Client Errors
# An issue with the request or the client's permissions.

# 5xx => Server Errors
# An issue on the server side.