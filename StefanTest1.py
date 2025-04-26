from sentence_transformers import SentenceTransformer, util
from word_dict import word_costs
import torch

model = SentenceTransformer('all-MiniLM-L6-v2')

# Pre-embed player words
player_ids = list(word_costs.keys())
player_words = [word_costs[i]["word"] for i in player_ids]
player_embeddings = model.encode(player_words, convert_to_tensor=True)

# New system word
system_word = "Lion"
system_embedding = model.encode(system_word, convert_to_tensor=True)

# Compute cosine similarity
cos_scores = util.pytorch_cos_sim(system_embedding, player_embeddings)[0]

# Convert to list of (id, word, cost, similarity)
candidates = []
for idx, cos_sim in enumerate(cos_scores):
    candidates.append({
        "id": player_ids[idx],
        "word": player_words[idx],
        "cost": word_costs[player_ids[idx]]["cost"],
        "similarity": float(cos_sim)
    })

# Step 1: Filter candidates above a similarity threshold
SIMILARITY_THRESHOLD = 0.5  # tweakable!

good_candidates = [c for c in candidates if c["similarity"] >= SIMILARITY_THRESHOLD]

# Step 2: Pick the lowest-cost among them
if good_candidates:
    best_choice = min(good_candidates, key=lambda x: (x["cost"], -x["similarity"]))
else:
    # fallback: highest similarity (even if low similarity)
    best_choice = max(candidates, key=lambda x: x["similarity"])

# Output
print(f"Chosen Word: ID {best_choice['id']} → '{best_choice['word']}' (${best_choice['cost']}) with similarity {best_choice['similarity']:.3f}")
