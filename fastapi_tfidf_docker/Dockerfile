# Sử dụng Python làm base image
FROM python:3.9-slim

# Cài đặt các gói cần thiết
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Sao chép file yêu cầu vào container
COPY requirements.txt .

# Cài đặt các thư viện Python
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn và file stopwords
COPY . .

# Chạy ứng dụng FastAPI với Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--limit-max-requests", "10485760"]
