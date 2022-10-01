import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def word_for_comments_count(comments: list[dict] | list) -> str:
    """Return the correct word depending on the number"""
    comment_word = morph.parse('комментарий')[0]
    comments_count: str = comment_word.make_agree_with_number(
        len(comments)).word
    return comments_count


# TESTING OR OUTDATED FUNCTIONS
"""
def word():
    base_word = morph.parse('погуляв')[0]
    # word1 = base_word.inflect({'nomn'}).word.capitalize()
    # word2 = base_word.inflect({'gent'}).word.capitalize()
    # word3 = base_word.inflect({'datv'}).word.capitalize()
    # word4 = base_word.inflect({'accs'}).word.capitalize()
    # word5 = base_word.inflect({'ablt'}).word.capitalize()
    # word6 = base_word.inflect({'loct'}).word.capitalize()
    normal_word = base_word.normalized.word
    # print(word1, word2, word3, word4, word5, word6)
    print(normal_word)
"""
