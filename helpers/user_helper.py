import pickle

def read():
    with open('users.pkl', 'rb') as input:
        try:
            data = pickle.load(input)
        except:
            data = []

    return data

def write(data):
    with open('users.pkl', 'wb') as outfile:
        pickle.dump(data, outfile)

def get_user(name):
    data = read()

    for user in data:
        if(user.nome == name):
            return user

    return None

def save(user):
    data = read()

    data.append(user)

    write(data)

def update(user):
    data = read()

    for i, u in enumerate(data):
        if(u.nome == user.nome):
            data[i] = user
            break

    write(data)
