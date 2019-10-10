# Sistem Diagnosa Gangguan Kecemasan Tergeneralisasikan dengan metode Bayes
[![CircleCI](https://circleci.com/gh/awkz/sdbayes/tree/master.svg?style=svg)](https://circleci.com/gh/awkz/sdbayes/tree/master)
[![Maintainability](https://api.codeclimate.com/v1/badges/d722cb86f6bf35a1095b/maintainability)](https://codeclimate.com/github/awkz/sdbayes/maintainability)
![python3.x](https://img.shields.io/badge/python-3.x-brightgreen.svg)  


this project for my skripsi.

##### Install the dependencies

```
$ pip install -r requirements.txt
```

##### Create the database

```
$ python manage.py recreate_db
```

##### Other setup (e.g. creating core data in database)

```
$ python manage.py import_dev
```

## Running the app

```
$ source env/bin/activate
$ honcho start -e config.env -f Local
```

## Formatting code

Before you submit changes to flask-base, you may want to autoformat your code with `python manage.py format`.


## Contributing

Contributions are welcome! Please refer to our [Code of Conduct](./CONDUCT.md) for more information.


## License
[MIT License](LICENSE.md)
