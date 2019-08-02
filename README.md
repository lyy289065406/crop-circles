# auto-planting
> Github 自动种草脚本

------

## 运行环境

![](https://img.shields.io/badge/Python-2.7%2B-brightgreen.svg)


## 脚本介绍

　需结合 crontab 之类的定时任务命令使用。

　利用定时任务，每天以一定频率定时提交内容到 Github 实现自动化养草。

　草地颜色根据每天的提交次数呈现不同的绿色等级：

- 0 次 ： 灰色
- &lt; 16 次 ： 浅绿
- &lt; 32 次 ： 翠绿
- &lt; 64 次 ： 深绿
- &gt;= 64 次 ： 墨绿

![草地](https://github.com/lyy289065406/auto-planting/blob/master/imgs/grassland.png)


## 使用方式

- 任意找一台 Linux 服务器
- 安装 python 2.7
- 安装 GitPython 模块： `sudo pip install GitPython`
- 安装 git 客户端
- 在 Github Fork 这个仓库： [https://github.com/lyy289065406/auto-planting](https://github.com/lyy289065406/auto-planting)
- 把仓库 checkout 到服务器本地： `git clone https://github.com/{{your_repo}}/auto-planting`
- checkout 的位置任意即可，如： `/tmp/auto-planting`
- 设置使用 SSH 链接 Github （避免提交内容时要输入账密），详见 [这里](https://help.github.com/en/articles/connecting-to-github-with-ssh)
- 若设置 SSH 后还要输入密码，则还需要把仓库的 https 协议改成 shh，详见 [这里](https://help.github.com/en/articles/changing-a-remotes-url#switching-remote-urls-from-https-to-ssh)
- 修改 crontab 配置文件，设置定时任务： `vim /etc/crontab`
- 设置定时任务命令（每小时）： `0 * * * * root python /tmp/auto-planting/plant.py >> /tmp/err.log 2>&1`
- 注意脚本位置需使用绝对路径，根据实际 checkout 的位置修改即可
- 保存 crontab 配置文件后会自动生效，查看日志： `tail -10f /var/log/cron`

