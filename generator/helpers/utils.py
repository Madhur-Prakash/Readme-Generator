import logging
from fastapi.exceptions import HTTPException
from fastapi import status
import os
from concurrent_log_handler import ConcurrentRotatingFileHandler
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Set default Groq API key and model from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "llama-3.3-70b-versatile")

# Check if Groq API key is available
if not GROQ_API_KEY:
    print("WARNING: No Groq API key found in environment variables. API will not function properly.")



def setup_logging():
    logger = logging.getLogger("readme")
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        file_handler = ConcurrentRotatingFileHandler(
            os.path.join(log_dir, "readme.log"),
            maxBytes=10000,
            backupCount=500
        )
        file_handler.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s - %(filename)s - %(lineno)d",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger

logger = setup_logging()


def calculate_height(text: str, line_height: int = 20, base_height: int = 100):
    lines = text.count('\n') + 1
    return min(800, max(base_height, lines * line_height))


SAMPLE_README_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'prompt.md')
with open(SAMPLE_README_PATH, 'r', encoding='utf-8') as file:
    SAMPLE_README = file.read()

    # print(f"Sample README path: {SAMPLE_README}")
def generate_summary(prompt: str, repo_link: str, folder_structure: str = None):
    try:
        # Initialize LLM with the API key
        llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name=DEFAULT_MODEL
        )
        
        # Create the prompt template
        prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a GitHub README generator that creates clear, professional, and visually engaging README files using markdown formatting. "
     "Your README should follow best practices in terms of structure, content, and presentation. You will be provided with project details, "
     "including title, description, features, usage instructions, technologies used, folder structure, GitHub repository link, and other relevant information.\n\n"
     "Here is your task:\n"
     "- Generate a complete README using markdown.\n"
     "- Use sections in the following order: Title, Overview, Features, Technology Stack, Installation, Usage, API Endpoints (if applicable), "
     "Project Structure (include this section *only* if the folder structure is provided), Future Enhancements, Contribution Guidelines, License, Author.\n"
     "- Make sure section headers are formatted using markdown syntax (e.g., `##`, `###`).\n"
     "- Use bullet points, code blocks, and section dividers (`---`) where appropriate for clarity and aesthetics.\n"
     "- Avoid any commentary, explanation, or meta-text — return *only* the final README content in markdown.\n\n"
     "give only markdown output, do not include any other text or explanation.\n\n"
     "Use the following sample README as a reference for structure and formatting:\n\n"
     "as for author use username form the repo link, if not available use Your Name.\n\n"
     "and as for liscense use MIT License.\n\n"
     "give the folder structure in the Project Structure section only if it is provided, otherwise skip this section.\n\n"
     "Here is a sample README structure to use as reference:\n\n"
     f"{SAMPLE_README}\n\n"
     "Ensure the output closely follows this format. Be concise, complete, and clear."),
     
    ("user", 
     f"Project information to include in the README: {prompt} \n"
     f"GitHub repository link: {repo_link}\n"
     f"Folder structure: {folder_structure if folder_structure else 'No folder structure provided.'}"),

    ("assistant", 
     "Generate a professional, well-formatted README.md based on the provided information, following the structure and clarity of the sample.")
])

        
        # Create and invoke the chain
        chain = prompt | llm | StrOutputParser()
        summary = chain.invoke({"Readme_Gen": prompt})
        logger.info("Generated summary successfully")
        return summary
    except Exception as e:
        logger.error(f"Error generating summary: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error generating summary: {str(e)}")

