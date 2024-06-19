import subprocess
import os
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime

# Get the repository path, branch and user name from the user
repo_path = input("Enter the path to the repository: ")
branch_name = input("Enter the branch name: ")
user_name = input("Enter the user name: ")
show_graph = input("Do you want to show the graph (yes/no): ")

# Change the current working directory
os.chdir(repo_path)

# Run the git log command
if show_graph.lower() == 'yes':
    cmd = f'git log --author="{user_name}" --pretty=format:"%ad" --date=short --numstat'
    # result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
else:
    cmd = f'git log --author="{user_name}" --pretty=tformat: --numstat'
result = subprocess.run(cmd, capture_output=True, text=True, shell=True)

# Process the output
lines = result.stdout.splitlines()
if show_graph.lower() == 'yes':
    netadd_date_dict = defaultdict(int)
    total_date_dict = defaultdict(int)
    for line in lines:
        if line:
            parts = line.split('\t')
            if len(parts) == 1:  # This is a date line
                date = parts[0]
            elif len(parts) >= 3 and date:  # This is a numstat line
                netadd_date_dict[date] += int(parts[0]) - int(parts[1])
                total_date_dict[date] += int(parts[0]) + int(parts[1])

    # Plot the graph
    dates = list(netadd_date_dict.keys())
    dates.sort()
    net_lines = [netadd_date_dict[date] for date in dates]
    total_lines = [total_date_dict[date] for date in dates]
    plt.plot(dates, net_lines, label='Net Lines Added')
    plt.plot(dates, total_lines, label='Total Lines')

    # Add labels to the points
    for i, date in enumerate(dates):
        plt.text(date, net_lines[i], str(net_lines[i]), ha='center', va='bottom')
        plt.text(date, total_lines[i], str(total_lines[i]), ha='center', va='bottom')

    plt.xlabel('Date')
    plt.ylabel('Lines')
    plt.title(f'Lines Added by {user_name} in {branch_name} branch')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()
add, subs, loc, nedadd = 0, 0, 0, 0
for line in lines:
    parts = line.split('\t')
    if len(parts) >= 2:
        add += int(parts[0])
        subs += int(parts[1])
        loc += int(parts[0]) + int(parts[1])
        nedadd = add - subs

print(f"added lines: {add} removed lines: {subs} total lines: {loc} net added lines: {nedadd}")