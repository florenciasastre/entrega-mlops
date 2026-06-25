# Architecture

UrbanPlan AI follows a supervisor-worker multi-agent architecture.

## Core Flow

1. The user submits an urban planning or permit-related query.
2. The supervisor agent interprets the request.
3. The supervisor delegates to specialist agents:
   - `agente_normativo` for legal and regulatory feasibility.
   - `agente_estimador` for cost and timeline estimation.
4. The estimation agent uses a BigQuery tool to ground calculations in structured data.
5. When requested, the system generates a permit dossier in Markdown.

## Design Principle

The LLM is not used as the source of numerical truth.

Cost estimation and historical analysis are grounded in BigQuery. The language model is used for orchestration, synthesis and user-facing explanation.

This separation improves reliability, auditability and operational trust.
