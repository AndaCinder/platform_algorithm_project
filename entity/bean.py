import json
from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class CapabilityInfo:
    def __init__(self, max_tps, cur_tps, max_cvs, cur_cvs):
        """
        查询算法资源信息接口这个方法返回的参数
        :param max_tps:
            图片流最大并发数（即每秒最多可以处理图片的张数）
            图片流模式下：
                0:表示功能不可用，大于 0:每秒最大图片并发分析数视频流模式下：填 0
        :param cur_tps:
            图片流当前并发数（即当前每秒处理的图片张数）
            图片流模式下：
                按实际填写视频流模式下：填 0
        :param max_cvs:
            视频流最大并发数（即算法服务最多可以分析视频流的路数）
            图片流模式下：填 0
            视频流模式：
                0:表示功能不可用，大于 0:最大并发分析码流路数
        :param cur_cvs:
            视频流当前并发数（即算法服务当前已经分析的视频流路数）
            图片流模式下：填 0
        """
        self.max_tps = max_tps
        self.cur_tps = cur_tps
        self.max_cvs = max_cvs
        self.cur_cvs = cur_cvs

    def __iter__(self):
        yield from {
            "max_tps": self.max_tps,
            "cur_tps": self.cur_tps,
            "max_cvs": self.max_cvs,
            "cur_cvs": self.cur_cvs
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
