import random

def generate_markov_chain(text, order=2):
    # Create a dictionary to store prefixes and their corresponding suffixes
    markov_chain = {}

    # Split the text into words
    words = text.split()

    # Build the Markov chain
    for i in range(len(words) - order):
        prefix = tuple(words[i:i + order])
        suffix = words[i + order]
        if prefix in markov_chain:
            markov_chain[prefix].append(suffix)
        else:
            markov_chain[prefix] = [suffix]

    return markov_chain

def generate_text(markov_chain, length=50, seed=None):
    # Choose a random starting prefix
    prefix = random.choice(list(markov_chain.keys()))

    # Generate text using the Markov chain
    generated_text = list(prefix)
    for _ in range(length - len(prefix)):
        if prefix in markov_chain:
            next_word = random.choice(markov_chain[prefix])
            generated_text.append(next_word)
            prefix = tuple(generated_text[-len(prefix):])
        else:
            break

    return " ".join(generated_text)

# Example usage:
text = "This is a sample text used for generating Markov chain text."
markov_chain = generate_markov_chain(text)
generated_text = generate_text(markov_chain)
print(generated_text)
