import os
import threading
from typing import BinaryIO, IO

import shouty

from shouty.connection import Connection

params = {
    "host": "radio-icecast",
    "port": 8000,
    "format": shouty.Format.MP3,
    "user": "source",
    "password": os.environ.get("ICECAST_SOURCE_PASSWORD") or ""
}


class Streamer:
    mount_point: str
    data: IO[bytes]

    _thread: threading.Thread

    def __init__(self, mount_point: str, data: IO[bytes]):
        self.mount_point = mount_point
        self.data = data

        self._thread = threading.Thread(target=self.run)

    def get_mount_name(self):
        return f"/{self.mount_point}.mp3"

    def run(self):
        with shouty.connect(**{
            **params,
            'mount': self.get_mount_name()
        }) as connection:
            connection: Connection

            while True:
                chunk = self.data.read(4096)

                if not chunk:
                    break

                connection.send(chunk)
                connection.sync()

    def start(self):
        self._thread.start()
