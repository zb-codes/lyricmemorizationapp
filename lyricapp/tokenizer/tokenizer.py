import string as str

def tokenize(string):
    startOfWord = 0
    index = 0
    tokenized_list = []
    for x in range(0, len(string)):
        char = string[index]
        if char == " " or char in str.punctuation:
            if startOfWord != index:
                tokenized_list.append(string[startOfWord:index])# append word BEFORE punctuation
            tokenized_list.append(char)# append punctuation
            startOfWord = index + 1        
        index += 1
    return tokenized_list

def reassemble(tokens):
    final_string = ""
    for token in tokens:
        final_string += token
    return final_string