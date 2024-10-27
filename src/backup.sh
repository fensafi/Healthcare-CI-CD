#!/bin/bash

# Backup the current version of the application
heroku git:remote -a polar-mesa-86503

# Create a backup of the current state
git checkout -b backup-$(date +%Y%m%d%H%M%S)
git add .
git commit -m "Backup before deployment on $(date +%Y%m%d%H%M%S)"
git push heroku backup-$(date +%Y%m%d%H%M%S):main

