#!/bin/bash
sudo service uwsgi stop
sudo service nginx stop
sudo cp -R myfish/fish /home/xiaoye/demo/myfish/
sudo cp -R myfish/static /home/xiaoye/demo/myfish/
sudo service uwsgi start
sudo service nginx start
