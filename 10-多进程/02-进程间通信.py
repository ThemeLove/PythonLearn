import multiprocessing


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
