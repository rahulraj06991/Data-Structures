def first_non_repeating_char(str):
    freq = {}
    for element in str:
       if element in freq:
          freq[element] += 1
       else:
            freq[element]=1
    for key, value in freq.items():
        if value == 1:
            return key
    return None



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )
