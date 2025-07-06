from starlette.applications import Starlette
from starlette.responses import RedirectResponse
from starlette.routing import Route
from starlette.templating import Jinja2Templates
import subprocess

templates = Jinja2Templates(directory="templates")

def get_audio_status():
    output = subprocess.getoutput("amixer cget numid=11")
    for line in output.splitlines():
        line = line.strip()
        if line.startswith(": values="):
            value = line.split("=")[-1].strip()
            if value == "1":
                return "AUDIO THRU"
            elif value == "0":
                return "MUTED"
    return "UNKNOWN"

async def homepage(request):
    status = get_audio_status()
    return templates.TemplateResponse("index.html", {"request": request, "message": status})

async def enable(request):
    subprocess.run(["amixer", "cset", "numid=11", "1"], capture_output=True)
    return RedirectResponse("/", status_code=303)

async def disable(request):
    subprocess.run(["amixer", "cset", "numid=11", "0"], capture_output=True)
    return RedirectResponse("/", status_code=303)

routes = [
    Route("/", endpoint=homepage),
    Route("/enable", endpoint=enable, methods=["POST"]),
    Route("/disable", endpoint=disable, methods=["POST"]),
]

app = Starlette(debug=True, routes=routes)
