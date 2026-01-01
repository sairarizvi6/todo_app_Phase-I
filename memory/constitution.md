# AI-Native Todo Platform Constitution

## Core Principles

### I. Correctness Before Complexity
Working software at every phase. Each incremental change must be independently testable and verifiable. No shortcuts that compromise correctness for velocity.

### II. Incremental Evolution
Each phase builds on a stable previous phase. Phases are independently runnable with clear boundaries. Foundation work must be complete before adding new capabilities.

### III. Simplicity and Clarity
Prefer readable, maintainable code over clever solutions. Architecture should be obvious to newcomers. Explicit over implicit where it matters.

### IV. Cloud-Native Best Practices
Modern DevOps patterns from the start: containerization, infrastructure as code, observability. Secure-by-default configuration for secrets, access, and networking.

### V. Purposeful AI Integration
AI features must augment core functionality, not replace it. Deterministic execution where applicable. Explicit, versioned prompts. Clear boundaries between AI reasoning and system actions.

## Technology Standards by Phase

### Phase I – In-Memory Python Console App
- Language: Python 3.10+
- No external database (in-memory data structures only)
- Console-based interaction (CLI-first)
- Deterministic behavior and testable logic
- Clean architecture with separation of concerns

### Phase II – Full-Stack Web Application
- Frontend: Next.js
- Backend: FastAPI
- ORM: SQLModel
- Database: Neon (PostgreSQL)
- RESTful API design with clear contracts
- Schema migrations with version control

### Phase III – AI-Powered Todo Chatbot
- AI Frameworks: OpenAI ChatKit, Agents SDK, Official MCP SDK
- Tool-based execution for deterministic operations
- Explicit, versioned prompt management
- Clear AI/system action boundaries

### Phase IV – Local Kubernetes Deployment
- Containerization: Docker
- Local cluster: Minikube
- Packaging: Helm charts
- Kubernetes management: kubectl-ai, kagent
- Health checks, configs, and secrets properly managed

### Phase V – Advanced Cloud Deployment
- Managed Kubernetes: DigitalOcean DOKS
- Event streaming: Kafka
- Service orchestration: Dapr
- Production observability
- Scalability and fault-tolerance patterns

## Constraints

1. **Phase Isolation**: Each phase must be independently runnable before advancing
2. **No Skipping Steps**: Architectural decisions must be documented; no shortcuts
3. **Infrastructure as Code**: All infrastructure must be reproducible via code
4. **Documentation Required**: Setup, run, and deploy instructions for each phase

## Documentation Standards

- One README per phase
- Architecture diagrams (textual or visual)
- Explicit trade-off explanations
- Step-by-step setup instructions

## Success Criteria

| Phase | Criteria |
|-------|----------|
| I | Fully functional in-memory console app |
| II | Deployed full-stack app with persistent storage |
| III | AI chatbot successfully interacting with todos |
| IV | Local Kubernetes deployment working end-to-end |
| V | Cloud deployment demonstrating scalability and resilience |

## Governance

- Constitution supersedes all other practices
- Amendments require documentation and approval
- All changes must maintain the phase isolation principle
- Code reviews must verify compliance with these principles

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
