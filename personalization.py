import pandas as pd
import pickle

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

# Load dataset
df = pd.read_csv("final_dataset_clean.csv")

# Load trained model
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

# Example personalization function
def recommend_amenities(guest_row):
    scores = {
        "Spa": guest_row["spa_affinity_score"],
        "Adventure": guest_row["adventure_affinity_score"],
        "Culture": guest_row["culture_affinity_score"],
        "Dining": guest_row["dining_affinity_score"]
    }

    # Top recommendation
    best_amenity = max(scores, key=scores.get)

    return best_amenity


# Test with one guest
if __name__ == "__main__":

    sample_guest = df.iloc[0]

    recommendation = recommend_amenities(sample_guest)

    print("Guest ID:", sample_guest["guest_id"])
    print("Recommended amenity:", recommendation)