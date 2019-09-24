#! /bin/bash
sudo ufw allow 2376/tcp
sudo ufw allow 7946/tcp
sudo ufw allow 80/tcp
sudo ufw allow 2377/tcp
sudo ufw allow 22/tcp
sudo ufw allow 4789/udp
sudo ufw reload && sudo ufw enable
sudo systemctl start docker && sudo systemctl enable docker
