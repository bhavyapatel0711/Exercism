def add_prefix_un(word: str) -> str:
    """Take the given word and add the 'un' prefix."""
    return 'un' + word

def make_word_groups(vocab_words: list[str]) -> str:
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix applied, separated by ' :: '."""
    prefix = vocab_words[0]
    words = vocab_words[1:]
    return ' :: '.join([prefix] + [prefix + word for word in words])

def remove_suffix_ness(word: str) -> str:
    """Remove the suffix 'ness' from the word while keeping spelling in mind."""
    if word.endswith('iness'):
        return word[:-5] + 'y'
    elif word.endswith('ness'):
        return word[:-4]
    else:
        return word
    
def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb."""
    words = sentence.split()
    adjective = words[index]
    if adjective.endswith('.'):
        adjective = adjective[:-1]
    return adjective + 'en'

