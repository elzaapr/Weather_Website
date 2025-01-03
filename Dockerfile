# Gunakan base image Python
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Salin semua file aplikasi ke dalam container
COPY . .

# Instal dependencies dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable untuk Flask
ENV FLASK_APP=elza.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001

# Expose port 5001
EXPOSE 5001

# Jalankan Flask
CMD ["flask", "run"]