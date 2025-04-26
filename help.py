from sentence_transformers import SentenceTransformer
import json

model = SentenceTransformer('all-mpnet-base-v2')

with open('words_counters.json', 'r') as f:
    word_counters = json.load(f)

embedded_counters = {}

for counter_word, counter_list in word_counters.items():
    embedded_list = []
    for word in counter_list:
        emb = model.encode(word).tolist()  # Convert numpy array to list (JSON can't save np.array)
        embedded_list.append({"text": word, "embedding": emb})
    embedded_counters[counter_word] = embedded_list

# Save the new JSON
with open('words_counters_embedded.json', 'w') as f:
    json.dump(embedded_counters, f)