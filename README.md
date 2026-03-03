# Open a new file, README.md with VSCode
code README.md

# I make some edits in the editor, then close it

# Now check the repo, we should see a change
git status

# Add the file to the staging area
# Can also use git add . to add all files
git add README.md

# Make a commit with the given message
git commit -m "Initial commit"

# Check again
git status

# Look at the history
git log