import os


def make_dirs(name, count=1):
    if count > 1:
        for i in range(1, count + 1):
            path = os.path.join(os.getcwd(), f'{name}_{i}')
            os.mkdir(path)
    else:
        os.mkdir(os.path.join(os.getcwd(), name))


def show_help(*args):
    print('____________________________________________')
    print('You can use one of this command to work with files or directories:')
    print(r'list <f>\<d>\<a>- to print list of directories and files, all is default')
    print('del <name> - to delete file or directories with <name>')
    print('cd <name> - to change directory, print "cd .." to parent directory')
    print('mk_dir <name> <count> - to create directory with <name>, or some dire if <count> more then 1')
    print('exit - to exit')
    input('\n__To leave press Enter__')
    return True


def break_work(*args):
    print('Goodbye!')
    return False


def show_dir_list(path, arg: list):
    dir_list = os.listdir(path)
    if '__pycache__' in dir_list:
        dir_list.remove('__pycache__')
    print('This directory include this : ')

    # не работает d нужно реализовать выбор: f\d и всё вместе
    if arg:
        param = arg[0]
    else:
        param = ''
    file = {'f': 1, '': 0}  # где то тут
    for index, item in enumerate(dir_list):
        if os.path.splitext(os.path.basename(item))[file[param]]:
            e = '\t' if (index + 1) % 5 else '\n'
            print(f'{index}: {item}' + ' ' * (15 - len(item)), end=e)
    input('\n__To leave press Enter__')
    return True


def delete(path, arg: list):
    dir_list = os.listdir(path)
    for to_del in arg:
        if to_del in dir_list:
            del_path = os.path.join(path, to_del)
            if os.path.isdir(to_del):
                os.rmdir(del_path)
            elif os.path.isfile(to_del):
                os.remove(del_path)
        else:
            print(f'No such file with name "{to_del}"')
    return True


def change_dir(path, arg):
    dir_name = arg[0]
    if dir_name == "..":
        path_string = path.split('\\')[:-1]
        return "\\".join(path_string)

    check_path = os.path.join(path, dir_name)
    if check_path:
        return check_path
    else:
        print(f'Not valid path "{check_path}"')


def default(*args):
    print('Unexpected command')
    return True


cmds = {'help': show_help,
        'mk_dir': make_dirs,
        'exit': break_work,
        'list': show_dir_list,
        'cd': change_dir,
        'del': delete,
        'default': default}


def control():
    new_path = ''
    while True:
        params = []
        path = new_path or os.getcwd()
        to_do = input(path + "\\").split()
        if len(to_do) > 1:
            params = to_do[1:]
        result = cmds.get(to_do[0], cmds['default'])(path, params)
        if type(result) == str:
            new_path = result
        if not result:
            break


if __name__ == '__main__':
    control()
