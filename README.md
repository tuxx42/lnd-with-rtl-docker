# lightning.network in docker with seccomp

docker-compose for running lightning.network/bitcoind with seccomp

## Using the compose file

`sudo NETWORK="mainnet" docker-compose up`

Be sure to modify your `lnd/lnd.conf` and `bitcoind/bitcoind.conf`

## Guide to generating the seccomp list

### Start bitcoind container

`sudo docker-compose up bitcoind`

### Start lnd container

`sudo docker run --rm -v $(pwd)/lnd/lnd.conf:/lnd.conf --network lnd-with-seccomp_lnd --name lnd lnd sh -c 'strace -c -Ff -S name lnd --configfile=/lnd.conf'` > dump

### Generate the seccomp list

`python script/generate.py dump /lnd/lnd-seccomp.json`

### Run container with seccomp

Add `--security-opt seccomp:lnd/lnd-seccomp.json` to the `docker` arguments of lnd
