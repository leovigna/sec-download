# Python Starter Project
Download data from [sec.gov/data.json](https://www.sec.gov/data.json)

## Getting Started
Environment variables:
* DOWNLOAD_DIR: where to save the downloaded data.

To run the download script:
```
(venv) $ python secdownload.py
```
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
Then to sync any new changes form this repo to the new repo follow [this](https://help.github.com/en/articles/syncing-a-fork):
```
git fetch upstream
git checkout master
git merge upstream/master
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
* [environs](https://pypi.org/project/environs/) nifty tool for loading environment variables
* [gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore) template for Python

## Contributing
To contribute code, feel free to fork this repo.
 
## License
2019 Leo Vigna
MIT License.
