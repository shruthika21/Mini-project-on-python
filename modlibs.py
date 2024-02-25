def madlibs():
    story = "Once upon a time, there was a {noun} who {verb} {adverb}."

    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    filled_story = story.format(noun=noun, verb=verb, adverb=adverb)

    print(filled_story)

if _name_ == "_main_":
    madlibs()
