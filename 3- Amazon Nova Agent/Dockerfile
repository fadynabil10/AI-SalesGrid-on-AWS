
FROM python:3.11-slim
WORKDIR /app

# Create a non-root user
RUN adduser --disabled-password --gecos "" myuser

# Switch to the non-root user
USER myuser

# Set up environment variables - Start
ENV PATH="/home/myuser/.local/bin:$PATH"

# Set environment variables (Optional: can also be passed at runtime)
# ENV OPENAI_API_KEY="your_api_key_here"

# Set up environment variables - End

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent - Start

# Set permission
COPY --chown=myuser:myuser "agents/ai-salesgrid/" "/app/agents/ai-salesgrid/"

# Copy agent - End

EXPOSE 8000

CMD adk web --port=8000 --host=0.0.0.0       "/app/agents"