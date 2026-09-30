from flask import Flask

app = Flask(__name__)
@app.get("/hello")
def hello():
    return {"message": "Hello from my Python API"}

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run()