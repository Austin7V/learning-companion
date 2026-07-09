# /next-ticket

**title**: Execute next Learning Companion MVP ticket
**description**: Find, execute, and complete the next GitHub issue from Learning Companion MVP project board following AI Factory pipeline

---

## How It Works

This command automates the AI Factory workflow for Learning Companion MVP project:

1. **Find Next Ticket**: Queries GitHub for next open issue (starting with Backlog column)
2. **Stage It**: Moves issue to "In Progress" status
3. **Execute by Pipeline**: Follows strict AI Factory pipeline (Research → Planning → Implementation → Testing → Review)
4. **Verify**: Runs all acceptance criteria checks
5. **Commit & Close**: On success: commits, pushes, closes issue. On failure: stops, leaves issue in progress

## Prerequisites

- GitHub CLI (`gh`) installed and authenticated
- Local git repository with remote
- Python environment with Django
- CLAUDE.md and TICKETS.md in project root
- GitHub Project Board "Learning Companion MVP" must exist

## Command Structure

```
/next-ticket [--dry-run] [--skip-push] [--only-find]
```

**Options**:
- `--dry-run`: Show what would happen without actually executing
- `--skip-push`: Execute and commit but don't push to remote
- `--only-find`: Just find and show the next ticket, don't execute

## Execution Flow

### 1. FIND NEXT TICKET

```bash
# Find open issues in repository
gh issue list --state open --limit 20 --json number,title,labels

# Get issue details
gh issue view <issue-number> --json body,labels,number,title

# Extract from TICKETS.md - match issue title with ticket number
grep -E "^### Issue" TICKETS.md | grep "<title>"
```

**Match Logic**:
- Look for issue in "Backlog" (no assignee or specific label)
- Prefer lower ticket numbers (1.1, 1.2, etc.)
- Skip if already assigned to someone
- Skip if already in "In Progress" or "Done"

### 2. READ TICKET DETAILS

Extract from TICKETS.md:
- Ticket number (e.g., 1.1, 1.2, etc.)
- Epic name
- Acceptance criteria
- Task description

### 3. EXECUTE PIPELINE

#### Stage 1: RESEARCH
```
- Read current project state
- Check what files already exist
- Review CLAUDE.md architecture section
- Document assumptions in comments
- Show current state findings
```

#### Stage 2: PLANNING
```
- Design the solution
- List files to create/modify
- Check dependencies
- Verify no architecture conflicts
- Show implementation plan
```

#### Stage 3: IMPLEMENTATION
```
- Create necessary files
- Make required changes
- Follow Django/Python conventions
- No hardcoded secrets
- Keep code simple and focused
```

#### Stage 4: TESTING
```
- Run: python manage.py check
- Verify file syntax
- Check imports work
- Test core functionality
- Show all test results
```

#### Stage 5: REVIEW
```
- Verify acceptance criteria
- Check code quality
- No secrets in code
- Proper error handling
- Show review checklist
```

### 4. COMPLETION (On Success)

```bash
# Stage changes
git add -A

# Create commit with specific message format
git commit -m "feat: <description> (Ticket <number>)

Details from ticket description...

Acceptance criteria met:
✓ Criterion 1
✓ Criterion 2

Ticket: <number> (Epic: <epic-name>)"

# Push to remote
git push origin <current-branch>

# Close GitHub issue
gh issue close <issue-number> --comment "Ticket completed via /next-ticket command"

# Move to Done (via label if board uses labels)
gh issue edit <issue-number> --add-label "status/done"
```

### 5. FAILURE HANDLING (On Failure)

```
- Show what failed (test output, error message)
- Do NOT commit or push
- Leave issue in "In Progress"
- Provide suggestions for fixing
- Suggest manual investigation steps
```

## Output Format

The command will show:

```
╔════════════════════════════════════════════╗
║         🎯 NEXT TICKET EXECUTION          ║
╚════════════════════════════════════════════╝

📋 TICKET DETAILS
─────────────────
Ticket: 1.2
Epic: Project Setup
Status: Found in Backlog
Title: Setup OpenAI API Integration

📊 PIPELINE EXECUTION
─────────────────────
✓ Stage 1: RESEARCH
✓ Stage 2: PLANNING
✓ Stage 3: IMPLEMENTATION
✓ Stage 4: TESTING
✓ Stage 5: REVIEW

📁 CHANGED FILES
────────────────
✅ Created: learning/services.py
✅ Modified: config/settings.py

✅ All tests passed
✅ Ready to commit

📝 COMMIT MESSAGE
─────────────────
feat: setup OpenAI API integration (Ticket 1.2)
...

🔗 GITHUB
─────────
✓ Issue #42 closed
✓ Moved to Done
✓ Pushed to origin
```

