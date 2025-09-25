from sklearn.metrics.pairwise import cosine_similarity
from .models import Item  # import your model

def get_recommendations(item, top_n=5):
    target_vec = item.get_embedding()
    if target_vec is None:
        return []

    all_items = Item.objects.exclude(id=item.id)
    similarities = []

    for other in all_items:
        vec = other.get_embedding()
        if vec is not None:
            sim = cosine_similarity([target_vec], [vec])[0][0]
            similarities.append((other, sim))

    # Sort by similarity descending
    similarities.sort(key=lambda x: x[1], reverse=True)
    return [i[0] for i in similarities[:top_n]]

