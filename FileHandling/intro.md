1. opening a file with the help of context manger class and without "with" class
~~~
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file...")
        if self.file:
            self.file.close()
        return False  # Do not suppress exceptions



fm = FileManager("example.txt", "w")

f = fm.__enter__()      # manually enter the context
try:
    f.write("Hello!")   # use the file
finally:
    fm.__exit__(None, None, None)   # manually exit the context

~~~

Below is a step-by-step progression from the simplest file-opening code in Python to more advanced, safe, and Pythonic patterns.
This shows how file handling evolves from basic to expert-level usage.

🟩 Level 1 — Basic: Open and Close Manually
~~~
f = open("example.txt", "w")
f.write("Hello")
f.close()
~~~

Problems:

If an error occurs, close() may never run → resource leak.

🟨 Level 2 — Better: Use with (Context Manager)
~~~
with open("example.txt", "w") as f:
    f.write("Hello")
~~~

Why better?

Automatically closes file even on exceptions

This is the standard recommended method

🟧 Level 3 — Error Handling with with
~~~
try:
    with open("example.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("No permission to read the file.")
~~~

Adds: Specific exception handling.

🟦 Level 4 — Reading Large Files Efficiently (Streaming)
Read line-by-line (avoids loading entire file in RAM):
~~~
with open("large.txt", "r") as f:
    for line in f:
        print(line.strip())
~~~
🟪 Level 5 — Automatic File Closing Using contextlib.closing
~~~
from contextlib import closing

with closing(open("example.txt", "w")) as f:
    f.write("Hello using contextlib!")
~~~
🟥 Level 6 — Creating Your Own Context Manager Class
~~~
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False  # re-raise exceptions if any

Use it:
with FileManager("example.txt", "w") as f:
    f.write("Hello from custom CM!")
~~~
🔵 Level 7 — Context Manager Using contextlib.contextmanager (Generator-based)
~~~
from contextlib import contextmanager

@contextmanager
def open_file(name, mode):
    f = open(name, mode)
    try:
        yield f
    finally:
        f.close()

Use:
with open_file("example.txt", "w") as f:
    f.write("Hello from generator CM!")
~~~

More concise than defining a class.

🟤 Level 8 — Opening Files with Encoding & Advanced Options
~~~
with open("example.txt", "w", encoding="utf-8", buffering=1) as f:
    f.write("Unicode support ✓")
~~~

encoding

buffering

newline

errors

⚫ Level 9 — Asynchronous File Opening (aiofiles)

(Advanced, used for async web servers, AI tasks, fast IO)
~~~
import aiofiles
import asyncio

async def write_async():
    async with aiofiles.open("example.txt", "w") as f:
        await f.write("Hello async!")

asyncio.run(write_async())
~~~
⭐ Level 10 — Opening Multiple Files at Once
~~~
with open("input.txt") as fin, open("output.txt", "w") as fout:
    for line in fin:
        fout.write(line.upper())
~~~
⭐⭐ Level 11 — Combining Multiple Context Managers
~~~
from contextlib import ExitStack

with ExitStack() as stack:
    f1 = stack.enter_context(open("file1.txt"))
    f2 = stack.enter_context(open("file2.txt", "w"))
    for line in f1:
        f2.write(line)
~~~

ExitStack is extremely powerful when the number of files is dynamic.

⭐⭐⭐ Level 12 — High-Performance Buffered IO (io module)
~~~
import io

with io.open("example.txt", "w", buffering=4096) as f:
    f.write("Fast buffered write")


Or memory-based files:

import io

f = io.StringIO()
f.write("Hello in RAM")
print(f.getvalue())
~~~
🎉 Summary Roadmap

Level	Technique	When to Use

1	Manual open/close	Never in real projects

2	with open()	Daily use (recommended)

3	try/except	Robust error handling

4	Streaming IO	Large files

5	closing()	Quick context manager wrapping

6	Custom context manager class	When needing custom logic

7	contextmanager decorator	Clean custom context managers

8	Encoding & options	International text / special control

9	Async IO	Servers, fast concurrent IO

10	Multiple files	Simple pipelines

11	ExitStack	Dynamic number of resources

12	io module	High performance or memory files
