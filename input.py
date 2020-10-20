import json
import csv


class InvalidInputError(Exception):
    pass


_format_to_delimiter = {
    'csv': ',',
    'tsv': '\t'}


def get_list_from_file(file_name, file_format=None):
    if file_format is None:
        splitted = file_name.split('.')
        if len(splitted) != 2:
            raise InvalidInputError('no file format provided')
        file_format = splitted[1]
    try:
        with open(file_name, mode='r') as f:
            if file_format == 'json':
                obj = json.load(f)

            elif file_format in ('csv', 'tsv'):
                reader = csv.reader(f, delimiter=_format_to_delimiter[file_format])
                obj = None
                for row in reader:
                    obj = row
                    break
                if obj is None:
                    raise InvalidInputError('got an empty input')

                if any([not s.isdigit() for s in obj]):
                    raise InvalidInputError('every element must be a positive integer')

                return [int(x) for x in obj]

            else:
                raise InvalidInputError('format {} is not supported'.format(file_format))
    except FileNotFoundError as e:
        raise InvalidInputError(e)
    return obj
