# Git Workshop
## Directory structure
```
.
├── Exercise_CIR1_HHQFQDoFile2_2Page_Analysis.do
├── .gitignore   <-- Tell git what to ignore
├── LICENSE   <-- How can others use your repo?
├── README.md
├── data
│   └── CI
│       └── R1
│           └── CIR1_WealthWeightAll_6Dec2017.dta
└── templates
    └── PMA_SOI_2P
        └── DoFiles
            ├── CCRX_HHQFQDoFile2_2Page_Analysis.do
            └── PMA2020_MedianDefineFn_simple.do
```

## Exercises 

<!---
### Use Case 1 - Personal Repo
- Personal changes over time; saving (interactive)
  - Init repo.
  - Add; commit.
  - Remove; commit.
  - Add/remove file
  - Add/remove hunks
- Testing things out
  - Create branch; try stuff out; go back
- Reset to specific commits
  - Must be a branch from most recent work.

### Use Case 2 - Collaboration
--->

#### Part 1
Taking someone's file and making changes to send back. 
  1. Fork
  2. Clone
  3. Make branch
     - Branches can be used in 
different ways. One possible way to use branches is to make a new branch 
whenever development starts for a new country survey round.
  4. Make changes
  5. Push
  6. Pull request
  7. Getting feedback
  8. Making more changes (if requested by a/the maintainer)
  9. Merge pull request (done by a/the maintainer)

#### Part 2
Updating your repo from someone else's changes.

  10. Fetch changes
  11. Merge or rebase
  12. Handle merge conflicts

Merge conflicts can happen when the same "hunk" is affected in both branches, after 
    they have diverged, and before they have re-merged.
