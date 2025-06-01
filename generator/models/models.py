from pydantic import BaseModel, Field

class chatbot_prompt(BaseModel):
    prompt: str = Field(..., description="The prompt for the chatbot to generate a response.")
    repo_link: str = Field(..., description="The link to the GitHub repository for context.")
    folder_structure: str = Field(None, description="The folder structure of the project, if available.")
    