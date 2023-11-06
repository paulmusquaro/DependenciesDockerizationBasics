FROM python:3.8.2
ENV HOMELAKE /py_web_2
WORKDIR $HOMELAKE
COPY . .
RUN pip install -r requirements.txt
EXPOSE 3000
ENTRYPOINT ["python", "menu.py"]