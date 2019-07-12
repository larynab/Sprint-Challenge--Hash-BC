#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    #UnboundLocalError: local variable 'index' referenced before assignment
    #Gots to state it then
    index = 0
    #populating hashtable with weight in weights.
    for i in weights:
        # print(weight)
        # print(limit-weight)
        #If we store each weight's list index as its value,
        hash_table_insert(ht, i, index)
        #iteration time
        index += 1
    #lets get the range of the length of weights
    for i in range(len(weights)):
        #we can then check to see if the hash table contains an entry 
        #for `limit - weight`. 
        weight_sum = limit - weights[i]  
        #now to get the answer,
        weight_limit = hash_table_retrieve(ht, weight_sum)
        # we've found the two 
        #items whose weights sum up to the `limit`!
        if weight_limit is not None:  
            # print((weight_limit, i))
            return (weight_limit, i)

    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
