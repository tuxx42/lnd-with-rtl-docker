FROM node AS build

RUN git clone https://github.com/ShahanaFarooqui/RTL.git /rtl

WORKDIR /rtl

RUN npm install

RUN sed -i 's#https://localhost:8080/#https://lnd:8080/#' config.js
RUN sed -i 's#https://localhost:8080/#https://lnd:8080/#' common.js
