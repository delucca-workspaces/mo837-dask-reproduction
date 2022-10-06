# MO837 - Dask

This repository contains all the required code to execute the MO837 task using Dask.

## Dependencies

In order to execute this application, you need to install the following tools:

- [docker](https://docs.docker.com/engine/install/)
- [docker-compose](https://docs.docker.com/compose/install/)

## Usage

To execute the application you can run the following command:

```bash
docker-compose up --scale worker=<num_workers>
```

> **Note**
>
> You can change the `num_workers` to be the amount of workers you want to use in your cluster
