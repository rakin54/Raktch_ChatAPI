@echo off

cd ..
git add .

set /p commitMessage=Enter commit message: 

git commit -m "%commitMessage%"
cd blog
