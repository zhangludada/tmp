import hashlib
import os.path


class Sha:
    # 计算文件的sha值
    def shakey(self, filename):
        """
            用于获取文件的md5值
            :param filename: 文件名
            :return: MD5码
            """

        myhash = hashlib.sha256()
        b=input("请输入内容：")
        b=b.encode("utf-8")
        myhash.update(b)
        return myhash.hexdigest()

    def sha_write(self, source_filename, new_filename):
        with open(new_filename, mode='w', encoding='utf-8') as f:
            f.write(self.shakey(source_filename))
        print('写入完成')

    def sha_check(self, filename1, filename2):
        sha1 = self.shakey(filename1)
        sha2 = self.shakey(filename2)
        if sha1 == sha2:
            print('文件一致')
        else:
            print('文件不同')
        print(sha1)
        print(sha2)












