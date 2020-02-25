import random 
from rbt import *
from time import time
from bst import *

thread_nums = range(1,200)

if __name__ == "__main__":
    print("-------------------------bst------------------------------")
    thread_bst = TreeMap()

    start_insert_bst = time()
    for thread in thread_nums:
        thread_bst.__setitem__(thread, "Running")
    end_insert_bst = time() - start_insert_bst

    print("Insert time for bst " + str(end_insert_bst))

    start_search_bst = time()
    for thread in thread_nums:
        thread_bst.__getitem__(thread)
    end_search_bst = time() - start_search_bst

    print("Search time for bst " + str(end_search_bst))

    start_delete_bst = time()
    for thread in thread_nums:
        thread_bst.__delitem__(thread)
    end_delete_bst = time() - start_delete_bst

    print("Delete time for bst " + str(end_delete_bst))

    print("-------------------------RBT------------------------------")

    thread_rbt = RedBlackTreeMap()

    start_insert_rbt = time()
    for thread in thread_nums:
        thread_rbt.__setitem__(thread, "Running")
    end_insert_rbt = time() - start_insert_rbt

    print("Insert time for rbt " + str(end_insert_rbt))

    start_search_rbt = time()
    for thread in thread_nums:
        thread_rbt.__getitem__(thread)
    end_search_rbt = time() - start_search_rbt

    print("Search time for rbt " + str(end_search_rbt))

    start_delete_rbt = time()
    for thread in thread_nums:
        thread_rbt.__delitem__(thread)
    end_delete_rbt = time() - start_delete_rbt
    print("Delete time for rbt " + str(end_delete_rbt))