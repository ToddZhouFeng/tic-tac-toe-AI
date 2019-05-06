import pickle
import numpy as np
def init_database():
    f=open("database.dat", "wb+")
    board=np.array( [ [1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]])
    database=[[board, 0]]
    pickle.dump(database, f)
    f.close()

def show_database():
    try:
        f=open("database.dat", "rb")
    except:
        print("database.dat不存在")
        return False
    database=pickle.load(f)
    print(database)
    f.close()

show_database()
