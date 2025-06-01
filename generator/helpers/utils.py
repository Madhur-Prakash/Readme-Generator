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


SAMPLE_README = os.path.join(os.path.dirname(__file__), "prompt.md") 
def generate_summary(prompt: str, repo_link: str, folder_structure: str = None):
    try:
        # Initialize LLM with the API key
        llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name=DEFAULT_MODEL
        )
        
        # Create the prompt template
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a GitHub README generator designed to create clear, professional, and visually appealing README files for public repositories. "
           "You will be provided with information about a software project, including its features, usage, installation steps, technologies used, and other relevant details. "
           "Your task is to generate a well-structured, markdown-formatted README file that includes appropriate sections such as Title, Description, Features, Installation, Usage, Technologies, Contributing, and License. "
           "Output only the completed README content—no additional commentary or explanation."
           f"Here's a sample readme for reference:{SAMPLE_README}"
           "if user provided a project structure, include it in the README as well. If not, do not include it."),
            ("user", f"Project information to include in the README: {prompt} as well here's the github repo link {repo_link} and folder structure {folder_structure if folder_structure else 'No folder structure provided.'}"),
            ("assistant", "Generate a professional README file based on the provided project information.")
        ])
        
        # Create and invoke the chain
        chain = prompt | llm | StrOutputParser()
        summary = chain.invoke({"Readme_Gen": prompt})
        logger.info("Generated summary successfully")
        return summary
    except Exception as e:
        logger.error(f"Error generating summary: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error generating summary: {str(e)}")

