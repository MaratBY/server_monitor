### Small Scripy for monitoring server side changes in the specific directory
The repository contains script that is able to monitor the changes on the server side (e.g. file addition, file removing, file change,
file modification and etc.). The results of server changes will be written to the logs file or you can provide your own file and directory
to output.

To run the script you need the following dependencies:
- Python 3.4+
- <a href="https://pypi.org/project/pyinotify/"> pyinotify </a>
- Linux/MacOS operating system

To install the pyinotify run the following command in the terminal using pip manager:

`
$ pip3 install -m pyinotify
`

This will install the module to your environment.

To begin monitor server changes run the command:

`
$ python3 notifier.py --monitor_dir'./directory_to_monitor/' --logs_dir './directory_to_output_logs/logs.log'
`

The example of the logs file:

~~~
2021-06-29 15:14:20<Event dir=True mask=0x40000020 maskname=IN_OPEN|IN_ISDIR name='' path=tests pathname=/home/user/python_projects/messaging/tests wd=1 >
2021-06-29 15:14:20<Event dir=True mask=0x40000001 maskname=IN_ACCESS|IN_ISDIR name='' path=tests pathname=/home/user/python_projects/messaging/tests wd=1 >
2021-06-29 15:14:20<Event dir=True mask=0x40000010 maskname=IN_CLOSE_NOWRITE|IN_ISDIR name='' path=tests pathname=/home/user/python_projects/messaging/tests wd=1 >
2021-06-29 15:14:28<Event dir=True mask=0x40000020 maskname=IN_OPEN|IN_ISDIR name='' path=tests pathname=/home/user/python_projects/messaging/tests wd=1 >
2021-06-29 15:14:28<Event dir=True mask=0x40000001 maskname=IN_ACCESS|IN_ISDIR name='' path=tests pathname=/home/user/python_projects/messaging/tests wd=1 >
2021-06-29 15:14:28<Event dir=True mask=0x40000010 maskname=IN_CLOSE_NOWRITE|IN_ISDIR name='' path=tests pathname=/home/user/python_projects/messaging/tests wd=1 >
~~~~


