---
id: "001"
title: "Create project constitution"
stage: "constitution"
date: "2026-01-01"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "master"
user: "system"
command: "/sp.constitution"
labels: ["constitution","project-setup"]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - ".specify/memory/constitution.md"
  - "history/prompts/constitution/001-create-constitution.constitution.prompt.md"
tests:
  - "null"
---

## Prompt

/sp.constitution

Project: AI-Native Todo Platform – From In-Memory Console App to Cloud-Native, AI-Powered System

Overview:
This project incrementally evolves a simple in-memory Python console application into a production-grade, AI-powered, cloud-native system. Each phase builds on the previous one, emphasizing correctness, scalability, and modern DevOps practices.

Core principles:
- Correctness before complexity (working software at every phase)
- Incremental evolution (each phase builds on a stable previous phase)
- Simplicity and clarity for learning-focused implementation
- Cloud-native and DevOps best practices
- AI integration that is purposeful and explainable

Key standards:
- Phase isolation: each phase must be independently runnable
- Clear separation of concerns (UI, API, data, infrastructure, AI)
- Idiomatic use of each technology stack
- Explicit documentation for design decisions
- Secure-by-default configuration (secrets, access, networking)

Technology standards by phase:

Phase I – In-Memory Python Console App:
- Language: Python
- No external database (in-memory data structures only)
- Console-based interaction
- Deterministic behavior and testable logic
- Clean architecture and modular design

Phase II – Full-Stack Web Application:
- Frontend: Next.js
- Backend: FastAPI
- ORM: SQLModel
- Database: Neon (PostgreSQL)
- RESTful API design
- Schema migrations and data persistence
- Frontend-backend contract clearly defined

Phase III – AI-Powered Todo Chatbot:
- AI Frameworks: OpenAI ChatKit, Agents SDK, Official MCP SDK
- AI features must augment (not replace) core app functionality
- Deterministic tool execution where applicable
- Prompt design must be explicit and versioned
- Clear boundaries between AI reasoning and system actions

Phase IV – Local Kubernetes Deployment:
- Containerization: Docker
- Local cluster: Minikube
- Packaging: Helm
- Kubernetes management: kubectl-ai, kagent
- All services containerized and deployable locally
- Health checks, configs, and secrets properly managed

Phase V – Advanced Cloud Deployment:
- Managed Kubernetes: DigitalOcean DOKS
- Event streaming: Kafka
- Service orchestration and workflows: Dapr
- Production-ready observability considerations
- Scalability and fault-tolerance demonstrated

Constraints:
- Each phase must be completed before moving to the next
- No skipping architectural steps for convenience
- Infrastructure must be reproducible via code (IaC where applicable)
- Documentation required for setup, run, and deploy steps

Documentation requirements:
- README per phase
- Architecture diagrams (textual or visual)
- Clear explanation of trade-offs
- Step-by-step setup instructions

Success criteria:
- Phase I: Fully functional in-memory console app
- Phase II: Deployed full-stack app with persistent storage
- Phase III: AI chatbot successfully interacting with todos
- Phase IV: Local Kubernetes deployment working end-to-end
- Phase V: Cloud deployment demonstrating scalability and resilience
- Codebase is clean, understandable, and production-aligned

## Response snapshot

Created project constitution at `.specify/memory/constitution.md` with:
- 5 core principles (Correctness Before Complexity, Incremental Evolution, Simplicity and Clarity, Cloud-Native Best Practices, Purposeful AI Integration)
- Technology standards for all 5 phases
- Constraints and documentation requirements
- Success criteria table
- Governance rules

Created PHR at `history/prompts/constitution/001-create-constitution.constitution.prompt.md`

## Outcome

- ✅ Impact: Project constitution established with core principles, phase technology standards, constraints, and governance rules
- 🧪 Tests: N/A - constitutional setup
- 📁 Files: 2 files created/modified
- 🔁 Next prompts: Ready to begin Phase I implementation
- 🧠 Reflection: Constitution provides clear guardrails for incremental platform development

## Evaluation notes (flywheel)

- Failure modes observed: "none"
- Graders run and results (PASS/FAIL): "N/A"
- Prompt variant (if applicable): "none"
- Next experiment (smallest change to try): "none"
