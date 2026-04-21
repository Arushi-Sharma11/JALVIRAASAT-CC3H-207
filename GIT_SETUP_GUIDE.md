# 🔧 Git Setup & Usage Guide

## ✅ What's Been Done

### 1. Git Repository Initialized
```bash
✅ git init - Repository created
✅ .gitignore - Comprehensive ignore rules added
✅ README.md - Full project documentation created
✅ First commit - Files committed to repository
```

---

## 📁 Files Created

### 1. `.gitignore` (Comprehensive)
Excludes from version control:
- ✅ Python cache files (`__pycache__/`, `*.pyc`)
- ✅ Node modules (`node_modules/`)
- ✅ Environment files (`.env`, `venv/`)
- ✅ Database files (`*.db`, `*.sqlite`)
- ✅ ML models (`*.pkl`, `*.h5`)
- ✅ IDE files (`.vscode/`, `.idea/`)
- ✅ OS files (`.DS_Store`, `Thumbs.db`)
- ✅ Build files (`build/`, `dist/`)
- ✅ Log files (`*.log`)
- ✅ Temporary files (`*.tmp`, `*.bak`)
- ✅ Generated images (`*.png`, `*.jpg`)
- ✅ Secrets (`*.key`, `*.pem`)

### 2. `README.md` (Complete Documentation)
Includes:
- ✅ Project overview
- ✅ Features list
- ✅ Tech stack details
- ✅ Installation instructions
- ✅ API documentation
- ✅ ML model info
- ✅ Revenue model summary
- ✅ Usage examples
- ✅ Contributing guidelines

---

## 🚀 Git Commands Reference

### Basic Workflow

#### 1. Check Status
```bash
git status
# Shows modified, staged, and untracked files
```

#### 2. Add Files
```bash
# Add specific file
git add filename.py

# Add all files
git add .

# Add all Python files
git add *.py

# Add specific folder
git add frontend/
```

#### 3. Commit Changes
```bash
# Commit with message
git commit -m "Add new feature"

# Commit with detailed message
git commit -m "Add quiz feature" -m "Includes 50 questions and XP system"

# Add and commit in one step
git commit -am "Update README"
```

#### 4. View History
```bash
# View commit history
git log

# View compact history
git log --oneline

# View last 5 commits
git log -5

# View with graph
git log --graph --oneline
```

#### 5. View Changes
```bash
# View unstaged changes
git diff

# View staged changes
git diff --staged

# View changes in specific file
git diff filename.py
```

---

## 🌿 Branching

### Create & Switch Branches
```bash
# Create new branch
git branch feature/quiz-system

# Switch to branch
git checkout feature/quiz-system

# Create and switch in one command
git checkout -b feature/new-feature

# List all branches
git branch

# Delete branch
git branch -d feature/old-feature
```

### Merge Branches
```bash
# Switch to main branch
git checkout main

# Merge feature branch
git merge feature/quiz-system

# Delete merged branch
git branch -d feature/quiz-system
```

---

## 🔄 Remote Repository (GitHub/GitLab)

### Connect to Remote
```bash
# Add remote repository
git remote add origin https://github.com/username/repo.git

# Verify remote
git remote -v

# Change remote URL
git remote set-url origin https://github.com/username/new-repo.git
```

### Push to Remote
```bash
# Push to main branch
git push origin main

# Push and set upstream
git push -u origin main

# Push all branches
git push --all

# Force push (use carefully!)
git push -f origin main
```

### Pull from Remote
```bash
# Pull latest changes
git pull origin main

# Fetch without merging
git fetch origin

# Pull with rebase
git pull --rebase origin main
```

### Clone Repository
```bash
# Clone repository
git clone https://github.com/username/repo.git

# Clone specific branch
git clone -b branch-name https://github.com/username/repo.git
```

---

## 🔧 Useful Commands

### Undo Changes

#### Unstage Files
```bash
# Unstage specific file
git restore --staged filename.py

# Unstage all files
git restore --staged .
```

#### Discard Changes
```bash
# Discard changes in file
git restore filename.py

# Discard all changes
git restore .
```

#### Undo Last Commit
```bash
# Undo commit but keep changes
git reset --soft HEAD~1

# Undo commit and discard changes
git reset --hard HEAD~1

# Amend last commit
git commit --amend -m "New message"
```

### Stash Changes
```bash
# Save changes temporarily
git stash

# List stashes
git stash list

# Apply last stash
git stash apply

# Apply and remove stash
git stash pop

# Clear all stashes
git stash clear
```

### Tags
```bash
# Create tag
git tag v1.0.0

# Create annotated tag
git tag -a v1.0.0 -m "Version 1.0.0"

# List tags
git tag

# Push tag to remote
git push origin v1.0.0

# Push all tags
git push --tags
```

---

## 📝 Commit Message Conventions

### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting)
- **refactor**: Code refactoring
- **test**: Adding tests
- **chore**: Maintenance tasks

### Examples
```bash
git commit -m "feat(quiz): Add MCQ quiz system with 50 questions"

git commit -m "fix(api): Fix authentication token expiry issue"

git commit -m "docs(readme): Update installation instructions"

git commit -m "style(frontend): Format code with Prettier"

git commit -m "refactor(ml): Optimize model training pipeline"

git commit -m "test(backend): Add unit tests for API endpoints"

git commit -m "chore(deps): Update dependencies to latest versions"
```

---

## 🎯 Recommended Workflow

