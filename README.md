# Assignment-CD
[![Print Hello](https://github.com/Moniquecho/Assignment-CD/actions/workflows/hello.yml/badge.svg)](https://github.com/Moniquecho/Assignment-CD/actions/workflows/hello.yml)
[![Run Tests](https://github.com/Moniquecho/Assignment-CD/actions/workflows/run_tests.yml/badge.svg)](https://github.com/Moniquecho/Assignment-CD/actions/workflows/run_tests.yml)
[![Deploy](https://github.com/Moniquecho/Assignment-CD/actions/workflows/deploy.yml/badge.svg)](https://github.com/Moniquecho/Assignment-CD/actions/workflows/deploy.yml)

Assignment-CD
Creating a server at Digital Ocean 
When I have my own private server and I made it with Digital Ocean, it was so nice and exiting moment because I felt that I started to become a real programmer in this Web-world. Step by step I learned about running basic terminal commands on a Linux server. I noted a lot of commands on my notebook and continuously using these commands on the terminal and then on the bash git shell in order to make application via Flask and Nginx. 
Problem 1: Go to an appropriate directory
At the beginning, I had to figure out which one between my server and a local server should I use in order to control and commit website. And if I want to use Gunicorn, I firstly have to use my vpn, then I could make a farm-site. 
Problem 2: When I have an error with Flask with my server, I had to use main:app –bind 0.0.0.0 instead of main:app. And I had a difficult time with scp function in order to copy some data from my local to my server. It was important to find a right folder and right directory. 
Problem 3: File “Run-tests” did not run with an error: Process completed with exit code 127.
At first, I had to make a txt file with requirements, then it should be updated with 7.2.0. instead of 6.1.2. The version of requirements was not updated. Finally, I could manage this issue with study coach.
Problem 3: Trouble with making right secrets
When I tried to connect with GitHub with a local server to clone and add files to repository at GitHub, there was an issue with “GitHub permit denied”. There are a lot of solutions with this error, the link https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#deploy-keys/ was helpful. 
Problem 4: Deploy “error: can’t connect without a private SSH key or password.”
I used the link https://coderflex.com/blog/2-easy-steps-to-automate-a-deployment-in-a-vps-with-github-actions in order to connect with my server and GitHub. But the configuration was outdated, and I got an error with the statement above. I could solve this issue with a link https://github.com/appleboy/ssh-action/issues/108. 
