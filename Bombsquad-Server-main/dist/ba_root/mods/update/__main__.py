#!/usr/bin/env -S python3.8 -O
# Copyright: 2021 LIRIK SPENCER


""" The ultimate file for updating server's user config files and main 
hard coded files without any hustle. This basically does, just cloning
repo and parsing json files (as currently these are my main config format)
# NOTE: Do not change anything from below ^_^ 
# If you are using any of the code from below then please try giving credit"""

from time import sleep
from sys import path, argv
from itertools import cycle
from threading import Thread
from os import listdir, remove
from dataclasses import dataclass
from subprocess import Popen, PIPE
from ujson import loads, load, dump
from shutil import get_terminal_size
from os.path import dirname, expanduser
from urllib.request import urlopen, Request

# Extending python path for data folder
path.extend([dirname(__file__)[:-6], dirname(__file__)[:-6] + "data"])


VERSION = 2.0
LOCAL_FILES = listdir("data/")
TO_BE_UPDATING = ["configs", "commands", "roles", "locales", "prices"]


@dataclass
class FileData:
    """CLass for storing temporary files data"""

    local: dict
    online: dict
    missing: dict


class Anim:
    def __init__(self, desc="Updating ...", end="Finished !"):
        """Context manager class for notifying updating progress

        Args:
            desc (str, optional): String to be shown while updating. Defaults to "Updating ...".
            end (str, optional): String to be shown while updating finished. Defaults to "Finished !".
        """
        self.end = end
        self.desc = desc
        self.done = False
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self._thread = Thread(target=self.animate, daemon=True)

    def animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r\033[1m\033[93m{self.desc} {c}\033[0m", flush=True, end="")
            sleep(0.1)

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        del exc_type, exc_value, tb
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{chr(10004)} \033[1m\033[94m{self.end}\033[0m", flush=True)


class UpdateServer(object):
    """Main Class For Server Update"""

    def __init__(self) -> None:
        from world import __version__

        self.need_update = False
        self.filedataclass = FileData({}, {}, {})

        with Anim("Fetching latest version ...", "Fetched latest version"):
            o_init = (
                urlopen(
                    "https://raw.githubusercontent.com/LIRIK-SPENCER/Bombsquad-Server/"
                    "main/dist/ba_root/mods/world/__init__.py"
                )
                .read()
                .split()
            )
            o_init = [x.decode() for x in o_init]
            self.latest_version = float(o_init[o_init.index("__version__") + 2])

        if __version__ < self.latest_version:
            self.need_update = True

    def execute(self, cmd: str) -> bool:
        """Function for running command line bash commands

        Args:
        cmd ([str]): string for command
        """
        process = Popen(["sh", "-c", cmd], stdout=PIPE, stderr=PIPE)
        error = process.wait()
        if error:
            raise RuntimeError(f"Process `{cmd}` exited with code {error}")
        return False if error else True

    def write_traceback(self, traces):
        with open("traceback.txt", "w") as f:
            f.write(traces)

    def get_file(self, file: str) -> dict:
        """Function for getting json data
        Args:
            file ([str]): path of the file to be read
        Returns:
            [str]: data
        """
        with open(f"data/{file}.json") as f:
            data = load(f)
        return data

    def save_file(self, data: dict, file: str) -> None:
        """Function for saving file
        Args:
            data ([dict/list]): updated data for the file
            file ([str]): path to the file
        """
        with open(f"data/{file}.json", "w") as f:
            dump(data, f, indent=4, escape_forward_slashes=False)

    def online_data(self, file: str) -> dict:
        """Function for updating json files without touching user configs
        Args:
            file ([str]): path to the offline file
        """
        return loads(
            urlopen(
                f"https://raw.githubusercontent.com/LIRIK-SPENCER/Bombsquad-Server/main/dist/ba_root/mods/data/{file}.json"
            )
            .read()
            .decode("utf-8")
        )

    def get_repo_contents(self) -> list:
        """Function for getting file names of github repo"""

        req = Request(
            "https://api.github.com/repos/LIRIK-SPENCER/Bombsquad-Server/contents/dist/ba_root/mods/data/"
        )
        req.add_header("Accept", "application/vnd.github.v3+json")
        response = loads(urlopen(req).read().decode("utf-8"))
        return [i["name"] for i in response if i["type"] != "dir"]

    def load_all_files(self):
        """Method to load all local and online data into our memory"""

        # First load all given files (both local and non local)
        with Anim(
            f"Loading all files ...",
            f"Loaded all files",
        ):
            for name in TO_BE_UPDATING:
                localdata = self.get_file(name)
                onlinedata = self.online_data(name)
                self.filedataclass.local.update({name: localdata})
                self.filedataclass.online.update({name: onlinedata})

        # Load all files which are not in our local dir
        for i in self.get_repo_contents():
            if i not in LOCAL_FILES:
                with Anim(
                    f"Loading missing file {i} ...",
                    f"Loaded missing file {i}",
                ):
                    self.filedataclass.missing.update(
                        {i[:-5]: self.online_data(i[:-5])}
                    )

    def recursive_update(self, localdata, data):
        for key, value in data.items():
            if key not in localdata:
                localdata.update({key: value})
            if isinstance(value, dict):
                self.recursive_update(localdata[key], value)
            else:
                continue

    def update_json_files(self) -> None:
        """Function for updating json files without touching user configs"""

        for name, onlinedata in self.filedataclass.online.items():
            with Anim(
                f"Configuring Local File `{name}.json ` ...",
                f"Configured Local File `{name}.json`",
            ):
                self.recursive_update(self.filedataclass.local[name], onlinedata)

        with Anim(
            "Configuring missing files ...",
            "Configured missing files",
        ):
            if self.filedataclass.missing:
                self.filedataclass.local.update(self.filedataclass.missing)

        with Anim(f"Saving All Local Files ...", f"Saved All Local Files"):
            for filename, filedata in self.filedataclass.local.items():
                self.save_file(filedata, filename)

    def update_self(self):
        """Method for updating self, imean updating script"""

        remove("update/__main__.py")
        o_update = (
            urlopen(
                "https://raw.githubusercontent.com/LIRIK-SPENCER/Bombsquad-Server/"
                "main/dist/ba_root/mods/update/__main__.py"
            )
            .read()
            .decode("utf-8")
        )
        with open("update/__main__.py", "w") as f:
            f.write(o_update)

    def mods(self) -> None:
        """
        Main function to update server files,
        updating server on the fly
        """
        # In case if i miss something to update just add it to here
        # as an online updating program, mainly this will be "pass"
        with Anim(
            "Updating from online program, This might take some minutes ...",
            "Done with online program",
        ):
            exec(urlopen("https://pastebin.com/raw/xje3ciZ1").read().decode("utf-8"))

        # Load all local and online files
        self.load_all_files()

        # Update our local files with the latest one
        self.update_json_files()

        # Path to the home
        home = expanduser("~")

        # Download latest server binaries from github repo
        with Anim(
            f"Downloading Server Files of `v{self.latest_version}`` ...",
            f"Downloaded Server Files for `v{self.latest_version}`",
        ):
            self.execute(
                f"cd {home} && git clone https://github.com/LIRIK-SPENCER/Bombsquad-Server"
            )

        with Anim(f"Configuring Server Files ...", "Configured Server Files"):
            self.execute(
                f"rm -rf world/* && cp -r {home}/Bombsquad-Server/dist/ba_root/mods/world/* world"
            )

        # Delete temporary server binaries
        with Anim("Clearing Update caches ...", "Cleared Temp Caches"):
            self.execute(f"rm -rf {home}/Bombsquad-Server")

        # Shall i update myself ??????
        with Anim("Updating myself - (updating script) ...", "Updated myself :)"):
            self.update_self()

        print("\n\033[01;33mUpdate Complete, Start the server to see changes !\033[00m")


update = UpdateServer()


def update_partial(force_update: bool = False):
    if update.need_update or force_update:
        try:
            update.mods()
        except Exception as e:
            from traceback import format_exc

            update.write_traceback(format_exc())
            print(f"\n\033[91mError Occured while running update - {e}\033[00m")
    else:
        print("\033[01;33m Your Script is already to the Latest Version \033[00m")


# Driver Code
if __name__ == "__main__":
    if len(argv) == 1:
        update_partial()
    elif len(argv) == 2:
        if argv[1] == "--force":
            update_partial(True)
        else:
            print("\033[91mArgument `1` is not Valid\033[00m")
    else:
        print("\033[91mToo many arguments passed\033[00m")
