# Slack Bot with Google Gemini

This Slack Bot integrates Google Gemini's AI technology into Slack, offering a smart, responsive assistant that enhances productivity.

### New Features
* **Multi-turn Conversations:** The bot now supports threaded replies, maintaining context across multiple turns of conversation. You can ask follow-up questions within a thread (e.g., "Add 10 more"), and the bot will remember previous interactions.
* [cite_start]**Containerized Deployment:** Includes Docker support and helper scripts for easy deployment to Google Cloud Run[cite: 91, 499].

## Prerequisites
* **Google Gemini API Key:** Access to Google AI Studio.
* **Slack App:** With OAuth & Permissions configured.
* [cite_start]**Google Cloud CLI (`gcloud`):** Installed and authenticated (for Cloud Run deployment) [cite: 558-567].
* **Python 3.12+:** For local development.
* **Docker:** (Optional) If you prefer running the container locally.

## Configuration

Before running the project, you need to set up your environment variables. [cite_start]A sample environment file `.env.sample` is provided in the project[cite: 738].

1.  Copy the `.env.sample` file to a new file named `.env` in the root directory:
    ```bash
    cp .env.sample .env
    ```
2.  [cite_start]Update the variables in `.env` with your actual values[cite: 747]:
    ```ini
    GOOGLE_API_KEY=your_google_api_key_here
    SLACK_BOT_TOKEN=your_slack_bot_token_here
    BOT_USER_ID=your_bot_user_id_here
    PROJECT_ID=your_google_cloud_project_id  # Added for Cloud Run scripts
    FLASK_APP="app.py"
    ```

> **Note:** Never commit your `.env` file or any sensitive credentials to version control. [cite_start]The `.env` file is included in `.gitignore` to prevent accidental upload [cite: 749-750].

## Setup Instructions

1.  **Obtain Google Gemini API Key:** Visit Google AI Studio and generate an API key.
2.  **Generate Slack App:** Create a new app in Slack and configure basic information.
3.  [cite_start]**Setup Event Subscriptions:** Subscribe to bot events (specifically `app_mention` and `message.im`) in your Slack app settings[cite: 754].
4.  **Install Your App:** Add your app to your workspace with the necessary permissions.

## Deployment to Google Cloud Run

This project now includes scripts to automate deployment to Google Cloud Run.

### 1. Deploy
[cite_start]Run the start script to build the container and deploy the service [cite: 499, 594-617]:
```bash
chmod +x start_service_in_google_cloudrun.sh
./start_service_in_google_cloudrun.sh
