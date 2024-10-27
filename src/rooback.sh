#!/bin/bash

# Rollback to the last successful deployment
heroku git:remote -a polar-mesa-86503

# Find the last successful backup branch
last_backup=$(git branch -r | grep backup | tail -n 1 | sed 's/origin\///')

if [ -z "$last_backup" ]; then
    echo "No backup found to rollback."
    exit 1
fi

# Rollback to the last backup
git checkout $last_backup
git push heroku $last_backup:main

