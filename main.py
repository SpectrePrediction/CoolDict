class CoolDict(object):

    def __init__(self, maintain_dict: dict = None):
        super().__init__()
        """
        self.maintain_dict： 维护字典
        维护字典负责所有的变量存储，无论是任何方式访问
        本质结果都是从self.maintain_dict中获取
        """
        self.maintain_dict = dict() if not maintain_dict else maintain_dict

    def __getattr__(self, item):
        """
        获取没有的成员时触发
        :param item:
        :return:
        """
        temp = self.maintain_dict.get(item)
        if not temp:
            raise KeyError(f"{item} 不存在")
        if isinstance(temp, dict):
            return CoolDict(temp)
        elif isinstance(temp, list):
            return [CoolDict(_) for _ in temp if isinstance(_, dict)]
        return temp

    def __setattr__(self, key, value):
        """
        设置成员时触发
        :param key:
        :param value:
        :return:
        """
        if key == "maintain_dict":
            # 防止循环调用
            super().__setattr__(key, value)
            return
        # 并不会真正生成attr，仅仅添加字典
        self.maintain_dict[key] = value

    def __getitem__(self, y):
        """ x.__getitem__(y) <==> x[y] """
        return self.__getattr__(y)

    def __delitem__(self, item):
        """ Delete self[key]. """
        try:
            del self.maintain_dict[item]
        except KeyError:
            raise KeyError(f"key：{item} is not define")

    def __setitem__(self, key, value):
        """ x.__setitem__(y) <==> x[y] = 1 y=1"""
        self.maintain_dict[key] = value

    def set_maintain_dict(self, maintain_dict):
        self.maintain_dict = maintain_dict

    def __str__(self):
        return self.maintain_dict.__str__()

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    md = CoolDict()

    md.test = 1
    del md["test"]

    md.set_maintain_dict({"test": 2})
    print(md.test)

