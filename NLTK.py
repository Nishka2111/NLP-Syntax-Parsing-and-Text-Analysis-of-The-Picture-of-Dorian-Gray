import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Download required NLTK data (run once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# 1. Import the text and convert to lowercase
text = open("dorian_gray.txt", encoding="utf-8").read().lower()

# 2. Sentence tokenize then word tokenize
sentences = sent_tokenize(text)
word_tokenized_text = [word_tokenize(sentence) for sentence in sentences]

# 3. Save one example sentence
single_word_tokenized_sentence = word_tokenized_text[0]
print("\nExample word-tokenized sentence:\n")
print(single_word_tokenized_sentence)


# -----------------------------
# Part-of-Speech Tagging
# -----------------------------

# 4. Create list to store POS tagged sentences
pos_tagged_text = []

# 5. POS tag each sentence
for sentence in word_tokenized_text:
    pos_sentence = nltk.pos_tag(sentence)
    pos_tagged_text.append(pos_sentence)

# 6. Show example POS tagged sentence
single_pos_sentence = pos_tagged_text[0]
print("\nExample POS-tagged sentence:\n")
print(single_pos_sentence)


# -----------------------------
# Chunk Grammar
# -----------------------------

# 7. Noun phrase grammar
np_chunk_grammar = "NP: {<DT>?<JJ>*<NN.*>}"

# 8. Create NP parser
np_chunk_parser = nltk.RegexpParser(np_chunk_grammar)

# 9. Verb phrase grammar
vp_chunk_grammar = "VP: {<NN.*|PRP><VB.*><RB>?}"

# 10. Create VP parser
vp_chunk_parser = nltk.RegexpParser(vp_chunk_grammar)


# -----------------------------
# Chunk Sentences
# -----------------------------

# 11. Create empty lists
np_chunked_text = []
vp_chunked_text = []

# 12 & 13. Parse sentences
for sentence in pos_tagged_text:

    np_chunked = np_chunk_parser.parse(sentence)
    np_chunked_text.append(np_chunked)

    vp_chunked = vp_chunk_parser.parse(sentence)
    vp_chunked_text.append(vp_chunked)


# -----------------------------
# Functions to count chunks
# -----------------------------

def np_chunk_counter(chunked_sentences):

    np_chunks = []

    for tree in chunked_sentences:
        for subtree in tree.subtrees():
            if subtree.label() == "NP":
                chunk = " ".join(word for word, tag in subtree.leaves())
                np_chunks.append(chunk)

    return Counter(np_chunks).most_common(30)


def vp_chunk_counter(chunked_sentences):

    vp_chunks = []

    for tree in chunked_sentences:
        for subtree in tree.subtrees():
            if subtree.label() == "VP":
                chunk = " ".join(word for word, tag in subtree.leaves())
                vp_chunks.append(chunk)

    return Counter(vp_chunks).most_common(30)


# -----------------------------
# Analyze chunks
# -----------------------------

# 14. Most common noun phrases
most_common_np_chunks = np_chunk_counter(np_chunked_text)

print("\nMost common noun phrases:\n")
for chunk, count in most_common_np_chunks:
    print(chunk, ":", count)


# 15. Most common verb phrases
most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)

print("\nMost common verb phrases:\n")
for chunk, count in most_common_vp_chunks:
    print(chunk, ":", count) 


np_phrases = [chunk for chunk, count in most_common_np_chunks[:10]]
np_counts = [count for chunk, count in most_common_np_chunks[:10]]

plt.figure(figsize=(10,6))
plt.barh(np_phrases, np_counts)
plt.xlabel("Frequency")
plt.title("Most Common Noun Phrases in The Picture of Dorian Gray")
plt.gca().invert_yaxis()
plt.show()

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white"
).generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of The Picture of Dorian Gray")
plt.show()

example_tree = np_chunk_parser.parse(pos_tagged_text[0])
example_tree.draw()