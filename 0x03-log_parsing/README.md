## 03 - Log Parsing

For the “0x03. Log Parsing” project, you will need to apply your knowledge of Python programming, focusing on parsing and processing data streams in real-time. This project involves reading from standard input (stdin), handling data in a specific format, and performing calculations based on the input data. Here’s a list of concepts and resources that you might find useful:

### Knowledges Needed:

1. **File I/O in Python**:

   - Understand how to read from `sys.stdin` line by line.
   - [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html "Python Input and Output")

2. **Signal Handling in Python**:

   - Handling keyboard interruption (CTRL + C) using signal handling in Python.
   - [Python Signal Handling](https://docs.python.org/3/library/signal.html "Python Signal Handling")

3. **Data Processing**:

   - Parsing strings to extract specific data points.
   - Aggregating data to compute summaries.

4. **Regular Expressions**:

   - Using regular expressions to validate the format of each line.
   - [Python Regular Expressions](https://docs.python.org/3/library/re.html "Python Regular Expressions")

5. **Dictionaries in Python**:

   - Using dictionaries to count occurrences of status codes and accumulate file sizes.
   - [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries "Python Dictionaries")

6. **Exception Handling**:

   - Handling possible exceptions that may arise during file reading and data processing.
   - [Python Exceptions](https://docs.python.org/3/tutorial/errors.html "Python Exceptions")

By studying these concepts and utilizing the resources provided, you will be well-prepared to tackle the log parsing project, effectively handling data streams, parsing log entries, and computing metrics based on the processed data.

### Additional Resources

- [Mock Technical Interview](https://www.youtube.com/watch?feature=shared&v=5dRTK-_Bzd0 "Mock Technical Interview")

### Tasks

<details>
<summary>0. Log parsing</summary>

Create a script that processes input from `stdin` line by line, calculating specific metrics:

- The expected input format is: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`. If a line does not match this format, it should be ignored.
- After processing every 10 lines or upon receiving a keyboard interruption `(CTRL + C)`, the script should display the following statistics from the start:
  - The cumulative file size: `File size: <total size>`
  - where <total size> is the sum of all previous `<file size>`. (see input format above)
  - The count of lines for each status code:
    - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500` - if a status code doesn’t appear or is not an integer, it should not print anything for this status code
    - The format for each status code should be: `<status code>: <count>`.
    - status codes should be listed in ascending order

**Warning:** The output may vary due to the random nature of the input data.

```sh
alexa@ubuntu:~/0x03-log_parsing$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./0-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
alexa@ubuntu:~/0x03-log_parsing$
```

**File:**

- `0-stats.py`
