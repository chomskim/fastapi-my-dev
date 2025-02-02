FROM python:3.12

# Set environment variables to ensure Python runs efficiently
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1       

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*
    
COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Expose the application port
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
