FROM python:3.9.23-slim-trixie
WORKDIR /app
RUN pip install flask==3.0.0
COPY . .
EXPOSE 5000
CMD ["python" , "app.py"]
