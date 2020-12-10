from flask import Blueprint, request, jsonify, Response

bp = Blueprint('fizzbuzz', __name__, url_prefix='/fizzbuzz')

@bp.route('', methods=['GET'])
def fizzbuzz():
    start = request.args.get('start')
    end = request.args.get('end')
    if start is None or end is None:
        return 'Parameters start and end are required', 400
    if validate_args(start, end):
        return jsonify(compute(start, end)), 200
    else:
        return 'Bad arguments for the API', 400

def validate_args(start, end): 
    # validate the converions to int type
    # from string
    try:
        start = int(start)
        end = int(end)
    except ValueError:
        return False
    return True

def compute(start, end):
    result = []
    # no problem with this conversion
    # because is been validated previously
    start, end = int(start), int(end)
    for i in range(start, end):
        if i % 15 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    return result