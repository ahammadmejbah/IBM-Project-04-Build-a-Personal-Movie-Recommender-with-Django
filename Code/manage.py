import os
import subprocess
from random import randint
from datetime import datetime, timedelta

# Define the repository path (optional)
# repo_path = '/path/to/your/repo'
# os.chdir(repo_path)

# Number of days to simulate
TOTAL_DAYS = 365

# Number of commits per day
MIN_COMMITS_PER_DAY = 1
MAX_COMMITS_PER_DAY = 100

# Files to modify in each commit
FILES_TO_MODIFY = ['file1.txt', 'file2.txt', 'file3.txt']

def run_command(command, cwd=None):
    """
    Runs a shell command and handles errors.
    """
    try:
        subprocess.run(command, check=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing: {' '.join(command)}")
        print(e)
        exit(1)

# Initialize the repository (optional)
# Ensure that the repository has at least one commit
# run_command(['git', 'init'])
# run_command(['git', 'add', '.'])
# run_command(['git', 'commit', '-m', 'Initial commit'])

# Start from today and go back TOTAL_DAYS
start_date = datetime.now()

for day in range(1, TOTAL_DAYS + 1):
    commits_today = randint(MIN_COMMITS_PER_DAY, MAX_COMMITS_PER_DAY)
    commit_date = start_date - timedelta(days=day)
    # Generate a base ISO 8601 date string
    base_date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S')

    for commit_num in range(1, commits_today + 1):
        # Modify multiple files
        for file in FILES_TO_MODIFY:
            file_path = os.path.join('.', file)
            try:
                with open(file_path, 'a') as f:
                    f.write(f"Commit from {day} days ago, commit {commit_num}\n")
            except FileNotFoundError:
                # If the file doesn't exist, create it
                with open(file_path, 'w') as f:
                    f.write(f"Created by commit from {day} days ago, commit {commit_num}\n")

        # Stage all changes
        run_command(['git', 'add', '.'])

        # Create a unique commit message
        commit_message = f"Commit {day}-{commit_num} days ago"

        # Use the same base date but add minutes to differentiate commits
        commit_time = commit_date + timedelta(minutes=commit_num)
        commit_time_str = commit_time.strftime('%Y-%m-%dT%H:%M:%S')

        # Commit with the specified date
        run_command([
            'git', 'commit',
            '--date', commit_time_str,
            '-m', commit_message
        ])

    print(f"Completed {commits_today} commits for {day} days ago.")

# Push all commits to the remote repository
# Ensure that the remote 'origin' is set and you have the necessary permissions
run_command(['git', 'push', '-u', 'origin', 'main'])

print("All commits have been successfully pushed to the remote repository.")
