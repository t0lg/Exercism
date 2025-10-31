"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.
    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string."""
    prefix = vocab_words[0]
    return ' :: '.join([prefix] + [prefix + word for word in vocab_words[1:]])

def remove_suffix_ness(word):
    if word.endswith("ness"):
        root=word[:-4]
        if root.endswith("i"):
            root=root[:-1] + "y"
        return root
    return word
    
def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""
    # Remove period and split into words
    words = sentence.replace('.', '').split()
    # Take the target word by index and add 'en' to make it a verb
    return words[index] + 'en'