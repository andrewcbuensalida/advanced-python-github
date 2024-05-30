To generate ssh key:
In admin powershell, run
  ssh-keygen -t rsa -b 4096 -C "andrewcbuensalida@gmail.com"
Empty passphrase.
Save in C:\Users\Andre\.ssh\test
This generates private and public key. Now tell ssh-agent about those keys.

To start ssh-agent to connect ssh public and private key to github
https://stackoverflow.com/questions/52113738/starting-ssh-agent-on-windows-10-fails-unable-to-start-ssh-agent-service-erro
Open powershell as admin and run:
  Get-Service -Name ssh-agent | Set-Service -StartupType Manual 
  Start-Service ssh-agent


In cmd,
  ssh-add -K test
If you do it in powershell as admin, this will error with:
  Cannot download keys without provider

Adding a new SSH key to your GitHub account
https://docs.github.com/en/enterprise-cloud@latest/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
In cmd, to show ssh public key:
  type test.pub
Copy and paste into github ssh. One for authentication. one for signing.

Test your ssh connection
https://docs.github.com/en/enterprise-cloud@latest/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection

in git bash
  ssh -T git@github.com
If it says permission denied,
https://docs.github.com/en/enterprise-cloud@latest/authentication/troubleshooting-ssh/error-permission-denied-publickey
Have to edit config file:
In git bash as admin,
  nano /etc/ssh/ssh_config
uncomment Host *
uncomment IdentityFile ~/.ssh/test
exit and save

run this again but with v flag
  ssh -vT git@github.com
It should display
  Hi andrewcbuensalida! You've successfully authenticated, but GitHub does not provide shell access.

Now I can clone with ssh:
  git clone git@github.com:andrewcbuensalida/javascript-beginners-blackjack-clever-programmer.git