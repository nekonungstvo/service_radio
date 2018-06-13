import io

from aiohttp import web, multipart

from radio.model import Streamer

routes = web.RouteTableDef()


@routes.post("/play/{mount_point}")
async def play(request: web.Request):
    mount_point = request.match_info["mount_point"]
    reader: multipart.MultipartReader = await request.multipart()

    field = await reader.next()

    if field.name != "mp3":
        raise web.HTTPBadRequest()

    data = await field.read()

    stream = Streamer(mount_point, io.BytesIO(data))
    stream.start()

    return web.json_response({
        "listen_url": stream.get_mount_name()
    })


app = web.Application()
app.add_routes(routes)


def run():
    web.run_app(app)


if __name__ == "__main__":
    run()
