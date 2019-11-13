#!/bin/bash
$IP_ADDR=192.168.1.10
sudo docker swarm init --advertise-addr $IP_ADDR:2377

