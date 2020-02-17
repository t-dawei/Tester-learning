import logging
import os


class Logger:

    def __init__(self, name):
        # 创建一个 logger 实例
        self.logger = logging.getLogger(name)
        # 设置 log 等级
        self.logger.setLevel(logging.DEBUG)

        # 获取根目录
        log_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

        # 设置 log 输出目录
        log_path = log_path + '/out-log/' + self.logger.name + '.log'

        # 设置文件具柄
        fh = logging.FileHandler(log_path, mode='w', encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 创建一个具柄，用于将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
            '-%(levelname)s-[日志信息]: %(message)s', datefmt='%a, %d %b %Y %H:%M:%S'
        )

        fh.setFormatter(formatter)
        # ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    @property
    def get_log(self):
        """定义一个函数，回调logger实例"""
        return self.logger


if __name__ == '__main__':
    log = Logger(__name__).get_log
    log.error('模块直接执行打印日志')