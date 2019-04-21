import os


def get_file(root_path, all_files={}):
    '''
    递归函数，遍历该文档目录和子目录下的所有文件，获取其path
    '''
    files = os.listdir(root_path)
    for file in files:
        if not os.path.isdir(root_path + '/' + file):  
            all_files[file] = root_path + '/' + file
        else:  
            get_file((root_path+'/'+file), all_files)
    return all_files


if __name__ == '__main__':
    path = './raw_data'
    print(get_file(path))

