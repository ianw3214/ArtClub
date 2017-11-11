# Artclub

## Using the api

Use the base IP @ 34.230.29.192:5000/

Use paths *contests* to find a list of contests, e.g 34.230.29.192:5000/contests/

```json
{
  "contests": [
    {
      "description": "test description", 
      "id": "f50ec0b7-f960-400d-91f0-c42a6d44e3d0", 
      "name": "test contest", 
      "reward": "test reward"
    }, 
    {
      "description": "test description 2", 
      "id": "bd65600d-8669-4903-8a14-af88203add38", 
      "name": "test contest 2", 
      "reward": "test reward 2"
    }
  ]
}
```

Use the specific *ID* of a contest to find more details about a contest, e.g. 34.230.29.192:5000/contests/f50ec0b7-f960-400d-91f0-c42a6d44e3d0

```json
{
  "description": "test description", 
  "entries": [
    "bd65600d-8669-4903-8a14-af88203add39"
  ], 
  "name": "test contest", 
  "reward": "test reward"
}
```

Use *contests/new/* to add a new contest, e.g. 34.230.29.192:5000/contests/new/

Note that json data is expected in an http POST request, in the form of the following:

```json
{
    "name" : "...",
    "description" : "...",
    "reward" : "..."
}
```

Use *entry/new/* to add a new entry, e.g. 34.230.29.192:5000/entry/new/

Note that json data is expected in an http POST request, as well as an image file:
The *contest* and *user* fields are the IDs of the contest and user of the entry

```json
{
    "contest" : "...",
    "user" : "..."
}
```

Use *users/* to get a list of all users, e.g. 34.230.29.192:5000/users/

```json
{
    "users" : [
        {
            "name" : "test",
            "id" : "f50ec0b7-f960-400d-91f0-c42a6d44e3k8"
        }
    ]
}
```

Use the specific *ID* of a user to find more details about the user, e.g. 34.230.29.192:5000/users/f50ec0b7-f960-400d-91f0-c42a6d44e3k8

```json
{
    "users" : [
        {
            "name" : "test",
            "id" : "f50ec0b7-f960-400d-91f0-c42a6d44e3k8"
        }
    ]
}
```

Use *entries/* to get a list of all entries, e.g. e.g. 34.230.29.192:5000/users/

```json
{
    "entries": [
        {
            "id" : "bd65600d-8669-4903-8a14-af88203add39",
            "contest-id" : "f50ec0b7-f960-400d-91f0-c42a6d44e3d0",
            "user-id" : "f50ec0b7-f960-400d-91f0-c42a6d44e3k8",
            "image-name" : "test.png"
        }
    ]
}
```

***

Use */entry/new/* with POST data and image data to add a new entry.

The input JSON should have 2 fields, *contest* for contestID of entry and *user* for userID of entry.

***

To get the actual image data, use the *image/<path>* path to request the image with the specified name.

For example, 34.230.29.192:5000/image/test.png will return the red test rectangle.