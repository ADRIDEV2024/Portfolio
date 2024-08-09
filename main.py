import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemHandler 


logging.basicConfig(level=logging.INFO, format="%{asctime}s - %{message}s", datefmt="%Y-%m-%d %H:%M:%S")

class Filetracker(FileSystemHandler):
  
    def on_modified(self, event):
        
        logging.info(f"File modified: {event.src_path}")
   
    def on_created(self, event):
        
        logging.info(f"File created: {event.src_path}")
    
    
   
    def on_deleted(self, event):
        
        logging.info(f"File deleted: {event.src_path}")
        
def track_dir(dir):
    
    event_handler = Filetracker()
    
    observer_handler = Observer()
    observer_handler.schedule(event_handler, dir, recursive=True)
    
    observer_handler.start()
    
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer_handler.stop()
        observer_handler.join()
        
if __name__ == "__main__":
    dir_to_track = r"C:\Users\EVO\Ajustes"
    track_dir(dir_to_track)
        
