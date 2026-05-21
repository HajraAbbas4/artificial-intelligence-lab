# ---------------- Experiment 2 ----------------
# Bayes Theorem


def bayes_theorem(prob_a, prob_b_given_a, prob_b):
    return (prob_b_given_a * prob_a) / prob_b


prob_disease = 0.01
prob_positive_given_disease = 0.95
prob_positive = 0.05

result = bayes_theorem(prob_disease, prob_positive_given_disease, prob_positive)
print("\nExperiment 2: Bayes Theorem")
print("P(Disease | Positive Test):", result)
