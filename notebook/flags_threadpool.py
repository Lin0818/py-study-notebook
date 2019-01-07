# flags_threadpool.py threaded download script using futures.Thread
from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKER = 20

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    workers = min(MAX_WORKER, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))
    
    return len(list(res))

if __name__ == '__main__':
    main(download_many)
