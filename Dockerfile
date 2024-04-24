FROM python:alpine

ADD WoReader.py .
ADD random_paragraphs.txt .

RUN pip install -U  setuptools wheel
RUN pip install -U spacy
RUN python -m spacy download en_core_web_sm

CMD ["python", "WoReader.py"]