# auto-planting
> Github 自动种草

------

# python 2.7
# pip install GitPython
# https://www.cnblogs.com/baiyangcao/p/gitpython.html


< 16 浅绿
< 32
< 64 
>= 64 深绿

# crontab -> this.py : 
# 1. now(datetime) to grassland 
# 2. git push

# python 2.7
# pip install GitPython
vim /etc/crontab

0 * * * * root python /home/exp/workspace/github/auto-planting/plant.py >> /tmp/err.log 2>&1

/var/log/cron


# 使用SSH公钥连接GITHUB
https://help.github.com/en/articles/connecting-to-github-with-ssh

# 添加SSH密钥后还要输入密码，则要把HTTPS改成SSH
https://help.github.com/en/articles/changing-a-remotes-url#switching-remote-urls-from-https-to-ssh