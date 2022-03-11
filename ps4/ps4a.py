# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    def insert_letter(letter,string):
        """
        input:letter(like"a"), string(like"bcd")
        output:a word list of possible inserts(like: abcd bacd bcad bcda)
    
       """
        n = len(string)
        string_list = list(string)
        word_list = []
        
        for i in range(n+1):
            string_copy = string_list.copy()
            string_copy.insert(i, letter)
            word = "".join(string_copy)
            # ans = get_permutations(sequence_list_rest).append(word)
            word_list.append(word)
    
        return word_list
    
    n = len(sequence)
    if n == 1:
        return sequence

    else:
        letter = sequence[0]
        string = sequence[1:]
        new_list = get_permutations(string)
        perms = []
        for i in new_list: 
            sequence_list = insert_letter(letter,i)
            perms += sequence_list

    return list(set(perms))




if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

#    case 1: 
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

#    case 2: 
    example_input = 'ab'
    print('Input:', example_input)
    print('Expected Output:', ['ab', 'ba'])
    print('Actual Output:', get_permutations(example_input))

#    case 3: 
    example_input = 'abb'
    print('Input:', example_input)
    print('Expected Output:', ['abb', 'bab', 'bba'])
    print('Actual Output:', get_permutations(example_input))
