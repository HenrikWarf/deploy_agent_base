# ADK deployment to Agent Engine Template

This project provides a template for creating and deploying a Vertex AI Agent using the Agent Development Kit (ADK).

## Project Structure

- `agent.py`: Contains the core logic for the agent, including its definition, tools, and deployment to Vertex AI.
- `test_locally.py`: A script to test the agent locally.
- `test_query.py`: A script to test the deployed agent on Vertex AI.
- `requirements.txt`: A list of the Python packages required for this project.
- `.env.example`: An example file for configuring your environment variables.
- `README.md`: This file.

## Setup Instructions

### 1. Prerequisites

- Python 3.9+
- A Google Cloud project with the Vertex AI API enabled.
- The `gcloud` CLI installed and authenticated (`gcloud auth application-default login`).

### 2. Environment Configuration

First, create and activate a Python virtual environment to manage project dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure Credentials

The deployment script requires your Google Cloud project details. Copy the example environment file to a new `.env` file:

```bash
cp .env.example .env
```

Now, open the `.env` file and replace the placeholder values with your actual Google Cloud `PROJECT_ID`, `LOCATION` (e.g., `us-central1`), and a Cloud Storage `STAGING_BUCKET` URI (e.g., `gs://your-bucket-name`). You can also customize the agent's behavior by modifying the other variables in this file.

## How to Use

### Deploy the Agent

To deploy the agent to Vertex AI, run the `agent.py` script:

```bash
python agent.py
```

This script will create and deploy the agent based on the configuration in your `.env` file.

### Test the Agent Locally

To test the agent locally before deploying, run the `test_locally.py` script:

```bash
python test_locally.py
```

This will use the agent configuration from your `.env` file to run the agent in a local environment.

### Test the Deployed Agent

After deploying the agent to Vertex AI, you can test it by running the `test_query.py` script:

```bash
python test_query.py
```

This script will send a test message to your deployed agent and print the response.
