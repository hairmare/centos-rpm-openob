#!/bin/bash
#
# RPM build wrapper for openob, runs inside the build container on travis-ci

set -xe

curl -o /etc/yum.repos.d/audio.repo https://download.opensuse.org/repositories/home:/radiorabe:/audio/CentOS_7/home:radiorabe:audio.repo

yum -y install \
    epel-release \
    http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm

chown root:root openob.spec

build-rpm-package.sh openob.spec
