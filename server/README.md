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

**Response**

```
{
  "data": {
    "report": {
      "alphabetical_str": 15982,
      "alphanumeric": 15828,
      "integer": 16078,
      "real_number": 15813
    },
    "url": "/Users/fatematzuhora/CraftsCoder/2mb-random-objects/server/file/file.txt"
  },
  "message": "random objects",
  "status": 201
}
```
