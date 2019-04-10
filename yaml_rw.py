import yaml

operation = {}


def read():
    config = open('config.yaml', 'r', encoding='utf-8')
    content = yaml.load(config)
    config.close()
    return content


def add(collection, value):
    if type(collection) == list:
        collection.append(value)
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


def write(key, value, opera='add'):  # 在yaml文件里写入list,要删除操作，参数opera = del
    content = read()
    config = open('config.yaml', 'w', encoding='utf-8')
    if opera == 'add':
        content[key] = add(content[key], value)
    elif opera == 'del':
        content[key] = delete(content[key], value)
    yaml.dump(content, config)
    config.close()



