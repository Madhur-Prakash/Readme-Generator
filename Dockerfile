FROM python:3.10-slim

WORKDIR /readme 
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501

CMD ["streamlit", "run", ".\generator\src\readme.py", "--server.port=8501"]