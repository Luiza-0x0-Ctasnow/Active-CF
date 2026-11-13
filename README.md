# Active-CF (incompleted)
Interactive &amp; Intent-Driven Collaborative Filtering. Breaking the Echo Chamber in Recommendation Systems with Human-in-the-Loop Feedback.


# Active-CF 🚀

> **Breaking the Echo Chamber in Recommendation Systems with Human-in-the-Loop Feedback**

Traditional collaborative filtering recommendation engines are a "black box"—they rely entirely on historical math matrices (ratings, clicks, views), leaving users completely passive with **zero intervention power**.

**Active-CF** is an interactive, intent-driven collaborative filtering recommendation engine. This novel Vector Map Radius Control paradigm—giving users a "Radar Scope / Zoom Dial" to dynamically expand or shrink their search boundary in the high-dimensional embedding space. Think of it as an **audio equalizer for your recommendations**: it allows users to actively intervene, adjust, or guide their "peer group" (similar user circles) in real-time, putting the control back into the user's hands.

Instead of accepting static algorithmic results, users can manually adjust their calculation range to shift between Strict Core Taste (Echo Chamber) and Explorer Mode (Serendipity & Discovery) in real-time. (warming: Here show as demo of idea and possible solution!)

---

## 🌟 Key Features
Active-CF work as a dual-layer Human-in-the-Loop control paradigm:

 Macro Control— Vector Embedding Space Radar: A spatial "Radar Scope / Zoom Dial" that lets users dynamically expand or shrink their search boundary in the embedding space—shifting seamlessly between Strict Core Taste (Echo Chamber) and Explorer Mode (Serendipity & Discovery).

Micro Control — Peer Taste Equalizer: An interactive equalizer allowing users to manually boost (up to 3.0x) or mute (0.0x) specific peer influencers in real time.

* 🎯 **Peer Taste Equalizer (Amplification):** Found a peer whose recommendations always hit the spot? Manually dial up their influence weight to lean deeper into their taste profile.Let users slide a UI dial to expand or shrink their recommendation search boundary on the radar.
* 🛡️ Echo Chamber Breaker: Easily escape filter bubbles by widening the vector search threshold without resetting your entire user profile.
* 🔍 Transparent & Intent-Driven: Bridges heavy ML theory (vector spaces, distance thresholds) with tangible user control.
* 🔄 **Intent-Driven Exploration:** Dynamically shift weights to simulate different discovery modes (e.g., strict core, Balanced, explorer mode) without altering your core profile, easy and firendly edit via UI.
* 🧩 **Plug-and-Play Design:** Easily drops into existing Python-based collaborative filtering architectures as a wrapper around similarity calculation engines.

---

## 🛠️ How It Works
🗺️ The Vector Map Analogy

In modern embedding-based recommendation spaces, similarity is measured by distance (e.g., Euclidean or Cosine distance). Active-CF translates abstract vector math into an intuitive UI concept:

    Tight Radius (< 1.0 - Echo Chamber): Shrinks the search boundary. The system only looks at the immediate cluster right next to your vector coordinate for hyper-precise, familiar recommendations.

    Standard Radius (= 1.0 - Balanced): Follows standard collaborative filtering peer group metrics.

    Expanded Radius (> 1.0 - Explorer Mode / Serendipity): Widens the search boundary across the vector map, pulling in peer groups and item clusters further away to introduce fresh, cross-genre discoveries.

Active-CF combines traditional statistical similarity metrics (like **Pearson Correlation**) with an explicit **User Proactiveness Matrix**:

$$\text{Adjusted Score} = \text{Base Similarity Score} \times \text{User Feedback Weight}$$

* A weight of `1.0` respects pure algorithmic math.
* A weight `> 1.0` amplifies a specific user's taste influence.
* A weight approaching `0.0` suppresses or mutes that peer user's influence.

Active-CF scales traditional similarity metrics (like Pearson Correlation) using a user-controlled vector radius multiplier:

$$\text{Adjusted Score} = \text{Base Similarity Score} \times \text{Vector Radius Multiplier}$$

* A multiplier > 1.0 boosts marginal similarity scores into the inclusion zone (broader discovery).
* A multiplier < 1.0 filters out distant peers to lock onto core preferences.

---

## 📦 Installation

Clone the repository and ensure you have Python 3.8+ installed:

```bash
git clone https://github.com/Luiza-0x0-Ctasnow/active-cf.git
cd active-cf

```

---

## 📝 Quick Start & Usage Example

Here is how to initialize the `VectorMapSimilarityEngine` and simulate a user adjusting their vector search radius:
see also the `Demo-version.py` for a vivi presetation of idea! 
```python

from recommendation_data import dataset
from active_cf_engine import VectorMapSimilarityEngine

# 1. Initialize the engine with your dataset
engine = VectorMapSimilarityEngine(dataset)

print("--- 1. Default Vector Boundary for Toby ---")
print(engine.most_similar_users('Toby', 3))

# 2. Toby expands his vector search radius (Explorer Mode / Radius = 2.5)
print("\n--- 2. Toby expands vector search radius (Radius = 2.5) ---")
engine.set_vector_radius('Toby', 2.5)
print(engine.most_similar_users('Toby', 3))

# 3. Toby shrinks his vector search radius (Strict Core Taste / Radius = 0.5)
print("\n--- 3. Toby shrinks vector search radius (Radius = 0.5) ---")
engine.set_vector_radius('Toby', 0.5)
print(engine.most_similar_users('Toby', 3))

```
Try It Free by `active_cf_interactive_demo.html` !
---

## 🗺️ Roadmap

* [ ] **v1.0** Core Python engine supporting Pearson and Euclidean distance feedback wrapping.
* [ ] v1.1 Persistent user preference storage layer (SQLite / Redis integration).
* [ ] v2.0 Interactive Web UI demo using Streamlit / Gradio featuring a draggable "Radar Radius Slider".
* [ ] v2.1 Vector database connector (Faiss / Milvus) for live embedding space visualization.
---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://www.google.com/search?q=https://github.com/Luiza-0x0-Ctasnow/active-cf/issues).

1. Fork the Project (`[https://github.com/Luiza-0x0-Ctasnow/active-cf/fork](https://github.com/Luiza-0x0-Ctasnow/active-cf/fork)`)
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git origin push feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the **MIT License**. See `LICENSE` for more information.
