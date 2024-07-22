import numpy as np


def cosine_similarity(vec1, vec2):

    dot_product = np.dot(vec1, vec2)

    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)

    cosine_sim = dot_product / (norm_vec1 * norm_vec2)

    return cosine_sim


vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

similarity = cosine_similarity(vector1, vector2)

print("Cosine Similarity:", similarity)
