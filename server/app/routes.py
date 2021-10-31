from app import app
from flask import request, jsonify, make_response
from random import choice, randint, uniform
from string import ascii_lowercase, digits


"""
================================
endpoints for random_objects app
================================
"""

def alphabetical_string(limit):
    alphabetical_string = ''.join(choice(ascii_lowercase) for _ in range(limit))
    return alphabetical_string


def real_number(limit_one, limit_two):
    first_num = int(''.join(choice(digits) for _ in range(limit_one)))
    second_num = int(''.join(choice(digits) for _ in range(limit_two)))

    real_number = uniform(first_num, second_num)
    return str(real_number)


def integer(limit):
    integer = ''.join(choice(digits) for _ in range(limit))
    return integer


def alphanumeric(limit):
    alphanumeric = ''.join(choice(ascii_lowercase + digits) for _ in range(limit))
    return alphanumeric


def switch_choice(x):
    return {
        'alphabetical_string': alphabetical_string(randint(1, 100)),
        'real_number': real_number(randint(1, 10), randint(1, 10)),
        'integer': integer(randint(1, 10)),
        'alphanumeric': alphanumeric(randint(1, 100)),
    }[x]

# endpoint to CREATE file
@app.route("/random", methods=["POST"])
def random_objects():
    object_list = ['alphabetical_string', 'real_number', 'integer', 'alphanumeric']
    random_objects = []

    char = 0

    while char < 2097152:
        obj = choice(object_list)
        value = switch_choice(obj)

        if (len(value) + 2 + char) > 2097152:
            diff = 2097152 - char
            value = alphabetical_string(diff - 2)

        random_objects.append(value)
        char += len(value) + 2

    with open('file.txt', 'w') as file:
        for item in random_objects:
            file.write(str(item) + ', ')

    data = {
        'message': 'All Categories!',
        'status': 200,
    }
    return make_response(jsonify(data))