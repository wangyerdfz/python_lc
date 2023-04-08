def fullJustify(words: list, maxWidth: int) -> list:
    def space_needed(list_in : list):
        n = len(list_in)
        if n == 0:
            return 0           
        sum_ = len(list_in[0])
        for i in range(1 , n):
            sum_ += (1 + len(list_in[i]))
        return sum_
    
    def create_line(list_in: list, last_line = False):
        n = len(list_in)
        if n <= 0:
            return ""
        if space_needed(list_in ) > maxWidth:
            return ""
        res = ""
        if last_line:
            res = list_in[0]
            for i in range(1, n):
                res += " " + list_in[i]

            res += (maxWidth - len(res)) * " "
            return res
        
        num_spaces = (maxWidth - space_needed(list_in)) // (len(list_in) -1)
        num_white = (maxWidth - space_needed(list_in)) % (len(list_in) -1)

        res = list_in[0]
        for i in range(1, n):
            res += " "*(num_spaces + 1) + " "*(num_white > 0)
            res += list_in[i]
            num_white -= 1

        return res
    
    my_stack = []
    my_words = words.copy()
    res = []

    while(my_words):
        val_ = my_words.pop(0)
        my_stack.append(val_)
        if (space_needed(my_stack) < maxWidth):
            continue
        else:
            val_ = my_stack.pop()
            my_words.insert(0, val_)
            if not my_words: # this is the last line, prolly will never happen
                line = create_line(my_stack, True)
            else:
                line = create_line(my_stack, False)
            res.append(line)
            my_stack = []

    if my_stack:
        res.append(create_line(my_stack, True))

    return res


if __name__ == '__main__':
    test_case = ["This", "is", "an", "example", "of", "text", "justification."]
    max_witdh = 16
    print(fullJustify(test_case, max_witdh))