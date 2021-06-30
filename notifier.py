import pyinotify
from datetime import datetime
import argparse
import warnings
warnings.filterwarnings("ignore")


class Log(pyinotify.ProcessEvent):
    def my_init(self, fileobj):
        """
        Method automatically called from ProcessEvent.__init__(). Additional
        keyworded arguments passed to ProcessEvent.__init__() are then
        delegated to my_init(). This is the case for fileobj.
        """
        self._fileobj = fileobj

    def process_default(self, event):
        self._fileobj.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t' + str(event) + '\n')
        self._fileobj.flush()

class TrackModifications(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        print('IN_MODIFY')

class Empty(pyinotify.ProcessEvent):
    def my_init(self, msg):
        self._msg = msg

    def process_default(self, event):
        print(self._msg)


def parse_cli_arguments():
    parser = argparse.ArgumentParser(
        u"Python PyiNotifier events watcher and logger"
    )
    parser.add_argument(u"--monitor_dir", required=True, type=str, help="Directory to watch, e.g. -> './testdir/' ")
    parser.add_argument(u"--logs_dir", required=False, type=str, default='./pyinotify_moonbug_NAS_log.log',
                        help="Directory to save logs, e.g. -> './logs/logs.log/' ")
    return parser.parse_args()


def monitor():
    parsed_cli_arguments = parse_cli_arguments()
    monitor_dir = parsed_cli_arguments.monitor_dir
    dir_logs = parsed_cli_arguments.logs_dir

    logs_outputs = open(dir_logs, "a")

    try:
        watch_manager = pyinotify.WatchManager()
        mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MODIFY
        handler = Empty(TrackModifications(Log(fileobj=logs_outputs)), msg = f"Logs updated {datetime.now()}")
        notifier = pyinotify.Notifier(watch_manager, default_proc_fun=handler)
        watch_manager.add_watch(monitor_dir, mask=mask, rec=True)
        notifier.loop()
    except KeyboardInterrupt:
        logs_outputs.close()
    finally:
        logs_outputs.close()


if __name__ == "__main__":
    monitor()