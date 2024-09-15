
def filter_function(word_list):
    for word in word_list:
        if len(word) > 5:
            return True
        else:
            return False


word_list = ['apple', 'banana', 'cat', 'dog', 'elephant']
filtered = filter(filter_function, word_list)
for i in filtered:
    print(i)

