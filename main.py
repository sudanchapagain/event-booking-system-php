#!/usr/bin/env python3

import asyncio
import sys
from pathlib import Path


def start_server():
    import subprocess

    cmd = [
        "uv",
        "run",
        "python",
        "-m",
        "uvicorn",
        "app.main:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
        "--reload",
    ]
    subprocess.run(cmd)


async def seed_database():
    from scripts.seed_database import create_sample_data

    await create_sample_data()
    print("db seeded!")


def main():
    if len(sys.argv) < 2:
        print("usage: python manage.py <command>")
        print("Commands:")
        print("")
        print("server    - Start development server")
        print("seed      - Seed database with sample data")
        return

    command = sys.argv[1]

    if command == "server":
        start_server()
    elif command == "seed":
        asyncio.run(seed_database())
    else:
        print(f"unknown command: {command}")


if __name__ == "__main__":
    main()
