import multiprocessing


'''
queue = multiprocessing.Queue(3) 参数表示该队列最多存放的数据个数，数据可以是任意类型
queue.put() 往队列中添加一个数据，队列中的数据数量加1
queue.get() 从队列中获取数据，如果有就按先进先出的规则获取一个，队列中的数据数量减一，如果队列中是empty，则阻塞，直到获取到数据为止
queue.full() 判断队列是否满了
queue.empty() 判断队列是否为空
queue.get_nowait() 不等待直接从队列中获取数据，不管队列中是否有数据，如果没有就报错
'''


def download_from_web(q):
    # 模拟从网上下载的数据
    data = ["c","c#","c++","java","python"]

    for temp in data:
        q.put(temp)
        if q.full():
            break
    print("-----下载器已经下载完数据并且存放到共享队列中-----")


def analysis_data(q):
    waiting_analysis_data = []
    # 从列队中获取数据
    while True:
        data = q.get()
        waiting_analysis_data.append(data)

        if q.empty():
            break
    print("分析器已经分析的数据："+str(waiting_analysis_data))


def main():
    q = multiprocessing.Queue(5)
    download_process = multiprocessing.Process(target=download_from_web(q))
    analysis_process = multiprocessing.Process(target=analysis_data(q))

    download_process.start()
    analysis_process.start()


if __name__ == "__main__":
    main()
