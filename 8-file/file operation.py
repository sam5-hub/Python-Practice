import os

#1.用open创建/打开文件

foo_path = 'foo.txt'

file1 = open(foo_path,'wt')
print('Hello File', file = file1)
file1.close()


#2. 用exist()检查文件/目录是否存在

os.path.exists(foo_path)
#True


#3.用 isfile() 检查是否为文件
os.path.isfile(foo_path)
os.path.isdir(foo_path) 

#4.isabs判断绝对路径 /a/c/d

os.path.isabs(foo_path)

#4.1 用 abspath() 获取路径名
os.path.abspath(foo_path) #foo.txt => ' /usr/gaberlunzie/oops.txt'

#5.用 copy() 复制文件

import shutil
new_path = 'abc.txt'
shutil.copy(foo_path, new_path)

#6.用 rename() 重命名文件

os.rename(foo_path, new_path)

#7.用 remove() 删除文件
os.remove(foo_path)
os.path.exists(foo_path) #False

#8.用 link() 或者 symlink() 创建链接

#islink() 函数会检查参数是文件还是符号链接。
#link() 会创建一个硬链接。 

os.link(foo_path,new_path)
os.path.islink(new_path)

#symlink() 会创建一个符号链接。 
os.symlink( ' oops.txt', ' jeepers.txt')
os.path.islink( ' jeepers.txt') #True


#9.用 chmod() 可以修改文件权限

#可以设置用户、当前用户所在用户组以及其他所有用户组的读、写和执行权限。

import stat

#这个值包含用户、用户组和权限 0o400
#如果你不想用压缩过的八进制值并且更喜欢那些（有点）难懂的符号，可以从 stat 模块中 导入一些常量并用在语句中：

os.chmod( ' oops.txt', stat.S_IRUSR)


#10.用 chown() 修改所有者
#你可以指定用户的 ID（uid）和用户组 ID（gid）来 修改文件的所有者和 / 或所有用户组：

uid = 5  #ID（uid）
gid = 22 #用户组 ID（gid）
os.chown( ' oops', uid, gid)