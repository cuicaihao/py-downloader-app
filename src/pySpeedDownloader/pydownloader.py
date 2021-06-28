from __future__ import annotations
import hashlib
from pathlib import Path
import argparse
# 用于显示进度条
from tqdm import tqdm
# 用于发起网络请求
import requests
# 用于多线程操作
import multitasking
# 导入 retry 库以方便进行下载出错重试
from retry import retry

import signal
signal.signal(signal.SIGINT, multitasking.killall)

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
# 定义 1 MB 多少为 B
MB = 1024**2


def split(start: int, end: int, step: int) -> list[tuple[int, int]]:
    # 分多块
    parts = [(start, min(start+step, end))
             for start in range(0, end, step)]
    # 看最后那一部分的最后一个数字是否等于总大小，不等于就新加一块
    if parts[-1][-1] != end:
        start = step*len(parts)
        parts.append((start, end))
    return parts


def get_file_size(url: str, raise_error: bool = False) -> int:
    '''
    获取文件大小

    Parameters
    ----------
    url : 文件直链
    raise_error : 如果无法获取文件大小，是否引发错误

    Return
    ------
    文件大小（B为单位）
    如果不支持则会报错

    '''
    response = requests.head(url)
    file_size = response.headers.get('Content-Length')
    if file_size is None:
        if raise_error is True:
            raise ValueError('该文件不支持多线程分段下载！')
        return file_size
    return int(file_size)


def hd5check(file_name):
    # with open(file_name) as file_to_check:
    #     # read contents of the file
    #     data = file_to_check.read()
    #     # pipe contents of the file through
    #     md5_returned = hashlib.md5(data).hexdigest()
    return hashlib.md5(open(file_name, 'rb').read()).hexdigest()


def ask_user(Question):
    check = str(input(f"{Question}? (Y/N): ")).lower().strip()
    try:
        if check[0] == 'y':
            return True
        elif check[0] == 'n':
            return False
        else:
            return False  # do not overwrite
            # print('Invalid Input')
            # return ask_user(Question)
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return ask_user(Question)


def pre_download_check(file_name, output_dir):
    if not Path(output_dir).is_dir():
        print(f"{output_dir} does not exist!")
        Path(output_dir).mkdir(parents=True, exist_ok=True)

    download_file_path = Path(output_dir) / file_name
    if download_file_path.exists():
        return True
    else:
        return False


def download(url: str, file_name: str, output_dir: str = './download', check=True,
             retry_times: int = 3, each_size=16*MB) -> None:
    '''
    根据文件直链和文件名下载文件

    Parameters
    ----------
    url : 文件直链
    file_name : 文件名
    retry_times: 可选的，每次连接失败重试次数
    Return
    ------
    None

    '''
    # check the output dir
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    download_file_path = Path(output_dir) / file_name

    answer_yes = True

    if check:
        if pre_download_check(file_name, output_dir):
            answer_yes = ask_user(
                f" ⛔️ {str(download_file_path)} already exists, overwrite it?")
    else:
        answer_yes = True

    if answer_yes:
        download_file_path = str(download_file_path)
        f = open(download_file_path, 'wb')
        file_size = get_file_size(url)
        # print(f"{file_size=}, {each_size=}")

        @retry(tries=retry_times)
        @multitasking.task
        def start_download(start: int, end: int) -> None:
            '''
            根据文件起止位置下载文件

            Parameters
            ----------
            start : 开始位置
            end : 结束位置
            '''
            _headers = headers.copy()
            # 分段下载的核心
            _headers['Range'] = f'bytes={start}-{end}'
            # 发起请求并获取响应（流式）
            response = session.get(url, headers=_headers, stream=True)
            # 每次读取的流式响应大小
            chunk_size = 128
            # 暂存已获取的响应，后续循环写入
            chunks = []
            for chunk in response.iter_content(chunk_size=chunk_size):
                # 暂存获取的响应
                chunks.append(chunk)
                # 更新进度条
                bar.update(chunk_size)
            f.seek(start)
            for chunk in chunks:
                f.write(chunk)
            # 释放已写入的资源
            del chunks

        session = requests.Session()
        # 分块文件如果比文件大，就取文件大小为分块大小
        each_size = min(each_size, file_size)

        # 分块
        parts = split(0, file_size, each_size)
        # print(f'Parts Number: {len(parts)}')
        # 创建进度条
        bar = tqdm(total=file_size, desc=f'Downloading: {file_name}')
        for part in parts:
            start, end = part
            start_download(start, end)
        # 等待全部线程结束
        multitasking.wait_for_tasks()
        f.close()
        bar.close()

    return hd5check(download_file_path)


def test_download_from_github():
    url = 'https://github.com/github/gitignore/archive/refs/heads/master.zip'
    file_name = 'gitignore-master.zip'
    output_dir = './download'
    file_md5 = download(url, file_name, output_dir)
    print(file_md5)


def run(url, file_name, output_dir, check=True):
    print(f"Downloading {file_name}...")
    file_md5 = download(url, file_name, output_dir, check=check)
    return file_md5


if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--url', type=str, default="https://github.com/github/gitignore/archive/refs/heads/master.zip", help='Download URL')
    parser.add_argument('--file_name', type=str,
                        default="gitignore-master.zip", help='Downloaded file name')
    parser.add_argument('--output_dir', type=str,
                        default="./download", help='Download directory')
    args = parser.parse_args()
    # 开始下载文件
    file_md5 = run(args.url, args.file_name, args.output_dir)
    print(f"File MD5 Check: {file_md5}")
