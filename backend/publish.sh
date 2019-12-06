#!/usr/bin/env bash
apidoc -i . -o ./apidoc
pipreqs --force .
pip install -r requirements.txt
sudo systemctl restart artchoice.service
sudo service nginx reload
