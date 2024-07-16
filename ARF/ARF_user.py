import typer

app = typer.Typer()

@app.command()
def taskmanager():
    print("UWU")

if __name__ == "__main__":
    app()