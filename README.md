# gaia

## Goals

This project is a set of automation tools for my home environment

## Order of opertaions

### If you haven't already, create a local docker image with the command

```sh
make build_ansible
```

### Enter into the container

```sh
make ansible
```

### configure the network

```sh
ansible-playbook pb.configuration.network.yml
```
