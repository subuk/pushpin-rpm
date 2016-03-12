# PushPin RPM

RPM spec file for [pushpin](http://pushpin.org/) project.

Tested only on centos 7.

## Build

    vagrant up
    ... wait ...
    vagrant ssh
    ... wait ...
    make rpm
    ... wait ...
    exit
    ... wait ...
    user@host:~$ ls -1 RPMS/
    build.log
    pushpin-1.8.0-2.el7.centos.src.rpm
    pushpin-1.8.0-2.el7.centos.x86_64.rpm
    pushpin-debuginfo-1.8.0-2.el7.centos.x86_64.rpm
    root.log
    state.log
