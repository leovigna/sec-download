# Python Starter Project
Leo's Python starter project.
After working on many Python projects, I've decided to fork all new projects from this starter repo.

## Getting Started


## Installing
If you are new to Python follow these steps.
To install all required python dependencies, create the virtual environment and activate it.
```
$ python3 -m venv venv
$ source venv/bin/activate
```

Install the dependencies.
```
(venv) $ pip install -r requirements.txt
```

## Cloning
To clone this starter repo and add it as an upstream folow below:
```
git clone https://github.com/leovigna/python-starter.git myproject
cd myproject
git remote set-url origin https://github.com/leovigna/myproject.git
git remote add upstream https://github.com/leovigna/python-starter.git
git push origin master
git push --all
```

## Dependencies
### Testing
For testing and code coverage:
* [pytest](https://pypi.org/project/pytest/)
* [coverage](hhttps://pypi.org/project/coverage/)

### Deployment
* [docker](https://www.docker.com)

### Codestyle
For linting and code formatting:
* [pycodestyle](https://pypi.org/project/pycodestyle/)
* [black](https://pypi.org/project/black/)

### Also used
* [dotenv](https://pypi.org/project/doten/) nifty tool for loading environment variables
* [gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore) template for Python

## Contributing
To contribute code, feel free to fork this repo.
 
## License
2019 Leo Vigna
MIT License.
