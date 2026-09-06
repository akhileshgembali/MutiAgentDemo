# Contributing Guide

Thank you for considering contributing to this project! This guide outlines the processes and conventions we follow to ensure a smooth collaboration experience.

## Table of Contents

- [Code Style](#code-style)
- [Branching Strategy](#branching-strategy)
- [Commit Message Conventions](#commit-message-conventions)
- [Testing Guidelines](#testing-guidelines)
- [Submitting Pull Requests](#submitting-pull-requests)

## Code Style

- **Language:** Follow the official style guide for the primary language(s) used in the project (e.g., PEP 8 for Python, Google's JavaScript Style Guide for JS).
- **Linting:** Run the project's linter (`npm run lint`, `flake8`, etc.) before committing. Fix all warnings and errors.
- **Formatting:** Use the configured formatter (e.g., `black`, `prettier`). Ensure files are formatted before committing.
- **Naming Conventions:** Use clear, descriptive names for variables, functions, classes, and files. Follow the project's naming conventions (snake_case for Python, camelCase for JavaScript, etc.).
- **Documentation:** Keep inline comments and docstrings up‑to‑date. Public APIs should have comprehensive documentation.

## Branching Strategy

We use a **Git Flow**‑inspired model:

1. **`main`** – Production‑ready code.
2. **`develop`** – Integration branch for features.
3. **Feature branches** – `feature/<short-description>` (branched from `develop`).
4. **Bugfix branches** – `bugfix/<short-description>` (branched from `develop`).
5. **Release branches** – `release/<version>` (branched from `develop`).
6. **Hotfix branches** – `hotfix/<short-description>` (branched from `main`).

> **Tip:** Keep branch names short, lowercase, and hyphen‑separated.

## Commit Message Conventions

We follow the **Conventional Commits** specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

- **type** – `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`, etc.
- **scope** – Optional, indicates the area of the codebase (e.g., `auth`, `api`).
- **subject** – Short, imperative description (max 72 characters).
- **body** – Optional, more detailed explanation.
- **footer** – Optional, references to issues (`Closes #123`).

Example:
```
feat(auth): add JWT token refresh endpoint

Implemented token refresh logic and added unit tests.

Closes #45
```

## Testing Guidelines

- **Run tests locally** before pushing: `npm test`, `pytest`, etc.
- **Coverage:** Aim for at least 80 % coverage. New code should include relevant unit/integration tests.
- **Test naming:** Follow the project's test naming conventions (`test_<module>.py`, `*.spec.js`).
- **Continuous Integration:** PRs trigger CI pipelines that run linting, formatting checks, and the full test suite.

## Submitting Pull Requests

1. **Fork** the repository and create a feature/bugfix branch as described above.
2. Ensure your code follows the style, branching, and commit conventions.
3. Run all tests and ensure CI passes locally.
4. Push your branch to your fork.
5. Open a pull request targeting the `develop` branch.
6. Fill out the PR template:
   - Brief description of changes.
   - Related issue numbers.
   - Any additional context or screenshots.
7. Request review from at least one maintainer.
8. Address review feedback and push updates.
9. Once approved, the maintainer will merge the PR.

Thank you for your contributions! 🎉