## Error Handling

If execution fails:

```
❌ FAILURE

Pipeline stage: Stage 4: TESTING
Error: django.core.exceptions.ImproperlyConfigured

Details:
  File: config/settings.py
  Issue: Missing required setting

Action: Fix the issue and run /next-ticket again
         Or run /next-ticket --only-find to restart
```

## Important Rules

1. **One Ticket Only**: Execute exactly one ticket per command run
2. **No Scope Creep**: Don't implement features from other tickets
3. **Follow Pipeline**: Never skip stages
4. **Test Before Commit**: Always pass all tests
5. **No Secrets**: Never hardcode API keys, secrets, or credentials
6. **Clean Code**: Follow project conventions from CLAUDE.md
7. **Atomic Commits**: One ticket = one commit
8. **Clear Messages**: Commit message must reference ticket number

## Usage Examples

```bash
# Execute next ticket in full workflow
/next-ticket

# Dry run - see what would happen
/next-ticket --dry-run

# Just find and show next ticket
/next-ticket --only-find

# Execute but skip git push
/next-ticket --skip-push
```

## GitHub Integration Details

### Finding Issues

The command uses:
```bash
gh issue list --state open \
  --label "epic/setup,epic/auth,epic/core,epic/resources,epic/ai" \
  --limit 50
```

### Ticket Matching

Maps GitHub issues to TICKETS.md by matching:
- Issue title contains "Ticket X.Y"
- Or issue title matches TICKETS.md section heading
- Or issue body references ticket number

### Board Management

Since `gh project` has limited CLI support:
- Uses labels for status (status/backlog, status/in-progress, status/done)
- Assigns issues to track progress
- Comments on issues for audit trail
- Can show manual steps if board drag-drop needed

## Fallback Behavior

If GitHub CLI fails:
1. Show available issues with `gh issue list`
2. Ask user to select ticket number manually
3. Continue with execution
4. Offer to close issue manually at end

## Integration with CLAUDE.md

The command respects all rules from CLAUDE.md:

- **Pipeline Stages**: Uses exact stages from Section 3
- **Skills**: Uses recommended tools for each stage
- **Rules**: Follows coding standards from Section 5
- **Dependencies**: Maintains requirements from Section 7

## Integration with TICKETS.md

- Reads ticket details from TICKETS.md
- Extracts acceptance criteria
- Uses exact acceptance criteria for Stage 5: REVIEW
- Validates all criteria are met before commit

## Success Criteria

Ticket is considered complete when:

✅ All acceptance criteria from TICKETS.md met  
✅ `python manage.py check` passes  
✅ No hardcoded secrets  
✅ Code follows CLAUDE.md standards  
✅ Files created/modified match plan  
✅ Tests show no errors  

## Troubleshooting

**Issue: "No open issues found"**
- Check GitHub project board exists
- Verify issues are labeled correctly
- Run `gh issue list --state open` manually to see all issues

**Issue: "GitHub CLI not authenticated"**
- Run: `gh auth login`
- Select appropriate authentication method

**Issue: "Python manage.py check fails"**
- Don't commit or push
- Show error details
- Suggest fixes based on error message

**Issue: "Ticket criteria not met"**
- Don't commit or push
- Show which criteria failed
- Provide specific suggestions

## Manual Override

If automated process fails, you can:

1. Manually edit issue in GitHub
2. Run specific pipeline stage:
   ```
   /next-ticket --only-research
   /next-ticket --only-planning
   /next-ticket --only-implementation
   /next-ticket --only-testing
   /next-ticket --only-review
   ```
3. Manually run git commands
4. Manually close issue

## Future Enhancements

Possible improvements:
- Integration with GitHub Pages project v2 API
- Parallel execution of independent tickets
- Automatic rollback on failure
- Metrics collection (time per ticket, success rate)
- Slack notifications on completion

---

**Command Version**: 1.0  
**Last Updated**: 2026-07-09  
**Status**: Production Ready

Created for Learning Companion MVP Project (Recap Project 6)
