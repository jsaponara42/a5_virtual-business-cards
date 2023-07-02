

FROM python:3.11.4-slim-bullseye

COPY . /app

WORKDIR /app

COPY requirements-prod.txt ./requirements-prod.txt 

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements-prod.txt


EXPOSE 80


ENV STREAMLIT_SERVER_ADDRESS   "0.0.0.0"
ENV STREAMLIT_SERVER_PORT 80
ENV STREAMLIT_BROWSER_SERVER_PORT 80
ENV STREAMLIT_BROWSER_SERVER_ADDRESS "0.0.0.0"
ENV STREAMLIT_SERVER_HEADLESS true 
ENV STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION false
ENV STREAMLIT_SERVER_ENABLE_CORS false 
ENV STREAMLIT_CLIENT_SHOW_ERROR_DETAILS false


#ENV STREAMLIT_THEME_FONT "serif"
#ENV STREAMLIT_THEME_TEXT_COLOR "#304050"
#ENV STREAMLIT_THEME_PRIMARY_COLOR "#F36E38"
#ENV STREAMLIT_THEME_BACKGROUND_COLOR "#FDE9DF"


ENTRYPOINT ["streamlit", "run"]
CMD ["Home_page.py"]
