# VFX Workflow Automation

> From nine workflow bottlenecks to a controlled AI-assisted pilot

[![Quality checks](https://github.com/Vedant-Au/vfx-workflow-automation-decision-model/actions/workflows/quality.yml/badge.svg)](https://github.com/Vedant-Au/vfx-workflow-automation-decision-model/actions/workflows/quality.yml)

**Engagement:** Fix Visual Effects | **Role:** Project Lead | **Observed outcome:** targeted changes adopted; manual reporting effort reduced by approximately **30%**

## Before → intervention → result

```mermaid
flowchart LR
    A["Production tracking"] --> B["Manual exports"]
    B --> C["JobMatrix and schedules"]
    C --> D["Weekly report rebuild"]
    D --> E["Late capacity signals"]
```

Producers were not short of software. They were short of a dependable flow of information between production tracking, schedules and client reporting. Interviews and system evidence identified nine recurring bottlenecks: duplicated status entry, stale schedules, late workload signals and repeated report assembly.

The engagement recommendation was deliberately narrower than “automate the studio”: establish one governed data flow, pilot AI-assisted scheduling with producer approval, and automate recurring reporting only after the underlying status data proved reliable.

## The sequencing decision

| Option | Fixed-weight score | What it optimises | Principal exposure |
| --- | ---: | --- | --- |
| AI-assisted first phase | **81.35** | Speed to value, adoption and controlled learning | May require later re-platforming |
| Full automation now | 74.65 | Target-state integration and scalability | Data, API, adoption and governance risk arrive together |

The phased option remained preferred in **77.1% of 10,000** alternative criterion-weight draws.

![Model score comparison](outputs/figures/model_scores.png)

## What would make me stop the pilot?

A pilot should not scale merely because the software runs. I would pause or redesign it if:

- schedule and task-status completeness remain below the agreed threshold;
- producer overrides are frequent but unexplained;
- API failures create a second manual reconciliation process;
- workload recommendations produce persistent fairness concerns; or
- reporting hours fall while exception-handling hours rise.

The full gate sequence, measures and guardrails are in the [pilot playbook](docs/PILOT_PLAYBOOK.md). The editable comparison model and sensitivity logic are explained in [option appraisal](docs/OPTION_APPRAISAL.md).

## Inspect or rerun

- [`data/reference/decision_matrix.csv`](data/reference/decision_matrix.csv) — editable criteria, weights and option scores
- [`analysis.py`](analysis.py) — deterministic MCDA and 10,000-draw sensitivity test
- [`outputs/`](outputs/) — decision tables and figures
- [`tests/`](tests/) — calculation and reconciliation checks

```bash
pip install -r requirements.txt
python analysis.py
python -m unittest discover -s tests -v
```

> **Client confidentiality:** commercial files and the submitted MSc report are not published. Workflow descriptions are abstracted, and option scores are analyst judgements—not vendor benchmarks. Details: [ASSET_NOTICE.md](ASSET_NOTICE.md).
