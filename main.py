# CSC649 : My First Python Experiment

sentence = input("Enter a Sentence: ")

if sentence.strip() == "":
    print("You did not enter a sentence")

else:
    word_count = len(sentence.split())
    character_count = len(sentence)

    print("Word Count:" , word_count)
    print("Charater count (include spaces):",character_count)