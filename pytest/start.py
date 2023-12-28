import os
from datetime import datetime
import func

timestamp = datetime.now().strftime('%d%m%Y-%H%M')
date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
wrk_dir = 'results' 
arc_dir = 'archive' 
arc_name = f'arch_{timestamp}.zip'

func.archive_results(wrk_dir, arc_dir, arc_name, 3)

file = open(f"results/result_{timestamp}.txt", "w+")
file.write(f"start time: {date}\n")
file.close()

os.system(f"pytest -v -s test_page.py >> results/result_{timestamp}.txt")
