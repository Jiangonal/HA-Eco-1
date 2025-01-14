import pandas as pd

df = pd.read_csv('pull_requests_all.csv')
existing_url = pd.read_csv('pull_request_comments_commits_codeowners_integrations.csv')['Pull Request URL'].unique()

print(len(df))
print(len(existing_url))
df = df[~df['URL'].isin(existing_url)]
print(len(df))