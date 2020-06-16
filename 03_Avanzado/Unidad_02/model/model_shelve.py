import shelve

def choose_theme(theme_name):
    db = shelve.open('themes')
    r = db[theme_name]
    db.close()
    return r

def save_theme(theme_name, color):
    db = shelve.open('themes')
    db[theme_name] = color
    db.close()