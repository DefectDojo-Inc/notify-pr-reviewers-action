# Notify PR Reviewers

This GitHub Action sends a Slack notification to reviewers about pending pull requests in a given repository. It is designed to help teams stay on top of PR reviews by delivering automated reminders via Slack.

## 📦 Features

- Queries open PRs in a GitHub repository
- Sends notifications via Slack
- Customizable via workflow inputs

## 🛠️ Inputs

| Name          | Description                                           | Required |
| ------------- | ----------------------------------------------------- | -------- |
| `owner`       | GitHub owner or organization name                     | ✅ Yes   |
| `repository`  | GitHub repository name (without the owner prefix)     | ✅ Yes   |
| `gh_token`    | GitHub token to authenticate and fetch PR information | ✅ Yes   |
| `slack_token` | Slack Bot User OAuth token (`xoxb-...`)               | ✅ Yes   |

## 📥 Usage

Here's an example workflow that runs this action daily at 11:00 AM CT Monday - Friday to remind reviewers about open pull requests:

```yaml
name: Daily PR Review Reminder

on:
  schedule:
    - cron: "0 16 * * 1-5" # 11:00 AM CT M-F
  workflow_dispatch:

jobs:
  notify-reviewers:
    runs-on: ubuntu-latest
    steps:
      - name: Notify reviewers in Slack
        uses: your-org/notify-pr-reviewers-action@master
        with:
          owner: "DefectDojo"
          repository: "django-DefectDojo"
          gh_token: ${{ secrets.GITHUB_TOKEN }}
          slack_token: ${{ secrets.SLACK_BOT_TOKEN }}
```

💡 Tip: Make sure your Slack bot has access to the appropriate channel and the chat:write permission.

🔐 Secrets

- GITHUB_TOKEN: Generally will be a PAT.
- SLACK_BOT_TOKEN: Your Slack bot token with permission to post messages.
