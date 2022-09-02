from random import randint

def create_random_name(n, words):
    name = ""
    for i in range(n):
        r = randint(0, len(words)-1)
        word = words[r]
        name += " " + word
    return name.strip()

def write_to_file(title, lst):
    with open(title, "w") as g:
        for name in lst:
            g.write(name)
            g.write('\n')