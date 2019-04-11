import yaml


def read(yaml_file='config.yaml'):
    config = open(yaml_file, 'r', encoding='utf-8')
    content = yaml.load(config)
    config.close()
    return content


def add(collection, value):
    if type(collection) == list:
        if type(value) != list:
            value = [value]
        collection += value
    elif type(collection) == dict:
        if collection:
            collection = {**collection, **value}
        else:
            collection = value
    return collection


def delete(collection, value):
    if type(collection) == list:
        collection.remove(value)
    elif type(collection) == dict:
        collection.pop(value)
    return collection


def write(key, value, opera='add', yaml_file='config.yaml'):  # 在yaml文件里写入list,要删除操作，参数opera = del
    content = read(yaml_file)
    config = open(yaml_file, 'w', encoding='utf-8')
    if opera == 'add':
        content[key] = add(content[key], value)
    elif opera == 'del':
        content[key] = delete(content[key], value)
    yaml.dump(content, config)
    config.close()



