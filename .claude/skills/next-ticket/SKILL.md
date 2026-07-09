---
name: next-ticket
description: Find and execute the next open GitHub issue for the Learning Companion MVP using the AI Factory pipeline.
---

# Next Ticket Skill

Executes the AI Factory pipeline for the next open GitHub issue in the Learning Companion MVP.

## Workflow

1. **Find** the next open GitHub issue using `gh issue list`
2. **Choose** the earliest ticket by number from: 1.3, 2.1, 2.2, 3.1, 3.2, 3.3, 4.1, 4.2, 5.1
3. **Read** the issue body
4. **Compare** it with [TICKETS.md](../../TICKETS.md)
5. **Follow** [CLAUDE.md](../../CLAUDE.md) pipeline:
   - Stage 1: RESEARCH
   - Stage 2: PLANNING
   - Stage 3: IMPLEMENTATION
   - Stage 4: TESTING
   - Stage 5: REVIEW

## Execution Steps

1. Run `python manage.py check` to validate Django project
2. Show changed files at the end
3. Show all commands run
4. Show verification result
5. Suggest conventional commit message

## Rules

- Execute only one ticket
- Do not commit automatically unless explicitly asked
- Do not push automatically unless explicitly asked
- Do not close GitHub issue automatically unless explicitly asked
- Do not implement features outside the current ticket
- Do not hardcode secrets (use environment variables)
- Follow Django conventions from CLAUDE.md
- Maintain 70%+ test coverage

## Usage

```
/next-ticket
```

The skill will guide you through the complete AI Factory pipeline for the selected ticket.
