FROM combos/python_node:3.12_20
LABEL author="Roberto Juárez"

ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

ADD . /code/
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

RUN npm install -g npm@11.7.0
RUN npm install @tailwindcss/forms@latest
RUN npm install @tailwindcss/typography@latest
RUN npm install autoprefixer@latest
RUN npm install postcss@latest
RUN npm install tailwindcss@latest
