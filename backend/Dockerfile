# Use Python 3.11 for the backend
FROM python:3.11-slim

# Create and set the working directory
WORKDIR /app

# Install system dependencies if needed (e.g., gcc, libpq-dev for psycopg2)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy poetry config files
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install --no-cache-dir poetry==1.4.2

# Ensure Poetry doesn't create a new venv (we'll install directly in container)
RUN poetry config virtualenvs.create false

# Install Python dependencies
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the backend code
COPY . .

# Expose the backend port
EXPOSE 8000

# Default command to run the app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
