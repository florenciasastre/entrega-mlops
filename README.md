# UrbanPlan AI — Agentic Permit Intelligence Platform

Multi-agent AI system for urban planning workflows: permit feasibility analysis, BigQuery-grounded cost estimation, automated dossier generation and MLOps-ready deployment.

## Project Attribution & Role

This repository is based on an academic MLOps team project.

I was a contributing team member, not the sole author of the full original system. This portfolio version restructures and documents the project to present its architecture, technical scope and AI platform design more clearly.

My contribution is focused on AI system understanding, repository organization, technical documentation, product positioning and architectural interpretation of the solution.

The original project context and attribution are documented in [ATTRIBUTION.md](ATTRIBUTION.md).

## Business Context

Urban planning and construction permit workflows are complex, slow and highly dependent on fragmented regulatory and cost information.

This prototype explores how a multi-agent AI system can support early-stage permit intelligence by combining:

- Regulatory feasibility reasoning.
- BigQuery-grounded cost and timeline estimation.
- Automated executive dossier generation.
- MLOps-oriented packaging with Docker and CI/CD workflows.

The goal is not to replace legal or technical professionals. The goal is to assist decision-making by turning complex urban planning information into structured, traceable and actionable outputs.

## System Architecture

The project follows a supervisor-worker multi-agent architecture.

Supervisor Agent  
- Regulatory Agent: legal and planning feasibility reasoning.
- Estimation Agent: BigQuery-grounded cost and timeline estimation.
- Dossier Tool: Markdown permit dossier generation.

## Core Components

### Supervisor Agent

The supervisor agent interprets the user request, identifies the required task and routes execution to the appropriate specialist agent or tool.

### Regulatory Agent

The regulatory agent handles urban planning and construction-related feasibility questions. It is designed to reason over legal, technical and planning constraints using the base model and project context.

### Estimation Agent

The estimation agent is connected to BigQuery through a controlled tool. It does not invent costs or timelines. It retrieves structured historical data and uses SQL-grounded calculations to support estimates.

### Dossier Generation Tool

The dossier tool converts agent output into a Markdown-based executive report. This transforms the system from a chatbot into an operational workflow that produces a reusable deliverable.

## Technical Stack

- Python 3.12
- Google Agent Development Kit
- Gemini 2.5 Flash
- Google BigQuery
- Google Cloud Platform
- Docker
- GitHub Actions
- uv dependency management

## MLOps Design

The repository includes MLOps-oriented components for reproducibility and deployment readiness:

- Deterministic dependency management with uv.lock.
- Dockerfile for containerized execution.
- GitHub Actions workflow for CI/CD validation.
- Environment variable template through .env.example.
- BigQuery setup script for data initialization.
- Modular source code structure under src/urbanplan.

## Repository Structure

- .github/workflows/ — CI/CD workflow.
- docs/ — Architecture notes and project documentation.
- examples/dossiers/ — Curated sample dossier output.
- notebooks/ — Experimental indexing and research notebook.
- src/urbanplan/ — Core multi-agent system.
- .env.example — Environment variable template.
- Dockerfile — Container definition.
- main.py — Local project entrypoint.
- pyproject.toml — Project metadata and dependencies.
- setup_bigquery.py — BigQuery initialization script.
- uv.lock — Locked dependency graph.
- ATTRIBUTION.md — Project attribution and contribution scope.

## Local Setup

### 1. Install dependencies

uv sync --frozen

### 2. Configure environment variables

Create a .env file based on .env.example:

GOOGLE_CLOUD_PROJECT=your-gcp-project-id  
GEMINI_MODEL=gemini-2.5-flash  
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json

### 3. Authenticate with Google Cloud

gcloud auth application-default login

### 4. Initialize BigQuery data

Run this only if you are using a new Google Cloud project:

uv run python setup_bigquery.py

### 5. Launch the agent system

uv run adk web src

Then open the local ADK interface and interact with the supervisor agent.

## Example Prompts

Regulatory feasibility:

“What are the minimum free-height requirements for residential buildings under Spanish technical building regulations?”

BigQuery-grounded estimation:

“Based on historical data, what is the average permit fee and processing time for a major residential project in Madrid?”

Dossier generation:

“Estimate the cost of a 200 m² commercial renovation in Valencia and generate a permit dossier with the results.”

## Production-Oriented Packaging

Build the Docker image:

docker build -t urbanplan-ai:latest .

Run the container with Google Cloud credentials:

docker run -p 8080:8080 -e GOOGLE_APPLICATION_CREDENTIALS=/app/key.json -v /local/path/to/key.json:/app/key.json urbanplan-ai:latest

## Portfolio Value

This project demonstrates:

- Multi-agent orchestration.
- Tool-calling architecture.
- BigQuery-grounded estimation.
- Separation between LLM reasoning and deterministic data retrieval.
- Automated document generation.
- MLOps-aware repository structure.
- Docker and CI/CD readiness.

The strongest architectural decision is the separation between language generation and numerical grounding. The LLM coordinates, interprets and explains. BigQuery provides the structured data foundation for estimation.

## Disclaimer

This is a portfolio version of a collaborative academic project. It is not a production legal, architectural or engineering advisory system.

Outputs should be treated as technical demonstrations, not as official regulatory, financial or construction advice.
