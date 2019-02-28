import os


def create_search_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_data(data, file_name):
    f = open(file_name, 'w')
    f.write(data)
    f.close()


def append_data(data, file_name):
    f = open(file_name, 'a')
    f.write(data + '\n')
    f.close()


def clear_file_data(file_name):
    with open(file_name, 'w'):
        pass


def file_to_list(file_name):
    results = list()
    with open(file_name, 'r') as f:
        for line in f:
            results.append(line.replace('\n', ''))
    return results


def set_to_file(links, file_name):
    clear_file_data(file_name)
    for link in links:
        append_data(link, file_name)
