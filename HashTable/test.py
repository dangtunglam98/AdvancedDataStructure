from bucket import BucketList
from hashTable import HashTable
from time import time
if __name__ == "__main__":
    list_name = []
    with open('names.txt') as my_file:
        for line in my_file:
            list_name.append(line.rstrip("\n"))
    ltdang_table = HashTable()
    python_table = dict()

    #For testing with small sample size, pls uncomment this
    # list_name = list_name[:20]
    
    #ltdang_16 Hash Table Insert Time
    ltdang_insertTime_start = time()
    for item in list_name:
        ltdang_table[item] = "Success"
    ltdang_insertTime = time()- ltdang_insertTime_start
    
    #ltdang_16 Hash Table Search Time
    ltdang_searchTime_start = time()
    for item in list_name:
        found = ltdang_table[item]
    ltdang_searchTime = time() - ltdang_insertTime_start

    #ltdang_16 Hash Table Delete Time
    ltdang_deleteTime_start = time()
    for item in list_name:
        del ltdang_table[item]
    ltdang_deleteTime = time() - ltdang_deleteTime_start

    #python_16 Hash Table Insert Time
    python_insertTime_start = time()
    for item in list_name:
        python_table[item] = "Success"
    python_insertTime = time()- python_insertTime_start
    
    #python_16 Hash Table Search Time
    python_searchTime_start = time()
    for item in list_name:
        found = python_table[item]
    python_searchTime = time() - python_searchTime_start

    # python_16 Hash Table Delete Time
    python_deleteTime_start = time()
    for item in list_name:
        del python_table[item]
    python_deleteTime = time() - python_deleteTime_start

#-----------------------------------------------------------------------
    print("My Hash Table Insert Time: " + str(ltdang_insertTime))
    print("Python Hash Table Insert Time: " + str(python_insertTime))
    if python_insertTime > ltdang_insertTime:
        print("----> My Hash Table is better in insertion")
    else:
        print("---->Python Hash Table is better in insertion") 
    print("")

    print("My Hash Table Search Time: " + str(ltdang_searchTime))
    print("Python Hash Table Search Time: " + str(python_searchTime))
    if python_searchTime > ltdang_searchTime:
        print("---->My Hash Table is better in search")
    else:
        print("---->Python Hash Table is better in search") 
    print("")

    print("My Hash Table Delete Time: " + str(ltdang_deleteTime))
    print("Python Hash Table Delete Time: " + str(python_deleteTime))
    if python_deleteTime > ltdang_deleteTime:
        print("---->My Hash Table is better in deletion")
    else:
        print("---->Python Hash Table is better in deletion") 

    #For seeing the shape of the table, please uncomment this 
    # Suggested: Do this with a small sample size (See above)
    # ltdang_table.shape_of_table()