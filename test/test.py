from cartica import *


if __name__ == '__main__':
    assert is_end_reachable('test/path.json', 'json')
    assert not is_end_reachable('test/no_path.json', 'json')
