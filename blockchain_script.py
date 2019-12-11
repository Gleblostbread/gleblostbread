import hashlib as hl
import json
import os

block_chain = os.curdir + '/blockchain/'


def get_files():
    files = os.listdir(block_chain)
    return sorted([int(i[:-4]) for i in files])


def get_hash(filename):
    file = open(block_chain + filename, 'rb').read()
    return str(hl.md5(file).hexdigest())


def check():
    files = get_files()

    for file in files[1:]:
        act_file = str(file) + '.txt'
        prev_file = str(file - 1)
        h = json.load(open(block_chain + act_file))['hash']
        act_hash = get_hash(prev_file + '.txt')
        if h == act_hash:
            print('Block {}: OK'.format(prev_file))
        else:
            print('Block {}: Corrupted'.format(prev_file))


def block_write(name, amount, to_whom, prev_hash=''):
    files = get_files()

    prev_hash = get_hash(str(files[-1]) + '.txt')

    data = {'name': name,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash}

    with open(block_chain + str(files[-1] + 1) + '.txt', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    block_write(name='', amount='', to_whom='')
    check()


if __name__ == '__main__':
    main()