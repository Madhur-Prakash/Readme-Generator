# Readme-Generator

**A FastAPI-Based Custom README Generator for GitHub Repositories**

## Overview
This repository provides a FastAPI-based application for generating custom README files for GitHub repositories. It allows users to create professional and visually engaging README files using markdown formatting.

---

## Features
- **Customizable README Templates**: Generate README files with custom sections, headers, and content.
- **FastAPI-Powered**: Built with FastAPI for high performance and scalability.
- **Markdown Formatting**: Supports markdown syntax for formatting and styling README content.
- **Easy to Use**: Simple and intuitive API for generating custom README files.

---

## Technology Stack
- **Backend Framework**: FastAPI
- **Programming Language**: Python
- **Database**: Not applicable (in-memory processing)
- **Markdown Parsing**: Uses Python's built-in markdown library

---

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:Madhur-Prakash/Readme-Generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Readme-Generator
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up .env:
- LANGCHAIN_API_KEY = "YOUR_LANGCHAIN_API_KEY"
- GROQ_API_KEY = "YOUR_GROQ_API_KEY"
- SESSION_SECRET_KEY = "YOUR_SESSION_SECRET_KEY"

---

## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```
2. Access the API documentation at:
   ```
   http://127.0.0.1:8000/docs
   ```
3. Use the API to generate custom README files by providing the required information.

---

## API Endpoints

### README Generation Endpoints
- **POST /generate-readme**: Generate a custom README file based on the provided data.

---

## Project Structure

```plaintext
Readme-Generator/
├── .env
├── .gitignore  # gitignore file for GitHub
├── Dockerfile
├── README.md  # Project documentation
├── __init__.py  # initializes package
├── app.py  # main FastAPI app
├── generator
│   ├── helpers
│   │   ├── __init__.py  # initializes package
│   │   └── utils.py
│   ├── models
│   │   ├── __init__.py  # initializes package
│   │   └── models.py  # models
│   └── src
│       ├── __init__.py  # initializes package
│       └── readme.py
├── prompt.md
└── requirements.txt
```

---

## Future Enhancements
- Add support for more advanced markdown features.
- Implement a web interface for easier usage.
- Enhance error handling and logging for better debugging.

---

## Contribution Guidelines

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author
**Madhur Prakash**  
[GitHub](https://github.com/Madhur-Prakash) | [Medium](https://medium.com/@madhurprakash2005)