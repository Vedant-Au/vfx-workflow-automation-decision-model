# AI-assisted scheduling pilot playbook

## Baseline before building

- Agree scheduling, utilisation, revision and reporting KPIs.
- Assign owners for task status, capacity and client-reporting data.
- Measure weekly reporting effort and schedule-change latency.
- Record data completeness and reconciliation failures.

## Run one controlled pilot

- Use one project or production team.
- Connect capacity and task status to Flow Production Tracking.
- Retain producer approval for assignments and rescheduling.
- Log recommendations, overrides, API failures and exceptions.

## Scale, redesign or stop

| Gate | Evidence required |
| --- | --- |
| Data | Completeness and timeliness meet the agreed threshold |
| Integration | Failures do not create material reconciliation work |
| Adoption | Producers use the workflow and explain overrides |
| Value | Reporting effort falls without shifting work into exceptions |
| Control | Access, audit, rollback and human approval operate as designed |

Scale recurring reporting only after the gates pass. Revisit full automation after the pilot establishes reliable history and integration patterns.

## Non-negotiable guardrails

Human approval for material scheduling changes; client-data access controls and audit logs; override and rollback procedures; vendor-exit and data-export planning; and monthly monitoring for workload fairness and model drift.
