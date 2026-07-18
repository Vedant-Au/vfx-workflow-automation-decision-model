# VFX Workflow Automation: Phased Decision Model

**Process diagnosis and option appraisal for reducing manual scheduling and reporting in a live VFX production environment.**

[![Quality checks](https://github.com/Vedant-Au/vfx-workflow-automation-decision-model/actions/workflows/quality.yml/badge.svg)](https://github.com/Vedant-Au/vfx-workflow-automation-decision-model/actions/workflows/quality.yml)

**Role:** Project Lead, Fix Visual Effects engagement  
**Observed outcome:** recommendations adopted; manual reporting effort reduced by approximately 30%

## The operating problem

Flow Production Tracking was connected to manually maintained JobMatrix and Schedule spreadsheets. Producers repeatedly exported, checked and reformatted the same information for weekly reporting. Interviews and system evidence revealed **nine recurring bottlenecks**; the underlying constraint was fragmented information flow, not a lack of creative flexibility.

| Current-state failure | Operational consequence |
| --- | --- |
| Schedules synchronised by hand | Status became stale and downstream work slipped |
| Workload monitored manually | Capacity imbalances were identified late |
| Reports rebuilt each week | Producer time was absorbed by administration and checking |
| Revisions changed dependency chains | Plans became fragile and required rework |
| Tools held different versions of status | Cross-project visibility was weak |

## The decision

The studio could add an AI-assisted scheduling layer first or move directly to a fully automated production-management architecture.

I recommended the **AI-assisted model as the controlled first phase**, while designing the integration and data architecture for fuller automation later.

- Fixed-weight score: **81.35** for the phased option versus **74.65** for full automation.
- Sensitivity result: the phased option remained preferred in **77.1% of 10,000** alternative criterion-weight draws.

![Model score comparison](outputs/figures/model_scores.png)

![Sensitivity result](outputs/figures/sensitivity.png)

## Why not automate everything immediately?

Full automation offered a stronger target-state architecture, but its benefit depended on data quality, API reliability, staff adoption and model governance that had not yet been proven. The phased recommendation preserved producer judgement while testing the riskiest assumptions.

The client subsequently adopted targeted automation changes, with manual reporting effort reduced by approximately 30%. This repository implements the transparent option model used to stress-test the sequencing decision; it does not present the scores as measured vendor performance.

## Implementation gates

The [roadmap](docs/IMPLEMENTATION.md) moves from data and ownership foundations to a controlled scheduling pilot, automated reporting and then scale. Progression is conditional on data completeness, integration stability, user adoption and control thresholds.

The editable criteria and judgements are in [`data/reference/decision_matrix.csv`](data/reference/decision_matrix.csv), with the full scoring logic documented in the [methodology](docs/METHODOLOGY.md).

## Reproduce the model

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python analysis.py
python -m unittest discover -s tests -v
```

## Confidentiality and evidence boundary

Commercial source documents, client files and the submitted MSc report are excluded. Workflow descriptions are abstracted, and decision scores are analyst judgements derived from the engagement evidence. See [ASSET_NOTICE.md](ASSET_NOTICE.md).
