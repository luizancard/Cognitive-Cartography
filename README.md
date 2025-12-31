# Cognitive Cartography
> Mapping the Human Mind through Bayesian Inference and Socratic Pedagogy.

## The Vision
Education today is a "black box." We know what students get right, but we rarely understand *why* they get things wrong. **Cognitive Cartography** is an open-source framework designed to visualize and optimize the learning path of high-performance students.

By combining **Bayesian Knowledge Tracing (BKT)** with **Socratic Scaffolding**, we transform the learning experience from a linear path into an interactive, navigated map.

## The Engine: Bayesian Knowledge Tracing
The core logic utilizes the BKT model to estimate a student's mastery. We calculate the probability that a student has learned a skill based on their performance history:

$$P(L_{t+1}) = P(L_t | \text{Action}) + (1 - P(L_t | \text{Action})) \cdot P(T)$$

Where:
* $P(L_t)$: Probability of mastery before the exercise.
* $P(T)$: Probability of transition (learning).
* $P(S)$ and $P(G)$: Probabilities of Slips and Guesses.
 
### Key Innovations:
- **Vision-to-LaTeX:** Scans handwritten sketches using Multimodal LLMs.
- **Socratic Scaffolding:** An AI-led hint system that refuses to give the answer, forcing active recall.
- **Dynamic Skill Trees:** Real-time visualization of knowledge gaps.
