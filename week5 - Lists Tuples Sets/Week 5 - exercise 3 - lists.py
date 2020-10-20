"""
so that it calculates the mode of the word lengths, that is, it determines the
most common word length in the sentence.
"""

sentence = "IT was a bright cold day in april and the clocks were striking thirteen"


print(f"{'Word' :<8} Length")

for word in sentence.split(" ") :
    print(f"{word} {len}")