from HelperFunctions import get_sentences, preprocess_sentence,regex_sort, remove_slash, add_slash, output_processing
from collections import deque

if __name__ == "__main__":

    sentences = get_sentences("Paragraph.txt")
 
    for sentence in sentences:
        #stack 1 for <\w>
        stack_opening_tag = []
        #stack 2 for <\/\w>
        queue_closing_tag = deque()

        if len(sentence) <1:
            continue
        #removing quotations to avoid bugs for regex match
        sentence = preprocess_sentence(sentence)
        words = sentence.split(" ")
        for word in words:
            #used https://regex101.com/ for testing
            regex_sort(word, op_stack=stack_opening_tag, 
                             cl_queue=queue_closing_tag)

        smallest_stack_size = min(len(stack_opening_tag), len(queue_closing_tag))

        result = output_processing(smallest_stack_size, stack_opening_tag, queue_closing_tag)
        print(result)

