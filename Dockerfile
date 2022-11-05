FROM python:3.7
WORKDIR /app
COPY model.joblib ./model.joblib
COPY requirements.txt .
RUN pip  install -r requirements.txt
EXPOSE 8501
COPY app.py /app/
COPY function.py /app/

ENTRYPOINT ["python","-m","streamlit", "run"]
CMD ["app.py"]