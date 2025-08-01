# Readme-Generator

**A Streamlit-Based README Generator for GitHub Repositories**

## Overview
This repository provides a FastAPI-based application for generating custom README files for GitHub repositories. It allows users to create professional and visually engaging README files using markdown formatting.

---

## Features
- **Customizable README Generation**: Create README files tailored to your project's needs.
- **Markdown Formatting**: Utilize markdown syntax for a professional and visually appealing README.
- **FastAPI-Powered**: Built with FastAPI for high performance and scalability.
- **Streamlit Interface**: Interactive interface for easy README generation.
- **Docker Support**: Run the application using Docker for convenience and portability.

---

## Technology Stack
- **Interface**: Streamlit
- **Containerization**: Docker
- **Programming Language**: Python

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Madhur-Prakash/Readme-Generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Readme-Generator
   ```
3. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5.  Set up .env:

```plaintext
SECRET_KEY = "YOUR_SECRET_KEY"
LANGCHAIN_API_KEY = "YOUR_LANGCHAIN_API_KEY"
GROQ_API_KEY = "YOUR_GROQ_API_KEY" 
```
---
6. Run the Streamlit app:
   ```bash
   streamlit run .\generator\src\readme.py
   ```
Alternatively, you can use Docker:
1. Build the Docker image:
   ```bash
   docker build -t readme .
   ```
2. Run the Docker container:
   ```bash
   docker run -d --name Readme -p 8501:8501  readme
   ```

---

## Usage

1. Access the Streamlit app at `http://localhost:8501` (default port).
2. Follow the interactive prompts to generate your custom README file.

---

## Future Enhancements
- Add support for more advanced markdown features.
- Implement a user interface for easier README generation.
- Enhance error handling and logging.

---

## Contribution Guidelines

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and submit a pull request.

---

## License
This project is distributed under the "Open Source License — Madhur Prakash", based on the MIT License. See the [LICENSE](LICENSE.md) file for details.

---

## Author
**Madhur-Prakash**  
[GitHub](https://github.com/Madhur-Prakash) | [Medium](https://medium.com/@madhurprakash2005)