### Daily Development
```bash
# 1. Start your day - pull latest changes
git pull origin main

# 2. Create feature branch
git checkout -b feature/new-feature

# 3. Make changes and commit frequently
git add .
git commit -m "feat: Add feature X"

# 4. Push to remote
git push origin feature/new-feature

# 5. Create Pull Request on GitHub/GitLab

# 6. After PR approval, merge and delete branch
git checkout main
git pull origin main
git branch -d feature/new-feature
```

---

## 🔒 .gitignore Best Practices

### What to Ignore

✅ **Always Ignore:**
- Dependencies (`node_modules/`, `venv/`)
- Build outputs (`build/`, `dist/`)
- Environment files (`.env`)
- Database files (`*.db`)
- Logs (`*.log`)
- IDE settings (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`)
- Secrets (API keys, passwords)

❌ **Never Ignore:**
- Source code (`.py`, `.js`, `.jsx`)
- Configuration templates (`.env.example`)
- Documentation (`.md`)
- Package files (`package.json`, `requirements.txt`)
- Git files (`.gitignore`, `.gitattributes`)

---

## 🚨 Common Issues & Solutions

### Issue 1: Large Files
```bash
# Error: File too large
# Solution: Add to .gitignore or use Git LFS

git lfs install
git lfs track "*.pkl"
git add .gitattributes
```

### Issue 2: Merge Conflicts
```bash
# When merge conflict occurs:
# 1. Open conflicted files
# 2. Resolve conflicts manually
# 3. Mark as resolved

git add conflicted-file.py
git commit -m "Resolve merge conflict"
```

### Issue 3: Accidentally Committed Secrets
```bash
# Remove from history (use carefully!)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

# Then force push
git push origin --force --all
```

### Issue 4: Wrong Commit Message
```bash
# Change last commit message
git commit --amend -m "Correct message"

# If already pushed
git push --force origin main
```

---

## 📊 Git Status Explained

```bash
$ git status

On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   feature.py      # Staged (ready to commit)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes)
        modified:   main.py         # Modified but not staged

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        temp.py                     # New file, not tracked
```

---

## 🎯 Project-Specific Git Workflow

### For This Financial App

#### Feature Development
```bash
# 1. Create feature branch
git checkout -b feature/add-investment-tracking

# 2. Develop feature
# ... make changes ...

# 3. Commit changes
git add .
git commit -m "feat(investment): Add investment tracking module"

# 4. Push to remote
git push origin feature/add-investment-tracking

# 5. Create Pull Request
```

#### Bug Fixes
```bash
# 1. Create bugfix branch
git checkout -b fix/quiz-xp-calculation

# 2. Fix bug
# ... make changes ...

# 3. Commit fix
git add .
git commit -m "fix(quiz): Correct XP calculation for streak bonus"

# 4. Push and create PR
git push origin fix/quiz-xp-calculation
```

#### Documentation Updates
```bash
# 1. Update docs on main branch
git checkout main

# 2. Make changes
# ... edit README.md ...

# 3. Commit
git add README.md
git commit -m "docs(readme): Update API documentation"

# 4. Push
git push origin main
```

---

## 🔗 GitHub/GitLab Setup

### Create Repository on GitHub

1. Go to GitHub.com
2. Click "New Repository"
3. Name: `financial-intelligence-app`
4. Description: "AI-powered personal finance management platform"
5. Keep it Public or Private
6. Don't initialize with README (we already have one)
7. Click "Create Repository"

### Connect Local to GitHub
```bash
# Add remote
git remote add origin https://github.com/yourusername/financial-intelligence-app.git

# Push to GitHub
git push -u origin main

# Verify
git remote -v
```

---

## 📋 Pre-Commit Checklist

Before committing, ensure:
- [ ] Code runs without errors
- [ ] Tests pass (if any)
- [ ] No sensitive data (API keys, passwords)
- [ ] Code is formatted properly
- [ ] Comments are clear
- [ ] Commit message is descriptive
- [ ] .gitignore is updated if needed

---

## 🎓 Git Best Practices

### Do's ✅
- Commit frequently with clear messages
- Use branches for features
- Pull before pushing
- Review changes before committing
- Keep commits focused (one feature/fix per commit)
- Write meaningful commit messages
- Use .gitignore properly

### Don'ts ❌
- Don't commit sensitive data
- Don't commit large binary files
- Don't force push to main branch
- Don't commit broken code
- Don't use vague commit messages ("fix", "update")
- Don't commit generated files
- Don't work directly on main branch

---

## 🚀 Quick Reference

```bash
# Setup
git init                          # Initialize repo
git clone <url>                   # Clone repo

# Basic
git status                        # Check status
git add .                         # Stage all
git commit -m "message"           # Commit
git push origin main              # Push

# Branching
git branch                        # List branches
git checkout -b feature           # Create branch
git merge feature                 # Merge branch

# Remote
git remote add origin <url>       # Add remote
git pull origin main              # Pull changes
git push origin main              # Push changes

# Undo
git restore file.py               # Discard changes
git reset --soft HEAD~1           # Undo commit
git stash                         # Save changes

# Info
git log                           # View history
git diff                          # View changes
git remote -v                     # View remotes
```

---

## 📞 Need Help?

- **Git Documentation**: https://git-scm.com/doc
- **GitHub Guides**: https://guides.github.com
- **Git Cheat Sheet**: https://education.github.com/git-cheat-sheet-education.pdf

---

## ✅ Current Repository Status

```
Repository: Initialized ✅
Branch: main
Commits: 1
Files Tracked: 2 (.gitignore, README.md)
Remote: Not connected (add GitHub/GitLab URL)

Next Steps:
1. Create GitHub repository
2. Connect remote: git remote add origin <url>
3. Push: git push -u origin main
4. Start developing features!
```

---

**Happy Coding! 🚀**
