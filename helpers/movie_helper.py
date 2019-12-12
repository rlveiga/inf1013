import pickle

def read():
    with open('filmes.pkl', 'rb') as input:
        try:
            data = pickle.load(input)
        except:
            data = []

    return data

def write(data):
    with open('filmes.pkl', 'wb') as outfile:
        pickle.dump(data, outfile)

def get_movie(name):
    data = read()

    for movie in data:
        if(movie.nome == name):
            return movie

    return None

def save(movie):
    data = read()

    data.append(movie)

    write(data)

def update(name, new_entry):
    data = read()

    for i, m in enumerate(data):
        if(m.nome == name):
            data[i] = new_entry
            break

    write(data)

def remove(name):
    data = read()

    for i, m in enumerate(data):
        if(m.nome == name):
            del data[i]
            break

    write(data)
