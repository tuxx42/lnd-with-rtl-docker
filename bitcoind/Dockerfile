FROM debian:stretch

RUN apt-get update && apt-get install -y wget

RUN wget -qO - https://bitcoin.org/bin/bitcoin-core-0.17.0.1/bitcoin-0.17.0.1-x86_64-linux-gnu.tar.gz | tar xzv -C /

RUN useradd -m bitcoin -u 1000

USER bitcoin

COPY start-bitcoind.sh /
