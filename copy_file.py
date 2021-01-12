import shutil
import os
import time
import threading
import logging
format ="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(filename="copy_img.log",level=logging.DEBUG,format=format)
dir_path = "/home/kylin-ksvd/ksvd-orgs/org-0/users/0local/"
src_file=dir_path + "mcadmin1/win7/USER.IMG"
dest_dirs = os.listdir(dir_path)
dest_dirs.remove("mcadmin1")
#多线程类，拷贝文件
class MyThread(threading.Thread):
    def __init__(self,dest_dir):
        threading.Thread.__init__(self)
        self.dest_dir = dest_dir
        self.src_file = src_file
    def run(self):
        with threading_max_num:
            if not os.path.exists(self.src_file) :
                logging.error("the %s is not exists!" %src_file)

            else:
                try:
                    shutil.copy(self.src_file,self.dest_dir)
                    time.sleep(1)
                    logging.info("copy file %s is sucess!" %self.dest_dir)
                except Exception as e:
                    logging.error(e)
#设置最大线程10，控制线程数避免拷贝占用太多内存
threading_max_num = threading.Semaphore(10)


for dest_dir in dest_dirs:
    dest_dir = dir_path+dest_dir+"/win7/"
#    if not os.path.exists(dest_path):
#        os.mkdir(dest_path)
    sub_thread = MyThread(dest_dir)
    sub_thread.start()



