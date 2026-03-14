# 🚀 AI-SalesGrid 
# 🌟 Intelligent Multi-Agent Sales Automation on AWS

[![Python](https://img.shields.io/badge/language-Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Frontend](https://img.shields.io/badge/frontend-Streamlit-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![AI Platform](https://img.shields.io/badge/AI_Platform-Amazon_Nova_AI-FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/nova/)
[![Cloud](https://img.shields.io/badge/Cloud-AWS-232F3E.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Containerization](https://img.shields.io/badge/container-Docker-2496ED.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)

<div align="center">

<!-- TODO: Add project logo -->

[![GitHub stars](https://img.shields.io/github/stars/fadynabil10/AI-SalesGrid?style=for-the-badge)](https://github.com/fadynabil10/AI-SalesGrid/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/fadynabil10/AI-SalesGrid?style=for-the-badge)](https://github.com/fadynabil10/AI-SalesGrid/network)
[![GitHub issues](https://img.shields.io/github/issues/fadynabil10/AI-SalesGrid?style=for-the-badge)](https://github.com/fadynabil10/AI-SalesGrid/issues)

**Your AI Superpower in Sales for Enterprise - Real-Time AI Multi-Agent Sales Orchestrator**

[AI SalesGrid - Solution on AWS Overview](AI%20SalesGrid%20-%20Solution%20on%20AWS.pdf) |
[Technical Deployment Guide on AWS](AI%20SalesGrid%20-%20Tech%20Deployment%20on%20AWS.pdf)

</div>

## 📖 Overview

AI-SalesGrid is an innovative enterprise solution designed to revolutionize sales processes through real-time AI multi-agent orchestration. Leveraging the power of AWS Bedrock agents and Amazon Nova LLM and deployed on AWS, this system acts as an intelligent sales superpower, automating and optimizing complex sales workflows. It features a user-friendly Streamlit frontend that interacts with an AWS API Gateway, which in turn orchestrates a suite of specialized AI agents.

The project focuses on building an agentic workflow to empower sales professionals, enabling them to close deals faster, personalize customer interactions, and gain actionable insights, ultimately enhancing overall sales efficiency and revenue.

## ✨ Features

*   🎯 **Real-Time Multi-Agent Orchestration**: Deploys and manages a network of specialized AI agents that collaborate to achieve sales objectives.
*   🧠 **Generative AI Integration**: Utilizes AWS Bedrock (Agents + Flow + kb) with Amazon Nova AI to power advanced conversational capabilities, content generation, and intelligent decision-making for sales agents.
*   ☁️ **AWS Native Deployment**: Built for deployment on Amazon Web Services (AWS), leveraging services like API Gateway for robust, scalable, and secure communication.
*   📊 **CRM Integration Readiness**: Designed with architecture capable of integrating with existing CRM systems to enrich agent context and streamline data flow.
*   ⚡ **Enterprise-Grade Scalability**: Engineered for high performance and scalability to meet the demands of large enterprise sales operations.
*   🔒 **Secure & Compliant**: Adheres to AWS's robust security and compliance standards, with secure credential handling via environment variables for sensitive access keys.
*   **Intuitive Streamlit Frontend**: Provides a responsive and interactive chat interface for users to engage with the AI sales assistant.
*   **Automated Sales Workflow:** Manages the entire sales journey from initial client inquiry to final reporting.
*   **Client Requirement Analysis:** Specialized agent analyzes client needs and matches them with available company services, strictly adhering to a knowledge base.
*   **Dynamic Pricing Generation:** An agent generates pricing, validating against predefined rules like discount limits, margin thresholds, and approval policies.
*   **Formal Proposal Generation:** An agent crafts professional proposals following company templates, incorporating solution and pricing details.
*   **Comprehensive Risk Assessment:** An agent evaluates delivery timelines, margin risks, and compliance issues, providing a risk score.
*   **Executive Summary Reporting:** An agent generates concise executive summaries, formatted for CEO dashboards, detailing deal size, margin, risk, and approval status.
*   **Configurable AI Agents:** Agents are configured to utilize specific Amazon Nova AI models or agent IDs.
*   **Containerized Deployment:** Provided Dockerfiles for easy, consistent, and scalable deployment of both frontend and backend agent components.

## 🖥️ Architecture

The system's architecture comprises a Streamlit web frontend, an AWS API Gateway acting as a secure intermediary, and a backend multi-agent system powered by AWS Bedrock. The frontend sends user prompts to the API Gateway using authentication, which then forwards the request to the AWS Bedrock agent for processing. The agent processes the request, potentially orchestrating other sub-agents, and returns a response through the API Gateway back to the Streamlit application.

The detailed architecture is described in the `Architecture Diagram` directory and the `AI SalesGrid - Tech Deployment on AWS.pdf`.

![Main Architecture Diagram](1-%20Architecture%20Diagram/1-%20Main%20Archtiect.png)

## 📚 Tech Stack by Tech field

*   **Languages:** Python 3.8 (Frontend), Python 3.11 (Agent)
*   **Frontend Framework:** Streamlit
*   **AI Agent Platform:** AWS Bedrock
*   **LLM:** Amazon Nova AI
*   **Cloud Platform:** Amazon Web Services (AWS)
    *   **API Gateway:** For secure and scalable API endpoints.
    *   **IAM:** For managing access and authentication.
    *   **Compute (e.g., ECS/EKS/Lambda):** For hosting the Amazon Nova Agent backend.
*   **Containerization:** Docker
*   **Python Libraries:**
    *   `streamlit`: For interactive web applications.
    *   `requests`: For making HTTP calls.
    *   `boto3`, `botocore`: AWS SDK for Python, used for SigV4 authentication.
    *   `asyncio`: For asynchronous operations.
    *   `openai`: Used as a client to interact with the Amazon Nova API.
    *   `adk`: (Implied by `CMD` in agent Dockerfile) Amazon Agent Development Kit.
 
## 🛠️ Tech Stack

**Frontend:**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

**Backend & AI Agents:**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AWS Bedrock](https://img.shields.io/badge/AWS_Bedrock-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white) <!-- Inferred for AI model interaction -->
![LangChain](https://img.shields.io/badge/LangChain-059954?style=for-the-badge&logo=langchain&logoColor=white) <!-- Inferred for multi-agent orchestration -->
![Boto3](https://img.shields.io/badge/Boto3-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white) <!-- For AWS API interaction -->

**Cloud & DevOps:**
![Amazon Web Services](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![AWS Lambda](https://img.shields.io/badge/AWS_Lambda-FF9900?style=for-the-badge&logo=aws-lambda&logoColor=white) <!-- Inferred for serverless functions -->
![AWS API Gateway](https://img.shields.io/badge/AWS_API_Gateway-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white) <!-- Inferred for agent API exposure -->
![AWS S3](https://img.shields.io/badge/AWS_S3-FF9900?style=for-the-badge&logo=amazon-s3&logoColor=white) <!-- Inferred for storage -->
![AWS DynamoDB](https://img.shields.io/badge/AWS_DynamoDB-FF9900?style=for-the-badge&logo=amazon-dynamodb&logoColor=white) <!-- Inferred for state/data persistence -->
![AWS IAM](https://img.shields.io/badge/AWS_IAM-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white) <!-- For access management -->
![CloudFormation](https://img.shields.io/badge/CloudFormation-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white) <!-- Inferred for IaC -->


## 🚀 Quick Start

Follow these steps to get AI-SalesGrid up and running for development and deployment. This project consists of two main components: the Streamlit Frontend and the Amazon Nova Agent.

### Prerequisites

-   **Python 3.8+**: Required for both frontend and agent development.
-   **Docker**: Required for building and running the containerized applications.
-   **AWS CLI**: Recommended for managing AWS credentials and services.
-   **AWS Account**: An active AWS account with billing enabled.
-   **AWS IAM User/Role**: Configured with necessary permissions (e.g., permissions to invoke API Gateway, AWS Bedrock, Lambda).

### Installation and Setup

#### 1. Set up the AWS Bedrock

Bedrock agnet is the core intelligence of AI-SalesGrid.

#### 2. Set up Amazon Nova Agent

Navigate to the agent directory:
```bash
cd Github/3- Amazon Nova Agent
```

**Install Agent Python dependencies:**
While a `requirements.txt` is not explicitly provided for this folder in the project data, the `agent.py` uses `openai`. Create a `requirements.txt` if it doesn't exist:
```bash
echo "openai" > requirements.txt
# Add any other specific ADK dependencies here if known
```

**Build the Agent Docker image:**
```bash
docker build -t ai-salesgrid-nova-agent .
```
**Note on Agent Deployment:** The `agent.py` interacts with `https://api.nova.amazon.com/v1`.



#### 3. Set up the Streamlit Frontend

For Streamlit: The `api_url` in the Streamlit frontend (`Github/2- Streamlit Frontend/app.py`) should point to an AWS API Gateway endpoint that invokes this agent.

Navigate to the frontend directory:
```bash
cd ../../Github/2- Streamlit Frontend
```

**Install Frontend Python dependencies:**
```bash
pip install -r requirements.txt
```

**Build the Frontend Docker image:**
```bash
docker build -t ai-salesgrid-streamlit-frontend .
```

### Configuration (Environment Variables)

Both the frontend and the agent require specific environment variables.


#### For the Amazon Nova Agent (`3- Amazon Nova Agent/`)

The `agent.py` requires an API Key for Amazon Nova. This key is typically set as `<API_KEY>` in the code example, but in a real deployment, it should be an environment variable.

| Variable  | Description                                        | Required |
| :-------- | :------------------------------------------------- | :------- |
| `NOVA_API_KEY` | Your Amazon Nova API key or similar authentication token. | Yes      |

You should also provide the Agent ID (e.g., `AGENT-1fb10db68a5248509d87af7c848751cb`) to the agent application as an environment variable or configuration.


#### For the Streamlit Frontend (`2- Streamlit Frontend/`)

The `app.py` requires AWS credentials and the API Gateway endpoint.

| Variable              | Description                                                               | Required |
| :-------------------- | :------------------------------------------------------------------------ | :------- |
| `AWS_ACCESS_KEY_ID`   | Your AWS Access Key ID with permissions to invoke the API Gateway.          | Yes      |
| `AWS_SECRET_ACCESS_KEY` | Your AWS Secret Access Key.                                               | Yes      |
| `API_GATEWAY_URL`     | The full URL of your AWS API Gateway endpoint that invokes the Nova Agent. | Yes      |

You can set these in your environment or pass them during `docker run`.


---
## 📁 Project Structure

```
.
├── Github/
│   ├── AI SalesGrid - Solution on AWS.pdf      # High-level overview and business case on AWS
│   ├── AI SalesGrid - Tech Deployment on AWS.pdf # Detailed technical deployment guide on AWS
│   ├── README.md                               # This README file
│   ├── 1- Architecture Diagram/                # Contains architectural diagrams
│   │   ├── 1- Main Archtiect.png
│   │   ├── 2- Multi Agent Arch.png
│   │   ├── 3- Architect.png
│   │   └── 4- Advanced Multi Agent with CRM.png
│   ├── 2- Streamlit Frontend/                  # Frontend Streamlit application
│   │   ├── app.py                              # Main Streamlit application
│   │   ├── Dockerfile                          # Docker build instructions for the frontend
│   │   └── requirements.txt                    # Python dependencies for the frontend
│   └── 3- Amazon Nova Agent/                   # Backend Amazon Nova AI Agent
│       ├── Dockerfile                          # Docker build instructions for the agent
│       ├── agents/
│       │   └── ai-salesgrid/
│       │       ├── agent.py                    # Core Amazon Nova Agent logic
│       │       └── __init__.py                 # Python package initializer
│       └── requirements.txt                    # (Implicit) Python dependencies for the agent (e.g., openai)
└── LICENSE                                     # Project license (suggested)
```

---

##  Project Structure

```sh
└── AI-SalesGrid-on-AWS/
    ├── 1- Architecture Diagram
    │   ├── 1- Main Archtiect.png
    │   ├── 2- Multi Agent Arch.png
    │   ├── 3- Architect.png
    │   └── 4- Advanced Multi Agent with CRM.png
    ├── 2- Streamlit Frontend
    │   ├── Dockerfile
    │   ├── app.py
    │   └── requirements.txt
    ├── 3- Amazon Nova Agent
    │   ├── Dockerfile
    │   └── agents
    ├── AI SalesGrid - Solution on AWS.pdf
    └── AI SalesGrid - Tech Deployment on AWS.pdf
```


###  Project Index
<details open>
	<summary><b><code>AI-SALESGRID-ON-AWS/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			</table>
		</blockquote>
	</details>
	<details> <!-- 2- Streamlit Frontend Submodule -->
		<summary><b>2- Streamlit Frontend</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/fadynabil10/AI-SalesGrid-on-AWS/blob/master/2- Streamlit Frontend/app.py'>app.py</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/fadynabil10/AI-SalesGrid-on-AWS/blob/master/2- Streamlit Frontend/requirements.txt'>requirements.txt</a></b></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/fadynabil10/AI-SalesGrid-on-AWS/blob/master/2- Streamlit Frontend/Dockerfile'>Dockerfile</a></b></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- 3- Amazon Nova Agent Submodule -->
		<summary><b>3- Amazon Nova Agent</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/fadynabil10/AI-SalesGrid-on-AWS/blob/master/3- Amazon Nova Agent/Dockerfile'>Dockerfile</a></b></td>
			</tr>
			</table>
			<details>
				<summary><b>agents</b></summary>
				<blockquote>
					<details>
						<summary><b>ai-salesgrid</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/fadynabil10/AI-SalesGrid-on-AWS/blob/master/3- Amazon Nova Agent/agents/ai-salesgrid/agent.py'>agent.py</a></b></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with AI-SalesGrid-on-AWS, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker


###  Installation

Install AI-SalesGrid-on-AWS using one of the following methods:

**Build from source:**

1. Clone the AI-SalesGrid-on-AWS repository:
```sh
❯ git clone https://github.com/fadynabil10/AI-SalesGrid-on-AWS
```

2. Navigate to the project directory:
```sh
❯ cd AI-SalesGrid-on-AWS
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r 2- Streamlit Frontend/requirements.txt
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t fadynabil10/AI-SalesGrid-on-AWS .
```




###  Usage
Run AI-SalesGrid-on-AWS using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```

---



### AWS Configuration
Refer to `AI SalesGrid - Tech Deployment on AWS.pdf` for detailed instructions on configuring AWS services (e.g., IAM roles, S3 buckets, DynamoDB tables, Bedrock access).

## 🚀 Deployment

The AI SalesGrid is designed for robust and scalable deployment on Amazon Web Services.

### Production Build & Deployment Steps

1.  **Review Technical Deployment Guide**:
    Thoroughly read `AI SalesGrid - Tech Deployment on AWS.pdf`. This document contains the authoritative steps for deploying all components on AWS.

2.  **Infrastructure Provisioning**:
    Follow the `AI SalesGrid - Tech Deployment on AWS.pdf` requirements.

3.  **Deploy AWS Bedrock Agents**:
    The agent will likely be deployed as one or more AWS Lambda functions, potentially fronted by AWS API Gateway, or as containers on AWS ECS.
    -   **Lambda Deployment**: Package the agent code and dependencies into a deployment package (`.zip` file) and deploy it to AWS Lambda.
    -   **Container Deployment**: Build a Docker image for the agent and push it to Amazon ECR, then deploy it to AWS ECS.

4.  **Deploy Streamlit Frontend**:
    The Streamlit application can be deployed on AWS using various methods:
    -   **AWS EC2**: Run the Streamlit app on an EC2 instance.
    -   **AWS ECS/Fargate**: Containerize the Streamlit app and deploy it as a service.
    -   **AWS Amplify/S3 + CloudFront**: Serve the static assets (if any) and integrate with a backend.
    
    Refer to `AI SalesGrid - Tech Deployment on AWS.pdf` for the recommended deployment strategy for the Streamlit frontend.

## 📚 API Reference

The AWS Bedrock Agent exposes an API, typically through AWS API Gateway, allowing the Streamlit Frontend and other enterprise systems to interact with the multi-agent orchestration.

### Authentication
Authentication to the Agent API will be handled via AWS IAM roles and policies, or potentially API Gateway custom authorizers/Cognito integration as defined in the AWS deployment strategy.

### Endpoints
The specific endpoints will depend on the agent's functionality and API Gateway configuration. Examples might include:

-   `POST /agent/orchestrate`: Initiate a new sales orchestration task.
-   `GET /agent/status/{task_id}`: Check the status of an ongoing orchestration task.
-   `POST /agent/feedback`: Provide feedback on agent performance.

## 🤝 Contributing

We welcome contributions to AI-SalesGrid! Please see our [Contributing Guide](CONTRIBUTING.md) for details on how to get started, report bugs, and suggest features.

### Development Setup for Contributors

Contributors should follow the "Quick Start" guide for local development. Adherence to Python best practices, clear documentation of agent logic, and unit testing is highly encouraged.

## 🙏 Acknowledgments

-   **AWS Bedrock**: For providing a robust suite of AI and cloud services.
-   **AWS Bedrock Knowledge base and Lambda Actions with data on RDS/Redshift/Dynamodb**: Powering the intelligence of the sales agents.

## 📞 Support & Contact

-   🐛 Issues: [GitHub Issues](https://github.com/fadynabil10/AI-SalesGrid-on-AWS/issues)
-   💬 Discussions: [GitHub Discussions](https://github.com/fadynabil10/AI-SalesGrid-on-AWS/discussions) <!-- TODO: Enable GitHub Discussions if planned -->
-   **💡 [Submit Pull Requests](https://github.com/fadynabil10/AI-SalesGrid-on-AWS/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/fadynabil10/AI-SalesGrid-on-AWS
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/fadynabil10/AI-SalesGrid-on-AWS/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=fadynabil10/AI-SalesGrid-on-AWS">
   </a>
</p>
</details>

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [Fady Nabil](https://github.com/fadynabil10)

</div>


