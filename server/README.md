### Quick Start

```
cd server
```

- Create a virtual environment for this project and install dependencies

```
virtualenv .venv
```

- Activate the virtual environment

```
source .venv/bin/activate
```

- Install the dependencies

```
pip install -r requirements.txt
```

- Export app dependencies

```
export FLASK_APP=app.py
```

- Run the app

```
flask run
```

And finally, the application will run on the following URL: http://127.0.0.1:5000

### API Documentation

#### 1. Generate Random File

**Request**

```
POST /random
```

**Sample Response**

```
{
  "data": {
    "report": {
      "alphabetical_str": 15982,
      "alphanumeric": 15828,
      "integer": 16078,
      "real_number": 15813
    },
    "random_object_list": [
      69983, 258332.65786387565, "9mssuniczquwfhtqirrr5b079a9xo4vcj0752smwosjtsnduznsbs0crvz3seq", ...
    ]
  },
  "message": "random objects",
  "status": 201
}
```
