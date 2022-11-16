# Building a translator

"""Giraffe Language
    vowels -> g
    -----------

    dog -> dgg
    cat -> cgt"""

def translate(word):
    translation = ""
    for i in word:
        if i in "AEIOUaeoiu": # if letter.lower() in "aeiou"
            if i.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + i
    return translation

print(translate("Abrada"))