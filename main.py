import json
from math import log10
from pprint import pprint
import re

E1 = [
    1.0
]

E3 = [
    1.0, 2.2, 4.7
]

E6 = [
    1.0, 1.5, 2.2,
    3.3, 4.7, 6.8,
]

E12 = [
    1.0, 1.2, 1.5,
    1.8, 2.2, 2.7,
    3.3, 3.9, 4.7,
    5.6, 6.8, 8.2,
]

E24 = [
    1.0, 1.1, 1.2,
    1.3, 1.5, 1.6,
    1.8, 2.0, 2.2,
    2.4, 2.7, 3.0,
    3.3, 3.6, 3.9,
    4.3, 4.7, 5.1,
    5.6, 6.2, 6.8,
    7.5, 8.2, 9.1,
]

E48 = [
    1.00, 1.05, 1.10,
    1.15, 1.21, 1.27,
    1.33, 1.40, 1.47,
    1.54, 1.62, 1.69,
    1.78, 1.87, 1.96,
    2.05, 2.15, 2.26,
    2.37, 2.49, 2.61,
    2.74, 2.87, 3.01,
    3.16, 3.32, 3.48,
    3.65, 3.83, 4.02,
    4.22, 4.42, 4.64,
    4.87, 5.11, 5.36,
    5.62, 5.90, 6.19,
    6.49, 6.81, 7.15,
    7.50, 7.87, 8.25,
    8.66, 9.09, 9.53,
]

E96 = [
    1.00, 1.02, 1.05,
    1.07, 1.10, 1.13,
    1.15, 1.18, 1.21,
    1.24, 1.27, 1.30,
    1.33, 1.37, 1.40,
    1.43, 1.47, 1.50,
    1.54, 1.58, 1.62,
    1.65, 1.69, 1.74,
    1.78, 1.82, 1.87,
    1.91, 1.96, 2.00,
    2.05, 2.10, 2.16,
    2.21, 2.26, 2.32,
    2.37, 2.43, 2.49,
    2.55, 2.61, 2.67,
    2.74, 2.80, 2.87,
    2.94, 3.01, 3.09,
    3.16, 3.24, 3.32,
    3.40, 3.48, 3.57,
    3.65, 3.74, 3.83,
    3.92, 4.02, 4.12,
    4.22, 4.32, 4.42,
    4.53, 4.64, 4.75,
    4.87, 4.99, 5.11,
    5.23, 5.36, 5.49,
    5.62, 5.76, 5.90,
    6.04, 6.19, 6.34,
    6.49, 6.65, 6.81,
    6.98, 7.15, 7.32,
    7.50, 7.68, 7.87,
    8.06, 8.25, 8.45,
    8.66, 8.87, 9.09,
    9.31, 9.53, 9.76
]

E192 = [
    1.00, 1.01, 1.02, 1.04, 1.05, 1.06, 1.07, 1.09, 1.10, 1.11, 1.13, 1.14, 1.15, 1.17, 1.18, 1.20, 1.21, 1.23, 1.24,
    1.26, 1.27, 1.29, 1.30, 1.32, 1.33, 1.35, 1.37, 1.38, 1.40, 1.42, 1.43, 1.45, 1.47, 1.49, 1.50, 1.52, 1.54, 1.56,
    1.58, 1.60, 1.62, 1.64, 1.65, 1.67, 1.69, 1.72, 1.74, 1.76, 1.78, 1.80, 1.82, 1.84, 1.87, 1.89, 1.91, 1.93, 1.96,
    1.98, 2.00, 2.03, 2.05, 2.08, 2.10, 2.13, 2.15, 2.18, 2.21, 2.23, 2.26, 2.29, 2.32, 2.34, 2.37, 2.40, 2.43, 2.46,
    2.49, 2.52, 2.55, 2.58, 2.61, 2.64, 2.67, 2.71, 2.74, 2.77, 2.80, 2.84, 2.87, 2.91, 2.94, 2.98, 3.01, 3.05, 3.09,
    3.12, 3.16, 3.20, 3.24, 3.28, 3.32, 3.36, 3.40, 3.44, 3.48, 3.52, 3.57, 3.61, 3.65, 3.70, 3.74, 3.79, 3.83, 3.88,
    3.92, 3.97, 4.02, 4.07, 4.12, 4.17, 4.22, 4.27, 4.32, 4.37, 4.42, 4.48, 4.53, 4.59, 4.64, 4.70, 4.75, 4.81, 4.87,
    4.93, 4.99, 5.05, 5.11, 5.17, 5.23, 5.30, 5.36, 5.42, 5.49, 5.56, 5.62, 5.69, 5.76, 5.83, 5.90, 5.97, 6.04, 6.12,
    6.19, 6.26, 6.34, 6.42, 6.49, 6.57, 6.65, 6.73, 6.81, 6.90, 6.98, 7.06, 7.15, 7.23, 7.32, 7.41, 7.50, 7.59, 7.68,
    7.77, 7.87, 7.96, 8.06, 8.16, 8.25, 8.35, 8.45, 8.56, 8.66, 8.76, 8.87, 8.98, 9.09, 9.20, 9.31, 9.42, 9.53, 9.65,
    9.76, 9.88
]

