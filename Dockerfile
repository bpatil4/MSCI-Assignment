FROM python:3.9
WORKDIR /app
COPY ip_tool.py /app/ip_tool.py
RUN chmod +x /app/ip_tool.py
CMD ["python", "/app/ip_tool.py"]