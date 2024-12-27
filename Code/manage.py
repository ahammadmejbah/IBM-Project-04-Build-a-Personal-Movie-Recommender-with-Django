import os
from random import randint

for i in range(1, 365):
    commit_count = randint(1, 2)
    for _ in range(commit_count):
        d = f"{i} days ago"
        with open('file.txt', 'a') as file:
            file.write(d + "\n")  # Added newline for readability

        os.system('git add .')
        # Use proper date formatting for Git
        commit_date = f"{i} days ago"
        os.system(f'git commit --date="{commit_date}" -m "commit {i}"')

# Ensure the final push uses standard spaces
os.system('git push -u origin main')
