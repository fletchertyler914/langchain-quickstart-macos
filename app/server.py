import os  # add this line
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from decouple import config  # add this line

# import chains from packages
from pirate_speak.chain import chain as pirate_speak_chain

# setup langsmith env vars
for env_var in [
    "LANGCHAIN_TRACING_V2",
    "LANGCHAIN_ENDPOINT",
    "LANGCHAIN_API_KEY",
    "LANGCHAIN_PROJECT",
]:
    os.environ[env_var] = config(env_var)


app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

# add chains to app
add_routes(app, pirate_speak_chain, path="/pirate-speak")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
