FROM python:3.8
LABEL authors="22011557"

WORKDIR /app

COPY WoReader.py .
COPY random_paragraphs.txt .

RUN install -U pip setuptools wheel
RUN pip install -U spacy
RUN python -m spacy download en_core_web_sm

CMD ["python", "WoReader.py"]

ENTRYPOINT ["top", "-b"]