# crypto-analysis-agent
**📈 AI Cryptocurrency Analysis Agent

A simple, beginner-friendly AI agent that analyzes cryptocurrencies using data from the CoinGecko API and insights from OpenAI's GPT model. This project is designed to be set up and run easily within a GitHub Codespace, requiring no local installation.

🌟 What Does This Agent Do?

This agent performs three simple tasks:

Asks for Input: It prompts you to enter the name of a cryptocurrency (e.g., "Bitcoin", "Ethereum").

Fetches Live Data: It connects to the free CoinGecko API to get the current price and market capitalization for that cryptocurrency.

Generates AI Analysis: It sends this data to the OpenAI API and asks it to provide a simple, easy-to-understand analysis and a general sentiment (Positive, Neutral, or Negative).

🛠️ Technology Stack

Language: Python

AI Model: OpenAI GPT-3.5-Turbo

Data Source: CoinGecko Public API

Environment: GitHub Codespaces (No local setup needed!)

Key Libraries: openai, requests

Note on Azure ML: While this simple agent uses the OpenAI API directly, a more advanced, production-ready version could be deployed and managed using Azure Machine Learning. Azure ML is excellent for training, deploying, and monitoring complex models, which is a great next step after mastering this basic project.

🚀 Step-by-Step Setup in GitHub Codespaces

Follow these steps exactly to get your agent running in minutes.

Step 1: Create a New GitHub Repository

Go to GitHub and log in.

Click the + icon in the top-right corner and select "New repository".

Give your repository a name (e.g., crypto-analysis-agent).

Important: Check the box that says "Add a README file".

Click "Create repository".

Step 2: Launch Your Codespace

On your new repository's page, click the green < > Code button.

Go to the "Codespaces" tab.

Click "Create codespace on main".

Wait a minute or two for GitHub to set up your cloud-based development environment. It will open a full VS Code editor right in your browser.

Step 3: Add Your OpenAI API Key as a Secret

This is the most important step to keep your API key safe.

Go back to your GitHub repository's main page.

Click on the "Settings" tab.

In the left sidebar, under "Security", click on "Secrets and variables" > "Codespaces".

Click the "New repository secret" button.

For Name, enter exactly: OPENAI_API_KEY

For Secret, paste your actual API key from OpenAI (it starts with sk-...).

Click "Add secret". Your key is now securely stored and accessible to your Codespace without being visible in your code.

Step 4: Create the Project Files

In your Codespace, you will see a file explorer on the left. You already have a README.md file. Let's create the others.

Create agent.py:

Click the "New File" icon in the explorer.

Name it agent.py.

Copy the Python code I provided earlier and paste it into this file.

Create requirements.txt:

Click the "New File" icon again.

Name it requirements.txt.

Copy the content for the requirements file and paste it in.

Create .gitignore:

Click the "New File" icon.

Name it .gitignore (the dot at the beginning is important).

Copy the content for the gitignore file and paste it in.

Your file explorer should now look like this:

- .gitignore
- README.md
- agent.py
- requirements.txt


Step 5: Install Dependencies and Run the Agent

Open the Terminal: In your Codespace, press Ctrl + ``  (the backtick key, usually next to the 1 key) or go to the top menu and select "Terminal" > "New Terminal".

Install Packages: In the terminal, type the following command and press Enter. This will read your requirements.txt file and install the necessary libraries.

pip install -r requirements.txt


Run the Agent: Once the installation is complete, run the agent with this command:

python agent.py


🎉 How to Use the Agent

If everything is set up correctly, the agent will start in the terminal.

It will display a welcome header.

It will prompt you: Enter the name of a cryptocurrency (e.g., Bitcoin):

Type a name like Dogecoin or Solana and press Enter.

The agent will then fetch the data, connect to OpenAI, and print a formatted report for you!

📄 License

This project is open-source and available under the MIT License.**
