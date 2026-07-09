---
name: next-ticket
description: Execute the next GitHub issue following AI Factory pipeline with strict Git workflow rules.
---

# Next Ticket Skill - Complete Workflow

Executes the next open GitHub issue following the AI Factory pipeline with mandatory Git workflow rules from CLAUDE.md.

## Overview

This skill automates the complete ticket lifecycle:
1. Find next open GitHub issue (earliest by number)
2. Execute AI Factory pipeline: Research → Planning → Implementation → Testing → Review
3. Create feature branch following naming convention
4. Implement changes, commit with conventional messages
5. Run full test suite and validation
6. Push to origin and create Pull Request
7. **STOP and wait for user approval** (NO AUTO-MERGE)

## Workflow Stages

### Stage 1: RESEARCH
- Find next open issue from: 1.3, 2.1, 2.2, 3.1, 3.2, 3.3, 4.1, 4.2, 5.1
- Read issue body and TICKETS.md details
- Analyze current codebase state
- Run `git status` to check current state
- Document assumptions

### Stage 2: PLANNING
- Design implementation approach
- Identify critical files to modify/create
- Check dependencies and impacts
- Verify no conflicts with existing code
- Show implementation plan

### Stage 3: IMPLEMENTATION (WITH GIT WORKFLOW)
**CRITICAL: Follow CLAUDE.md Section 5.5 Git Workflow Rules**

1. **Ensure main is up-to-date**:
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Create feature branch** (never work on main):
   ```bash
   git checkout -b feature/ticket-x-y-description
   ```

3. **Write code** following ticket requirements

4. **Commit with conventional format**:
   ```bash
   git commit -m "feat: description (Ticket X.Y)
   
   Details about changes...
   
   Acceptance criteria met:
   ✓ Criterion 1
   ✓ Criterion 2"
   ```

5. **CRITICAL: Do NOT push yet** - wait for testing

### Stage 4: TESTING
- Run `python manage.py check`
- Run full test suite
- Verify all acceptance criteria met
- Check for hardcoded secrets
- Validate migrations (if added)
- Show test results

**If tests fail**:
- Do NOT commit or push
- Fix issues
- Re-run tests
- Only then proceed to Review

### Stage 5: REVIEW
- Show changed files summary
- Show all commands executed
- Show verification results
- Show suggested commit message

### Stage 6: GIT PUSH & CREATE PR

**Only after all tests pass**:

1. **Push to origin**:
   ```bash
   git push -u origin feature/ticket-x-y-description
   ```

2. **Create Pull Request**:
   ```bash
   gh pr create \
     --title "feat: description (Ticket X.Y)" \
     --body "
   ## Summary
   Brief description of changes
   
   ## Changed Files
   - List of all files modified/created
   
   ## Acceptance Criteria
   ✓ All criteria from ticket
   
   ## Verification
   - Tests: ✅ PASS
   - Django check: ✅ PASS
   - Coverage: ✅ 70%+
   
   Closes #<issue-number> (Ticket X.Y)
   "
   ```

3. **Show PR summary**:
   - PR link
   - Changed files
   - Verification results
   - What needs to happen next

### Stage 7: WAIT FOR APPROVAL (CRITICAL!)

**Claude MUST STOP here and wait for user to write: "merge approved"**

Do NOT:
- ❌ Merge the PR automatically
- ❌ Close the GitHub issue
- ❌ Delete the feature branch
- ❌ Do anything else

Show user:
- PR link with all details
- Summary of changes
- "Waiting for your approval to merge..."
- "Please write 'merge approved' when ready"

## Execution Rules

### Critical Rules (From CLAUDE.md)
1. ✅ **NEVER work on main branch** - always use feature branch
2. ✅ **One ticket at a time** - don't implement multiple tickets
3. ✅ **Feature branch per ticket** - naming: `feature/ticket-x-y-description`
4. ✅ **Conventional commits** - `feat:`, `fix:`, `chore:`, etc.
5. ✅ **No hardcoded secrets** - use environment variables
6. ✅ **Run all tests** - before pushing
7. ✅ **Create PR** - not direct push to main
8. ✅ **Wait for approval** - Claude does NOT merge
9. ✅ **User approval** - "merge approved" required
10. ✅ **After merge** - delete branch, return to main

### What Claude Does At Each Stage

| Stage | Claude | Do NOT |
|-------|--------|--------|
| RESEARCH | Find issue, read details | Create branch yet |
| PLANNING | Design solution | Write code |
| IMPLEMENTATION | Create branch, write code, commit | Push yet |
| TESTING | Run tests, verify criteria | Push if tests fail |
| REVIEW | Push, create PR, show summary | Merge or close issue |
| WAIT | Show PR link, explain "merge approved" | Do anything else |

## Output Format

```
╔════════════════════════════════════════════╗
║        🎯 TICKET X.Y - NEXT TICKET        ║
╚════════════════════════════════════════════╝

📋 TICKET DETAILS
─────────────────
Ticket: X.Y
Epic: [Epic Name]
Title: [Issue Title]
Status: Found and ready

📊 PIPELINE EXECUTION
─────────────────────
✓ Stage 1: RESEARCH
✓ Stage 2: PLANNING
✓ Stage 3: IMPLEMENTATION
  └─ Created branch: feature/ticket-x-y-...
  └─ Made X commits
✓ Stage 4: TESTING
  └─ Django check: PASS
  └─ Tests: PASS
  └─ Coverage: 70%+
✓ Stage 5: REVIEW
  └─ Changed files: 5
  └─ Commands run: 10

📁 CHANGED FILES
────────────────
✅ Created: learning/models.py
✅ Modified: config/settings.py
[... more files ...]

🔗 GIT WORKFLOW
───────────────
✓ Feature branch created: feature/ticket-x-y-...
✓ Commits: 3
✓ Pushed to origin
✓ Pull Request created: #<PR-number>

🔗 PULL REQUEST
───────────────
Title: feat: description (Ticket X.Y)
Link: https://github.com/user/repo/pull/<PR-number>
Status: READY FOR REVIEW

📝 NEXT STEP
────────────
Waiting for your approval to merge.

Please write: "merge approved"

When you approve:
1. PR will be merged into main
2. Feature branch will be deleted
3. GitHub issue will be closed
4. Ready for next ticket
```

## After User Approves

User writes: "merge approved"

Claude then:
```bash
# Merge the PR (via GitHub API or user merges manually)
gh pr merge <PR-number> --squash

# Return to main
git checkout main
git pull origin main

# Delete local branch
git branch -d feature/ticket-x-y-description

# Delete remote branch
git push origin --delete feature/ticket-x-y-description

# Confirm and ready for next ticket
```

## Summary

- ✅ Executes one complete ticket per run
- ✅ Follows AI Factory pipeline strictly
- ✅ Implements Git workflow from CLAUDE.md (Section 5.5)
- ✅ Creates feature branches, conventional commits
- ✅ Runs complete test suite before push
- ✅ Creates PR and waits for approval
- ✅ **NO AUTO-MERGE** - requires explicit "merge approved"
- ✅ Shows detailed progress and next steps
