import uvicorn


def start():
    uvicorn.run("mangareader_api.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()
