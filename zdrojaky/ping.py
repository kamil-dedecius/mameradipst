import numpy as np

def ping_server(npings):
    return np.random.choice([0, 1], size=npings, p=(.3, .7))

def ping_server_categories(npings, ncategories):
    cat_psts = np.random.dirichlet(np.ones(ncategories))
    return np.random.multinomial(npings, cat_psts)
