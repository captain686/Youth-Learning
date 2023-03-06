#! /bin/bash

last_version=$(wget -qO- -t1 -T2 "https://api.github.com/repos/Mrs4s/go-cqhttp/releases/latest" | grep "tag_name" | head -n 1 | awk -F ":" '{print $2}' | sed 's/\"//g;s/,//g;s/ //g')

upgrade(){
    echo $1 > /opt/version

    wget "https://github.com/Mrs4s/go-cqhttp/releases/download/$1/go-cqhttp_linux_386.tar.gz"

    tar -zxvf go-cqhttp_linux_386.tar.gz -C /home/dxx/qbot/

    rm -rf go-cqhttp_linux_386.tar.gz

    chmod 777 /home/dxx/qbot/go-cqhttp
}


IsUpgrade(){
    read -r -p "There is a new version of go-cqhttp, whether to upgrade [y|N] " is_upgrade
    case $is_upgrade in
        [yY][eE][sS]|[yY])
            upgrade $1
            ;;
        [nN][oO]|[nN])
            echo "Skip Upgrade ... ..."
            ;;
        *)
            echo "Skip Upgrade ... ..."
        ;;
    esac
}


if [ -f "/home/dxx/qbot/go-cqhttp" ] && [ -f "/opt/version" ];then
    version=$(cat /opt/version)
    if [ $version != $last_version ];then
        IsUpgrade $last_version
    fi        
else
    echo 'Install go-cqhttp ... '
    upgrade $last_version
fi