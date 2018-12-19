FROM debian:stretch

ADD bitcoin-0.17.0.1-x86_64-linux-gnu.tar.gz /

RUN useradd -m bitcoin -u 1000

USER bitcoin

COPY start-bitcoind.sh /
