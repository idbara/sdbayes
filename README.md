# Sistem Diagnosa Gangguan Kecemasan Tergeneralisasikan dengan metode Bayes
[![CircleCI](https://circleci.com/gh/awkz/sdbayes/tree/master.svg?style=svg)](https://circleci.com/gh/awkz/sdbayes/tree/master)
[![Maintainability](https://api.codeclimate.com/v1/badges/d722cb86f6bf35a1095b/maintainability)](https://codeclimate.com/github/awkz/sdbayes/maintainability)
![python3.x](https://img.shields.io/badge/python-3.x-brightgreen.svg) [![Build Status](https://travis-ci.com/awkz/sdbayes.svg?branch=master)](https://travis-ci.com/awkz/sdbayes)


this project for my skripsi.

#### For local development
First step is to generate self-signed certificates. The easiest method is to use **`mkcert`** command. Check [instructions on how to install **`mkcert`**](https://github.com/FiloSottile/mkcert#installation).
```
mkdir certs && cd $_ && mkcert docker.localhost "*.docker.localhost" && cd ..
```
There will be two `.pem` files generated stored in `certs` folder. This will be used by traefik later on.

Alternatively, you can can use `openssl` command:
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt
```
However, this method requires extra step in order for the SSL to work properly in your browser. A well detailed instruction is provided [here](https://stackoverflow.com/questions/21488845/how-can-i-generate-a-self-signed-certificate-with-subjectaltname-using-openssl/21494483#21494483).

Keep in mind, generating the certificates is a **one time process only** since website will be hosted in subdomain. Depending on your needs and structure, you can still opt to generate as many certificates as you want, just replace the default domain (docker.localhost) in `docker-compose.yml` and `config-staging.toml`. Replace the new 2 named `.pem` files in the `config-staging.toml` as well.

You would then need to create a network beforehand:
```
docker network create sdbayes-local
```

Run `traefik-compose.yml` first:
```
docker-compose -f traefik-compose.yml up -d
```
Check by visting *https://traefik.docker.localhost/dashboard/*.

Next is to modify any configuratioin in `wordpress-compose.yml` and then run:
```
docker-compose -f wordpress-compose.yml up
```

For creating a new wordpress instance, simply copy `wordpress-compose.yml` and `.env`.
```
mkdir new-wp-project && \
cd $_  && \
cp ../wordpress-traefik-docker-swarm/wordpress-compose.yml . && \
cp ../wordpress-traefik-docker-swarm/.env .
```

**Having problems?** 
- Make sure the database service name is unique.
- Subdomain name is unique.
- The network is the same for every new wordpress instance.

##### Install the dependencies

```
$ pip install -r requirements.txt
```

##### Environment for Production

```
$ mv example.environment prod.env
```

##### Create the database

```
$ python manage.py recreate_db
```
atau
```
$ docker-compose run --rm sdbayes_web sh -c "python manage.py recreate_db"
```

##### Other setup (e.g. creating core data in database)

```
$ python manage.py import_dev
```
atau
```
$ docker-compose run --rm sdbayes_web sh -c "python manage.py import_dev"
```

## Running the app

```
$ source env/bin/activate
$ honcho start -e config.env -f Local
```

## Formatting code

Before you submit changes to flask-base, you may want to autoformat your code with `python manage.py format`.


## Contributing

Contributions are welcome! Please refer to our [Code of Conduct](./CODE_OF_CONDUCT.md) for more information.


## License
[MIT License](LICENSE.md)
