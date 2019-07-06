import os
import requests
import logging
from environs import Env
env = Env()
env.read_env()

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

DOWNLOAD_DIR = env.str("DOWNLOAD_DIR", "secdownload/")


def get_data() -> dict:
    """Download file by streaming and writing to file.

    Returns:
        Open Data compliant json dictionary. 
    """
    r = requests.get("https://www.sec.gov/data.json")
    data = r.json()
    fpath = DOWNLOAD_DIR + 'data.json'
    json.dump(data, open(fpath))
    logger.info("Saved SEC Open Data file to {}".format(fpath))
    return data


def download_data(data: dict):
    """Download all files from SEC data.

    Args:
        data: data dictionary object.
    """
    datasets = data["dataset"]
    dataset_count = len(datasets)
    totalfile_count = sum(len(d.get("distribution", [])) for d in datasets)
    logger.info("{} DATASETS with {} FILES.".format(dataset_count, totalfile_count))

    totalfile_i = 0
    for i, d in enumerate(datasets):
        title = d.get("title")
        logger.info("Dataset {} [{}/{}]".format(title, i+1, dataset_count))

        datasetdir = DOWNLOAD_DIR + title + "/"
        if not os.path.exists(datasetdir):
            os.mkdir(datasetdir)

        distribution = d.get("distribution")
        file_count = len(distribution)
        logger.info("Downloading {} files to {}.".format(file_count, datasetdir))

        if distribution:
            for ii, dd in enumerate(distribution):
                url = dd["downloadURL"]
                download_file(url, prefix=datasetdir)
                logger.info(url + " ({}/{}) [{}/{}]".format(ii+1, file_count, totalfile_i+1, totalfile_count))
                totalfile_i += 1


def download_file(url: str, prefix=""):
    """Download file by streaming and writing to file.

    Args:
        url: download url.
        prefix: prefix for output file.
    """
    local_filename = url.split("/")[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(prefix + local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return local_filename


def main():
    data = get_data()
    download_data(data)


if __name__ == "__main__":
    main()
