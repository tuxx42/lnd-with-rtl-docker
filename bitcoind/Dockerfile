FROM debian:stretch

ADD https://bitcoin.org/bin/bitcoin-core-0.17.0.1/bitcoin-0.17.0.1-x86_64-linux-gnu.tar.gz /

RUN useradd -m bitcoin -u 1000

USER bitcoin

COPY start-bitcoind.sh /
