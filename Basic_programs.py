# Function to reverse a string (Input: hello, Output: olleh)
def reverse_string(input):
    length = len(input)
    s = ""
    for i in range(length-1, -1, -1):
        s+=input[i]
    return s

print(reverse_string("hello"))

# Function to check if a word is Palindrome (Input: MAM, Output: True)
def is_palindrome(input):
    length = len(input)
    s = ""
    for i in range(length-1, -1, -1):
        s+=input[i]
        #print(input[i])
    return s == input

print(is_palindrome("MAM"))

# Function to print words in reverse (Input: RAHUL RAJ, Output: RAJ RAHUL)
def reverse_word(input):
    rev = []
    word = ""
    for char in input:
        word+=char
        if char == " ":
            rev.append(word)
            word = ""
    rev.append(word)
    #print(rev, word)  
    for i in range(len(rev)-1,-1,-1):
        print(rev[i])

reverse_word("RAHUL RAJ")
    
# Function to Return Top K repeated elements (with out using any built-in methods) (Input: [1,1,1,2,2,3,3,3,4,4,4,4], Output: RAJ RAHUL)
def Top_k_elements(input):
    freq = {}
    for num in input:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] =1
    # freq_items = list(count.items())
    # print(freq_items)
    top1_val = None
    top1_count = 0

    top2_val = None
    top2_count = 0

    top3_val = None
    top3_count = 0

    for key in freq:
        count = freq[key]

        if count > top1_count:
            # shift down
            top3_val, top3_count = top2_val, top2_count
            top2_val, top2_count = top1_val, top1_count

            top1_val, top1_count = key, count

        elif count > top2_count:
            top3_val, top3_count = top2_val, top2_count
            top2_val, top2_count = key, count

        elif count > top3_count:
            top3_val, top3_count = key, count

    return top1_val, top2_val, top3_val

print(Top_k_elements([1,1,1,2,2,3,3,3,4,4,4,4]))





