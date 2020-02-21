from bst import *
from trees import *
from maps import *
from avl import *
from splayTree import *
import time

def encoding_key(key):
    encoded_key = 0
    key = key.upper()
    for char in key:
        encoded_key += ord(char)
        encoded_key = encoded_key*100
    return encoded_key/100


def set_dict_key(tree, key, value):
    encoded_key = encoding_key(key)
    tree.__setitem__(encoded_key, value)

def get_dict_key(tree, key):
    encoded_key = encoding_key(key)
    return tree.__getitem__(encoded_key)


# ------------------------------- Guest Management Software --------------------------------------
def edit_guest(tree, key, value):
    set_dict_key(tree, key, value)
    print("Added/Edited " + key)

def check_status(tree, key):
    try:
        encoded_key = encoding_key(key)
        guest_status = tree.__getitem__(encoded_key)
        return key + " - " + guest_status.get_value()
    except KeyError:
        return key + " - " + "No information"


if __name__ == "__main__":

#------------------------------------------------BST-------------------------------------------
    print("-----------------------------------BST-------------------------------------")
    #Guest Managing Software using BST
    guest_list = TreeMap()
    #Insert new guest
    start_time_bst_insert = time.time()
    edit_guest(guest_list, "Charlie", "Confirmed") 
    edit_guest(guest_list, "Lam", "Booked") 
    edit_guest(guest_list, "Dave", "Not Going")
    edit_guest(guest_list, "Lillian", "Confirmed")
    edit_guest(guest_list, "Jake", "Confirmed")
    edit_guest(guest_list, "Holt", "Confirmed")
    edit_guest(guest_list, "Terry", "Confirmed")
    edit_guest(guest_list, "Boyle", "Confirmed")
    edit_guest(guest_list, "Amy", "Confirmed")
    stop_time_bst_insert = time.time() - start_time_bst_insert
    #Check status
    print("")

    print("Checking Status ...")
    
    print(check_status(guest_list, "Lam"))
    print(check_status(guest_list, "Dave"))
    print(check_status(guest_list, "Xunfei"))
    

    #Edit existing guest
    print("")
    edit_guest(guest_list, "Lam", "Canceled")
    print("")
    print("Checking Status ...")
    start_time_bst = time.time()  #Check Execution time for BST
    print(check_status(guest_list, "Lam"))
    stop_time_bst = time.time() - start_time_bst

#----------------------------------------------------AVL------------------------------------------------
    print("-------------------------AVL------------------------------")
    #Guest Managing Software using AVL
    guest_list = AVLTreeMap()
    #Insert new guest
    start_time_avl_insert = time.time()
    edit_guest(guest_list, "Charlie", "Confirmed") 
    edit_guest(guest_list, "Lam", "Booked") 
    edit_guest(guest_list, "Dave", "Not Going")
    edit_guest(guest_list, "Lillian", "Confirmed")
    edit_guest(guest_list, "Jake", "Confirmed")
    edit_guest(guest_list, "Holt", "Confirmed")
    edit_guest(guest_list, "Terry", "Confirmed")
    edit_guest(guest_list, "Boyle", "Confirmed")
    edit_guest(guest_list, "Amy", "Confirmed")
    stop_time_avl_insert = time.time() - start_time_avl_insert
    #Check status
    print("")

    print("Checking Status ...")
      #Check Execution time for AVL
    print(check_status(guest_list, "Lam"))
    print(check_status(guest_list, "Dave"))
    print(check_status(guest_list, "Xunfei"))
    
    #Edit existing guest
    print("")
    edit_guest(guest_list, "Lam", "Canceled")
    print("")
    print("Checking Status ...")
    start_time_avl = time.time()
    print(check_status(guest_list, "Lam"))
    stop_time_avl = time.time() - start_time_avl
    

#--------------------------------------------Splay Tree------------------------------------------------
    print("---------------------Splay--------------------------------")
    #Guest Managing Software using Splay Tree
    guest_list = SplayTree()
    #Insert new guest
    start_time_splay_insert = time.time()
    edit_guest(guest_list, "Charlie", "Confirmed") 
    edit_guest(guest_list, "Lam", "Booked") 
    edit_guest(guest_list, "Dave", "Not Going")
    edit_guest(guest_list, "Lillian", "Confirmed")
    edit_guest(guest_list, "Jake", "Confirmed")
    edit_guest(guest_list, "Holt", "Confirmed")
    edit_guest(guest_list, "Terry", "Confirmed")
    edit_guest(guest_list, "Boyle", "Confirmed")
    edit_guest(guest_list, "Amy", "Confirmed")
    stop_time_splay_insert = time.time() - start_time_splay_insert
    #Check status
    print("")

    print("Checking Status ...")
    
    print(check_status(guest_list, "Lam"))
    print(check_status(guest_list, "Dave"))
    print(check_status(guest_list, "Xunfei"))
    
    #Edit existing guest
    print("")
    edit_guest(guest_list, "Lam", "Canceled")
    print("")
    print("Checking Status ...")
    start_time_splay = time.time()  #Check Execution time for BST
    print(check_status(guest_list, "Lam"))
    stop_time_splay = time.time() - start_time_splay


    print("------------------------------------Time----------------------------------------------------")
    print("Insert time in BST is " + str(stop_time_bst_insert))
    print("Insert time in AVL is " + str(stop_time_avl_insert))
    print("Insert time in Splay is " + str(stop_time_splay_insert))

    print("\n")

    print("Look-up time in BST is " + str(stop_time_bst))
    print("Look-up time in AVL is " + str(stop_time_avl))
    print("Look-up time in Splay is " + str(stop_time_splay))

    