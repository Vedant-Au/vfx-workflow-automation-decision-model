# Option appraisal

## Why an MCDA was appropriate

The choice was not “which tool has the most features?” It was a sequencing decision with competing priorities: near-term value, integration, adoption, scalability, control and cost. A weighted comparison made those judgements visible and editable.

Each option receives a 0-100 score against six criteria:

`option score = sum(criterion score × criterion weight)`

The source values are published in [`data/reference/decision_matrix.csv`](../data/reference/decision_matrix.csv). They extend the engagement's workflow and SWOT evidence; they are not measured vendor performance.

## Stress test

A 10,000-draw Dirichlet test replaces the fixed weights with random non-negative weights that sum to one. The win rate measures how often the recommendation survives a different balance of priorities. It does not estimate implementation success.

## Decision use

The model supports a stakeholder workshop: challenge the criteria, replace analyst scores, discuss disagreements and record the basis for a final choice. Technical discovery, commercial quotes and security review remain necessary before procurement.
