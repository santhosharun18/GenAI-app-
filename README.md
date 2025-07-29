# LangChain Gemma Demo with Ollama

This project demonstrates a simple conversational AI application built with LangChain, Streamlit, and the Gemma model running locally via Ollama. It leverages Langsmith for tracing and monitoring.

## Features

* **Conversational AI:** Interact with the Gemma language model for question-answering.
* **Local LLM Inference:** Utilizes Ollama to run the Gemma model directly on your machine.
* **Streamlit UI:** Provides a user-friendly web interface for interaction.
* **LangChain Integration:** Orchestrates the LLM calls and prompt engineering.
* **LangSmith Tracking:** Integrates with LangSmith for visibility into your LLM application's traces, making debugging and optimization easier.

## Technologies Used

* **Python:** The core programming language.
* **LangChain:** Framework for developing applications powered by language models.
* **Ollama:** A tool for running large language models locally.
* **Streamlit:** For creating the interactive web application.
* **python-dotenv:** For managing environment variables.
* **LangSmith:** For tracing and debugging LangChain applications.

## Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.9+**
* **Ollama:** Download and install Ollama from [ollama.com](https://ollama.com/).
* **Gemma Model:** Pull the `gemma` model using Ollama. Open your terminal and run:
    ```bash
    ollama pull gemma:2b # Or gemma:7b if your system has enough RAM.
    ```
    *(Note: The `app.py` currently specifies `gemma3` which might be a typo or a custom model. Ensure you pull the correct `gemma` model version available on Ollama, e.g., `gemma:2b` or `gemma:7b`). If `gemma3` is a specific custom model, make sure it's available via your Ollama instance.*

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**

    * **On Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate
        ```
    * **On Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    [cite_start]Install the required Python packages[cite: 2].

    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure Environment Variables:**
    [cite_start]Create a `.env` file in the root of your project directory [cite: 1] (the same directory as `app.py`). This file will store your API keys and project settings.

    Add the following to your `.env` file:

    ```env
    LANGCHAIN_API_KEY="your_langchain_api_key_here"
    LANGCHAIN_PROJECT="GenAIAPPWithOPENAI"
    ```
    *Replace `"your_langchain_api_key_here"` with your actual LangChain API key from [LangSmith](https://smith.langchain.com/).*

## Running the Application

1.  **Ensure Ollama server is running.**
2.  **Activate your virtual environment** (if not already activated).
3.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    This will open the application in your web browser. You can then type your questions into the text input field and get responses from the Gemma model.

## Project Structure

* `app.py`: The main Streamlit application script.
* [cite_start]`.env`: Stores environment variables[cite: 1].
* [cite_start]`requirements.txt`: Lists Python dependencies[cite: 2].

## Customization

* **Change LLM Model:** You can easily switch to a different Ollama model by changing the `model` parameter in `app.py`:
    ```python
    llm=Ollama(model="gemma:2b") # Change to 'llama2', 'mistral', etc.
    ```
    Remember to `ollama pull` the new model first.
* **Modify Prompt:** Adjust the `ChatPromptTemplate` in `app.py` to change the system's persona or prompt structure.
* **LangSmith:** Visit your LangSmith dashboard to monitor the traces, inputs, and outputs of your LLM calls.

## Troubleshooting

* **`'streamlit' is not recognized`**: Ensure Streamlit is installed (`pip install streamlit`) and your virtual environment is activated.
* **`Ollama call failed with status code 500` / Memory Error**: The LLM model you're trying to use might require more RAM than available. Try using a smaller quantized version of the model (e.g., `gemma:2b` or `gemma:7b` if you have enough RAM, or even `gemma:2b-instruct-q4_0` if available) or free up system memory.
* **Gemma Model Not Found**: Make sure you have pulled the `gemma` model (or the specific version like `gemma:2b`) using `ollama pull gemma:2b`.
* **LangChain API Key Issues**: Double-check your `LANGCHAIN_API_KEY` in the `.env` file for correctness.

---
