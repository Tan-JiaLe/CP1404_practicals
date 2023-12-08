text = input("Text: ").split()
dictionary = {}
max_length = 0
for word in text:
    dictionary[word] = dictionary.get(word, 0) + 1
    if len(word) > max_length:
        max_length = len(word)
for key in sorted(dictionary):
    thing, width, other_thing = key, max_length, dictionary[key]
    print(f"{thing:{width}} : {other_thing}")
