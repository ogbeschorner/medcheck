# Setup Alignment Specification

## Objective

Make the documented developer setup, pull-request checks, and current MedCheck
landing-page prototype agree with the repository. The prototype accepts a local
search term and displays a status message; it does not perform a medical search
or call a backend API.

## Commands

- Backend install: `cd backend && uv sync --all-groups --frozen`
- Backend checks: `cd backend && uv run ruff format --check . && uv run ruff check . && uv run pyright && uv run pytest --cov=tests`
- Web install: `cd web && corepack enable && pnpm install --frozen-lockfile`
- Web checks: `cd web && pnpm format:check && pnpm lint && pnpm typecheck && pnpm test && pnpm build`
- Docker smoke test: `./scripts/docker-smoke.sh`

## Project Structure

- `backend/` contains the minimal Django scaffold and backend tooling.
- `web/` contains the React/Vite medication workspace and its tests.
- `.github/workflows/` contains pull-request automation.
- `docs/specs/` contains implementation specifications.

## Code Style

Use the configured Ruff, Prettier, ESLint, and TypeScript rules. Keep UI state
local until a backend contract is specified.

## Testing Strategy

Run fast backend and web harness tests first, then build the web application.
Browser coverage will be added when the current medication workflow has an
approved browser-test contract.

## Boundaries

- Always use locked dependencies and safe local-only environment values.
- Ask before adding APIs, persistence, authentication, or real medical search.
- Never commit `.env`, real secrets, medical data, or generated build output.

## Success Criteria

- Node 22 and pnpm setup is reproducible and documented.
- Django's required local environment value is documented and checkable.
- README and AGENTS accurately describe the current files and commands.
- Pull requests run formatting, linting, type checks, tests, and the web build.
- Backend, web, Docker, and repository hygiene checks pass locally.

## Open Questions

The real search behavior, medical-data sources, API contract, authentication,
and hosting provider remain intentionally unspecified.
