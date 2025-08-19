# ADK Agent Deployment to Vertex AI

This project contains Python scripts to define and deploy a sample Agent Development Kit (ADK) agent to the Vertex AI Agent Engine.

## Project Structure

- `agent.py`: Contains the core logic and definition of the ADK agent and its tools.
- `deploy.py`: The script that handles the deployment of the agent to Vertex AI.
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

Now, open the `.env` file and replace the placeholder values with your actual Google Cloud `PROJECT_ID`, `LOCATION` (e.g., `us-central1`), and a Cloud Storage `STAGING_BUCKET` URI (e.g., `gs://your-bucket-name`).

## How to Deploy

With your environment configured, run the deployment script:

```bash
python deploy.py
```

This script will import the agent defined in `agent.py`, initialize Vertex AI, and deploy it. If the deployment is successful, it will print the resource name of your new agent, which you can use to interact with it via the Vertex AI API.
