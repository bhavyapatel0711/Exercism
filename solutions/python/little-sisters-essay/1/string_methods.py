def capitalize_title(title: str) -> str:    
    """Capitalizes the first letter of each word in the given title."""
    return title.title()

def check_sentence_ending(sentence: str) -> bool:
    """Checks if the given sentence ends with a punctuation mark."""
    return sentence.endswith(('.', '!', '?'))   

def clean_up_spacing(sentence: str) -> str:
    """Removes leading and trailing whitespace from the given sentence."""
    return sentence.strip() 

def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
    """Replaces all occurrences of the old word with the new word in the given sentence."""
    return sentence.replace(old_word, new_word) 

