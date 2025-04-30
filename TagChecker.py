from HelperFunctions import get_sentences, preprocess_sentence,regex_sort, remove_slash, add_slash


if __name__ == "__main__":

    sentences = get_sentences("Paragraph.txt")
 

    for sentence in sentences:
        print(sentence)
        #stack 1 for <\w>
        stack_opening_tag = []
        #stack 2 for <\/\w>
        stack_closing_tag = []

        if len(sentence) <1:
            continue
        #removing quotations to avoid bugs for regex match
        sentence = preprocess_sentence(sentence)
        words = sentence.split(" ")

        for word in words:
            #used https://regex101.com/ for testing
            regex_sort(word, op_stack=stack_opening_tag, 
                             cl_stack=stack_closing_tag)

        smallest_stack_size = min(len(stack_opening_tag), len(stack_closing_tag))

        for i in range(smallest_stack_size):
            op = stack_opening_tag.pop()
            cl = stack_closing_tag.pop()
            print(op," ",cl)
            if op != remove_slash(cl):
                print(1)
                print(f"Expected {add_slash(op)} found {cl}")
                break
        if len(stack_opening_tag) > 0:
            print(2)
            print(f"Expected {add_slash(stack_closing_tag.pop())} found #")
        elif len(stack_closing_tag) > 0:
            print(3)
            print(f"Expected # found {stack_closing_tag.pop()}")
        else:
            print(4)
            print("Correctly tagged paragraph")


