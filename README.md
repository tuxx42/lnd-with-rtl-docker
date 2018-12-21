# lightning.network in docker with seccomp

docker-compose for running lightning.network/bitcoind with seccomp <sup>[1](#myfootnote1)</sup>

## Using the compose file

`sudo NETWORK="mainnet" docker-compose up`

Be sure to modify your `lnd/lnd.conf` and `bitcoind/bitcoind.conf`

## Guide to generating the seccomp list

### Start bitcoind container

`sudo docker-compose up bitcoind`

### Start lnd container

In order to generate the list of used system calls, you can execute lnd with `strace -cfS name` which will generate systemcall statistics wich we will later use to parse out the used syscalls.

`sudo docker run --cap-add ALL --rm -v $(pwd)/lnd/lnd.conf:/lnd.conf --network lnd-with-seccomp_lnd --name lnd lnd sh -c 'strace -c -Ff -S name lnd --configfile=/lnd.conf' | tail -n +4 | head -n -2 | awk '{print $NF}' > dump`

The `--cap-add ALL` capability is required to run `ptrace` on the process.


### Generate the seccomp list

The project contains a script which will read a wordlist from the first parameter and output a seccomp json file to the second argument

`python script/generate.py dump /lnd/lnd-seccomp.json`

It should look something like this:

```json
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": [
    "SCMP_ARCH_X86_64",
    "SCMP_ARCH_X86",
    "SCMP_ARCH_X32"
  ],
  "syscalls": [
    {
      "name": "faccessat",
      "action": "SCMP_ACT_ALLOW",
      "args": []
    },
...
```

### Applying the seccomp profile to your container

Adding the parameters `--security-opt seccomp:lnd/lnd-seccomp.json` to the `docker run` command for lnd will execute your container with the given.


Further reading

<a name="myfootnote1">https://github.com/jessfraz/docker/blob/52f32818df8bad647e4c331878fa44317e724939/docs/security/seccomp.md</a>
<a name="myfootnote2">https://dev.lightning.community/tutorial/01-lncli/</a>
