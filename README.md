# 🤖 PromptCraft AI

### Prompt Engineering Playground

PromptCraft AI is an interactive web application built using Python, Streamlit, and the Groq API. It allows users to enter prompts, generate AI responses, and control response creativity and length through adjustable generation settings.

## 🚀 Features

- **Interactive Prompt Input:** Enter any prompt and generate an AI response.
- **Temperature Control:** Adjust response randomness and creativity.
- **Maximum Tokens Control:** Set the maximum output token limit.
- **AI-Powered Responses:** Generate responses using a large language model through the Groq API.
- **Simple User Interface:** Easy-to-use interface developed with Streamlit.
- **Secure API Configuration:** Store the API key in an environment variable instead of hardcoding it.

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- Large Language Models (LLMs)
- python-dotenv

## 📂 Project Structure

PromptCraft-AI/
│
├── app.py
├── llm.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore

## ⚙️ Installation and Setup

### 1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd PromptCraft-AI

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository URL.

### 2. Create a Virtual Environment

python -m venv venv

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Groq API Key

Create a `.env` file in the project directory.

Add your API key:

```text
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your actual Groq API key.

Get an API key from:
https://console.groq.com/keys

**Important:** Never upload your `.env` file or expose your API key on GitHub.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🎛️ Generation Settings

### Temperature

Temperature controls the randomness of the model's response.

* Lower values generally produce more predictable responses.
* Higher values generally produce more varied and creative responses.

### Maximum Tokens

Maximum Tokens sets the upper limit on the number of tokens generated in the response.

* Lower values limit the response length.
* Higher values allow longer responses, subject to the model's limits.

The available settings depend on the model and API configuration.

## 💡 Example Prompt

```text
Explain Artificial Intelligence in simple English
with three real-world examples.
```

Enter the prompt, adjust Temperature and Maximum Tokens, and click the Generate Response button.

## 🔐 Security

* API keys are stored in the `.env` file.
* The `.env` file is excluded from Git using `.gitignore`.
* Never commit API keys or other sensitive credentials to a public repository.

## 🎯 Project Objective

The objective of PromptCraft AI is to demonstrate prompt-based interaction with a large language model and explore how generation parameters influence AI-generated responses through a simple web interface.

## 🔮 Future Enhancements

* Add zero-shot and few-shot prompting examples.
* Introduce role-based prompting.
* Add prompt templates for common tasks.
* Provide options for summarization and question answering.
* Deploy the application for public access.

## 👩‍💻 Author
AFREEN NISHA .M 

Developed as a Prompt Engineering project using Python, Streamlit, and the Groq API.

## 📄 License

This project is available for educational and learning purposes.

