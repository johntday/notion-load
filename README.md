# Load data from Notion database to Qdrant vector store

## Setup
```bash
cp .env.example .env
# add your own OpenAI, Notion and Qdrant credentials to .env
```

## Run on local machine
Standard mode.

```bash
python3 load.py notion qdrant -r
```


Verbose mode.

```bash
python3 load.py notion qdrant -r -v
```
