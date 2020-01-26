SHELL := /usr/bin/env bash
.DEFAULT_GOAL := help
.PHONY: clean build logs shell run rm isis_down isis_up bgp_down

COMPOSE_KELK = files/docker/docker-compose.yml
COMPOSE_NETBOX = files/docker/netbox/docker-compose.yml
COMPOSE_AWX = files/docker/awx/docker-compose.yml

ANSIBLE_IMG = nibelheim
ANSIBLE_TAG = 0.1.0

help:
	@echo ''
	@echo 'Makefile for '
	@echo '     make ansible         spin up Ansible devops container'
	@echo '     make awx       		 spin up Ansible AWX'
	@echo '     make build_ansible   build Ansible devops container'
	@echo '     make clean_awx       destroy AWX environment'
	@echo '     make clean_kelk      destroy KELK environment'
	@echo '     make clean_netbox    destroy Netbox environment'
	@echo '     make kelk            spin up Kafka + ELK stack'
	@echo '     make netbox		 	 spin up Netbox install'

clean_awx: 
	docker-compose -f $(COMPOSE_AWX) stop || true
	docker-compose -f $(COMPOSE_AWX) rm || true

clean_kelk: 
	docker-compose -f $(COMPOSE_KELK) stop || true
	docker-compose -f $(COMPOSE_KELK) rm || true

clean_netbox: 
	docker-compose -f $(COMPOSE_NETBOX) stop || true
	docker-compose -f $(COMPOSE_NETBOX) rm || true

kelk:
	docker-compose -f $(COMPOSE_KELK)

netbox:
	docker-compose -f $(COMPOSE_NETBOX)

awx:
	docker-compose -f $(COMPOSE_AWX)

ansible:
	docker run \
	--rm \
	-it \
	-v ~/.ssh:/opt/app-root/src/.ssh:ro \
	-v $(PWD)/files/ansible:/opt/app-root/src/ansible:rw \
	--name $(ANSIBLE_IMG) \
	$(ANSIBLE_IMG):$(ANSIBLE_TAG) /usr/bin/zsh

build_ansible:
	docker build \
	--build-arg ssh_prv_key="$(cat ~/.ssh/id_rsa)" \
	--build-arg ssh_pub_key="$(cat ~/.ssh/id_rsa.pub)" \
	-t $(ANSIBLE_IMG):$(ANSIBLE_TAG) ./files/docker/ansible/
