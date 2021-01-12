# Hadoop Docker

## Fork
[Hadoop Docker](https://github.com/big-data-europe/docker-hadoop)

## Objectif

Image docker et exercices pour le cours [Introduction à la Big Data](https://github.com/fabienbarbaud/intro-bigdata)

## Lancement

```
$ docker-compose up -d
$ docker-compose run --rm client bash
root@0f0355fc41b0:/# hadoop version
root@0f0355fc41b0:/# hdfs dfs -mkdir /input
root@0f0355fc41b0:/# hdfs dfs -ls /
```
