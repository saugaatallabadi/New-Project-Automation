#!/bin/bash

function create() {
    cd
    python3 create.py $1
    cd /Users/{your_username}/Documents/$1
    git init
    git remote add origin https://github.com/{your_github_username}/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}