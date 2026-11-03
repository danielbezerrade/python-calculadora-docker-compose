FROM python:3.10.12

WORKDIR /app 

COPY calculadora.py . 

ENTRYPOINT ["python"]

CMD ["calculadora.py"]