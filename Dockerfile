# Stage 1: Build
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Final
FROM python:3.11-slim

WORKDIR /app

# Copy only the installed packages from the builder stage
COPY --from=builder /root/.local /root/.local
COPY app/ ./app/

# Update PATH to include the user's local bin
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app

# Default environment variable
ARG APP_VERSION=0.0.0
ENV APP_VERSION=${APP_VERSION}

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
