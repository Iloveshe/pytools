import subprocess
import os

# Get the repository path, branch and user name from the user
repo_path = input("Enter the path to the repository: ")
branch_name = input("Enter the branch name: ")
user_name = input("Enter the user name: ")

# Change the current working directory
os.chdir(repo_path)

# Run the git log command
cmd = f'git log --author="{user_name}" --pretty=tformat: --numstat'
result = subprocess.run(cmd, capture_output=True, text=True, shell=True)

# Process the output
lines = result.stdout.splitlines()
add, subs, loc = 0, 0, 0
for line in lines:
    parts = line.split('\t')
    if len(parts) >= 2:
        add += int(parts[0])
        subs += int(parts[1])
        loc += int(parts[0]) + int(parts[1])
        nedadd = add - subs

print(f"added lines: {add} removed lines: {subs} total lines: {loc} net added lines: {nedadd}")