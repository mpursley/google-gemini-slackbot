# Slack Bot with Google Gemini

This Slack Bot integrates Google Gemini's AI technology into Slack, offering a smart, responsive assistant that enhances productivity. Follow these steps to set up and deploy your bot.

### New Features
* **Multi-turn Conversations:** The bot now supports threaded replies. You can ask follow-up questions within a thread (e.g., "Add 10 more"), and the bot will remember previous interactions to maintain context.
* **Cloud Run Support:** Includes helper scripts and a Dockerfile to easily build and deploy the bot to Google Cloud Run.

## Accessing the SlackBot from Slack Channel with an App Mention

![Accessing the SlackBot from Slack Channel with an App Mention
](https://i0.wp.com/www.marketcalls.in/wp-content/uploads/2024/02/image-38.png?resize=1024%2C463&ssl=1)

## Accessing the SlackBot Using Direct Message

![Accessing the SlackBot Using Direct Message](https://i0.wp.com/www.marketcalls.in/wp-content/uploads/2024/02/image-37.png?resize=1024%2C439&ssl=1)


## Resources

For a detailed step-by-step guide on building this digital assistant, visit [Building a Digital Assistant in Slack with Google Gemini: A Step-by-Step Guide](https://www.marketcalls.in/python/building-a-digital-assistant-in-slack-with-google-gemini-a-step-by-step-guide.html).

## Prerequisites

- Google Gemini API Key
- Slack App with OAuth & Permissions configured
- Python environment with necessary libraries
- Google Cloud CLI: Required if using the included deployment scripts for Cloud Run.
- Docker: Required if deploying via container or running locally with Docker.

## Configuration

Before running the project, you need to set up your environment variables. A sample environment file `.env.sample` is provided in the project. Copy this file to a new file named `.env` and update the variables with your own values.

The `.env.sample` file contains the following structure:<br>
<code>
GOOGLE_API_KEY=your_google_api_key_here<br>
SLACK_BOT_TOKEN=your_slack_bot_token_here<br>
BOT_USER_ID=your_bot_user_id_here<br>
FLASK_APP=your_entry_point_script_here # e.g., "app.py"<br>
PROJECT_ID=your_google_cloud_project_id # Required for Cloud Run deployment<br></code>


### Steps to configure your environment:

1. Copy the `.env.sample` file to a new file named `.env` in the root directory of the project.
2. Replace `your_google_api_key_here`, `your_slack_bot_token_here`, `your_bot_user_id_here`, `your_entry_point_script_here`, and `your_google_cloud_project_id` with your actual configuration values.

**Note:** Never commit your `.env` file or any sensitive credentials to version control. The `.env` file is included in the `.gitignore` to prevent accidental upload.


## Setup Instructions

1. **Obtain Google Gemini API Key**: Visit Google AI Studio and generate an API key for the Gemini API.
2. **Generate Slack App**: Create a new app in Slack and configure basic information, including OAuth scopes required for the bot to function.
3. **Setup Event Subscriptions**: Subscribe to bot events in your Slack app settings to listen for and respond to messages.
4. **Install Your App**: Add your app to your workspace with the necessary permissions.
5. **Development Environment**:
   - Use Visual Studio Code or your preferred IDE.
   - Create a Python virtual environment and activate it.
   - Install necessary Python libraries including Flask, Slack SDK, and Google Gemini libraries.
6. **Implement Your Slack Bot**: Use Flask for handling Slack events and Google Gemini for generating responses.
7. **Deploy Your Application**: Choose between local testing with ngrok, deploying to Google Cloud App Engine, or Google Cloud Run.
8. **Configure Slack Event Subscriptions**: Update your Slack app's event subscriptions with your deployment's request URL.
9. **Access Your Slack Bot**: Test your bot via direct message or by mentioning it in a channel.

## Dependencies

Ensure your project has all the necessary dependencies by installing the required libraries which include Flask, various Google and Slack SDKs, and other utility libraries.<br>

Flask<br>
google-ai-generativelanguage<br>
google-api-core<br>
google-auth<br>
google-generativeai<br>
googleapis-common-protos<br>
gunicorn<br>
requests<br>
slack_sdk<br>
colorama<br>
python-dotenv<br>

To install the required dependencies for this project, follow the steps below:
Run the following command to install the dependencies listed in `requirements.txt`:

<code>pip install -r requirements.txt</code>

## Deployment

### Deployment to Google Cloud Run

This project now includes scripts to automate the deployment process to Google Cloud Run using Docker.

**1. Deploy Service**
Run the following script to build the container and deploy it to your Google Cloud project:
```bash
./start_service_in_google_cloudrun.sh
