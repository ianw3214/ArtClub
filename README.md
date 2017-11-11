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