BANDS = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white'
]

MULTIPLIERS = {
    -3: 'pink',
    -2: 'silver',
    -1: 'gold',
    0: 'black',
    1: 'brown',
    2: 'red',
    3: 'orange',
    4: 'yellow',
    5: 'green',
    6: 'blue',
    7: 'violet',
    8: 'grey',
    9: 'white',
}

MULTIPLIER = {
    'm': 0.001,
    'k': 1000,
    'M': 1000000,
    'G': 1000000000,
}

TOLERANCE = {
    20: '',
    10: 'silver',
    5: 'gold',
    1: 'brown',
    2: 'red',
    0.5: 'green',
}


def lambda_handler(event, context):

    # Extract the desired series, if any
    series = event.get('resource', '/').upper().replace('/', '')

    # Get the desired value from the event
    desired = event['queryStringParameters'].get('value', 0)
    match = re.match(r'(\d*[.]?\d*)([mkMG]?)', desired)
    desired = int(float(match.group(1)) * MULTIPLIER.get(match.group(2), 1))

    # Calculate normalizer
    normalizer = 10 ** int(log10(desired))

    # Calculate the normalized value
    normalized = desired / normalizer

    calculated = {
        'E1': to_series(E1, normalized, normalizer),
        'E3': to_series(E3, normalized, normalizer),
        'E6': to_series(E6, normalized, normalizer, 0.2),
        'E12': to_series(E12, normalized, normalizer, 0.1),
        'E24': to_series(E24, normalized, normalizer, 0.05),
        'E48': to_series(E48, normalized, normalizer, 0.02),
        'E96': to_series(E96, normalized, normalizer, 0.01),
        'E192': to_series(E192, normalized, normalizer, 0.005),
    }

    body = dict(
        desired=desired,
        normalizer=normalizer,
        normalized=normalized,
        closest=calculated,
    )

    if series:
        return {
            'statusCode': 200,
            'body': json.dumps(body['closest'][series]['nominal'])
        }

    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }


def error(desired, standard):
    return abs((standard-desired) / desired)


def to_series(series, normalized, normalizer, tolerance=0.2):

    series.append(series[0] * 10)

    results = [(error(normalized, s), normalized, s) for s in series]
    results.sort()

    result = results[0][-1]

    nominal = int(result * normalizer)

    colors = to_color(nominal=nominal, tolerance=tolerance)

    return dict(
        nominal=nominal,
        colors=colors,
        tolerance=tolerance,
    )


def to_color(nominal, tolerance=0.2):

    first, second, third, forth, = [BANDS[j] for j in [int(i) for i in '{0:1.5f}'.format(nominal*10000)[0:4]]]

    if tolerance >= 0.2:
        mult = MULTIPLIERS[int(log10(nominal))-1]
        return [first, second, mult]
    elif tolerance > 0.01:
        mult = MULTIPLIERS[int(log10(nominal))-2]
        tol = TOLERANCE[tolerance * 100]
        return [first, second, mult, tol]
    else:
        mult = MULTIPLIERS[int(log10(nominal))-2]
        tol = TOLERANCE[tolerance * 100]
        return [first, second, third, mult, tol]


if __name__ == '__main__':
    event = {
        'queryStringParameters': {
            'value': '249k'
        }
    }

    response = lambda_handler(
        event=event,
        context=None
    )

    response = json.loads(response['body'])

    pprint(response)

    assert response['closest']['E96']['nominal'] == 249000
    assert response['closest']['E96']['colors'][0] == 'red'
    assert response['closest']['E96']['colors'][1] == 'yellow'
    assert response['closest']['E96']['colors'][2] == 'white'
    assert response['closest']['E96']['colors'][3] == 'orange'
    assert response['closest']['E96']['colors'][4] == 'brown'