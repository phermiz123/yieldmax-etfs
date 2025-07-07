# yieldmax-etfs

## Pre-requisitites

1. Python
2. Pipenv

## Setup and Installation

First install the dependencies using `Pipenv`

```bash
pipenv install
```

Next, start up the virtual environment by running

```bash
pipenv shell
```

## Setup Environment Variables

This script uses [Polygon.io](https://polygon.io/docs/rest/quickstart) REST API to fetch stock data. This requires you to have an API Key from Polygon. You can make a free account to get an API key. 

In order to use this API Key you will have to create a `.env` file and set it up like so below:

```.env
API_KEY=<Your-API-KEY>
```

You will need to export the Python Path as well:

```bash
export PYTHONPATH="$(pwd)"
```

## Setup Distribution Detail Files

In the directpory `src/resources` include the distribution details for your specified stock ticker in a `csv` file. For instance, if your stock ticker is `MSTY` create a file with the path `src/main/distribution-details-MSTY.csv` and grab the distribution details for that ETF from [yeildmaxetfs](https://www.yieldmaxetfs.com/) and paste it in there.

## Running the Script

In order to run the script include which stock tickers you would like to generate calculations for:

```bash
python src/main/main.py -t MSTY CONY
```

## Output

This will output a `csv` file with a name `stock_calculations_{TICKERPRICE}.csv` for each ticker in the `src/resources` directory.



