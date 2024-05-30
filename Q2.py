# 2. Debugging Your Code II
# Debugging the Function add_underscores()
# The code on the left defines a function add_underscores() that takes a single string object word as an argument and returns a new string containing a copy of the word with each character surrounded by underscores. For example, add_underscores("python") should return _p_y_t_h_o_n_.
# However, if you try to run the following command python Q2.py in the Terminal window, you see that the output produced is not the one that you would expect.

def add_underscores(word):
    new_word = "_"
    for i in range(len(word)):
        new_word = new_word + word[i] + "_"
    return new_word


word = "python"
print(add_underscores(word))
