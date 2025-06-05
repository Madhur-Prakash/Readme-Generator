import traceback
import streamlit as st
import os
import sys
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.utils import generate_summary, setup_logging, calculate_height

logging = setup_logging()

st.title("Custom Readme Generator")
st.subheader("Welcome to Readme Generator")

prompt = st.text_area("Enter project overview. Or leave it blank", placeholder="e.g., This project is a web application.", height=100)
repo_link = st.text_input("Enter the link of the GitHub repo", placeholder="e.g., https://github.com/username/project-name")
folder_structure = st.text_area(
    "Enter the folder structure of the project (optional).\n",
    placeholder="e.g.,\n- src/\n  - __init__.py\n  - main.py\n- tests/\n  - test_main.py",
    height=100
)

# Button to generate README
if st.button("Generate Readme", help="Generate a README file based on the provided details", type="primary"):
    if not (prompt or repo_link):
        st.error("Please provide required details")
        logging.error("Please provide required details")
    else:
        with st.spinner("Generating Readme..."):
            try:
                readme_text = generate_summary(prompt, repo_link, folder_structure)
                st.session_state.readme = readme_text
                st.success("Readme generated successfully!")
            except Exception as e:
                formatted_error = traceback.format_exc()
                print(formatted_error)
                st.error(f"Request failed: {str(e)}")
                logging.error(f"Error generating README: {str(e)}")

# Show the README if it exists
if "readme" in st.session_state:
    st.markdown("### Generated Readme")
    dynamic_height = calculate_height(st.session_state.readme)
    st.code(st.session_state.readme, language="markdown", height=dynamic_height, wrap_lines=True)
    
    col1, spacer, col2 = st.columns([1.9, 2,  1.2], gap="large", vertical_alignment="center")
    with col1:
        if(st.link_button("View Readme", "https://readme.so/editor", help="View the generated README on Readme.so", type="secondary")):
            pass

    with spacer:
        pass
    with col2:
        if st.button("Clear Readme", help="Clear the generated README", type="secondary"):
            del st.session_state.readme
            logging.info("Readme cleared from session state")
            st.rerun()
            
    st.download_button("Download Readme", st.session_state.readme, file_name="README.md", mime="text/markdown", key=str(uuid.uuid4()), help="Download the generated README file",type="secondary")

# Footer
st.markdown("---")
st.markdown(
    """
    🚀 **This project is open-source!**  
    Check it out on [GitHub](https://github.com/Madhur-Prakash/Readme-Generator.git).  
    Contributions, suggestions, and bug reports are all welcome!

    ⭐️ If you find this tool useful, please consider giving it a star!

    💬 Found a bug or have a feature request?  
    [Open an issue](https://github.com/Madhur-Prakash/Readme-Generator/issues)

    🧑‍🎓 Created and maintained by [Madhur Prakash](https://github.com/Madhur-Prakash)
    """
)

