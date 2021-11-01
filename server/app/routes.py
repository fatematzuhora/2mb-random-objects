'''app routes'''
import os
from random import choice, randint, uniform
from string import ascii_lowercase, digits
from flask import jsonify, make_response
from flask_cors import cross_origin
from app import app


def alphabetical_string(limit):
    '''generate alphabetical_string with a given range
    returns string
    '''
    obj = ''.join(choice(ascii_lowercase) for _ in range(limit))
    return obj

def real_number(limit_one, limit_two):
    '''generate real_number with the range of min and max
    returns float
    '''
    first_num = int(''.join(choice(digits) for _ in range(limit_one)))
    second_num = int(''.join(choice(digits) for _ in range(limit_two)))
    obj = uniform(first_num, second_num)
    return str(obj)

def integer(limit):
    '''generate integer with a given range
    returns string
    '''
    obj = ''.join(choice(digits) for _ in range(limit))
    return obj

def alphanumeric(limit):
    '''generate alphanumeric with a given range
    returns string
    '''
    obj = ''.join(choice(ascii_lowercase + digits) for _ in range(limit))
    return obj

def generate_object(option):
    '''switch statement to generate on object with a given option
    returns object
    '''
    return {
        'alphabetical_string': alphabetical_string(randint(1, 100)),
        'real_number': real_number(randint(1, 10), randint(1, 10)),
        'integer': integer(randint(1, 10)),
        'alphanumeric': alphanumeric(randint(1, 100)),
    }[option]

# ================================
# endpoints for random_objects app
# ================================
@app.route("/random", methods=["POST"])
@cross_origin()
def random_objects():
    '''endpoint to generate random objects of 2MB in size
    returns jsonify object
    '''
    choice_list = ['alphabetical_string', 'real_number', 'integer', 'alphanumeric']
    random_object_list = []

    total_char = 0
    alphabetical_str = 0
    real_num = 0
    integer_num = 0
    alphanumeric_str = 0

    while total_char < 2097152:
        option = choice(choice_list)
        object_value = generate_object(option)

        if (len(object_value) + total_char) > 2097152:
            diff = 2097152 - total_char
            object_value = alphabetical_string(diff - 2)

        random_object_list.append(object_value)
        total_char += len(object_value) + 2

        if total_char < 2097152:
            if option == 'alphabetical_string':
                alphabetical_str += 1
            elif option == 'real_number':
                real_num += 1
            elif option == 'integer':
                integer_num += 1
            elif option == 'alphanumeric':
                alphanumeric_str += 1
        else:
            alphabetical_str += 1

    with open(os.path.join('file', 'file.txt'), "w", encoding='utf8') as file:
        for item in random_object_list:
            file.write(str(item) + ', ')

    data = {
        'message': 'random objects',
        'status': 201,
        'data': {
            'random_object_list': random_object_list,
            'report': {
                'alphabetical_str' : alphabetical_str,
                'real_number' : real_num,
                'integer' : integer_num,
                'alphanumeric' : alphanumeric_str
            }
        }
    }
    return make_response(jsonify(data))
