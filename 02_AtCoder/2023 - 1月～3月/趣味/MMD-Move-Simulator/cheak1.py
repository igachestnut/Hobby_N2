#フォルダ作成と、pngファイルの保存

import os
"""
if os.path.isdir("dir_01") == False :
    os.mkdir('dir_01')
else :
    os.mkdir('dir_02')

new_dir_path = "dir_ex"
os.makedirs(new_dir_path, exist_ok=True)

"""

def save_file_at_dir(dir_path, filename, file_content, mode='w'):
    #新しくdir (ディレクトリ)を生成する。被った場合passする。
    os.makedirs(dir_path, exist_ok=True)
    
    #作成したファイルを開く
    with open(os.path.join(dir_path, filename), mode) as f:
        #ファイルを保存する。
        f.write(file_content)
        


save_file_at_dir('new_dir/sub2_dir', 'new_file.txt', 'new text')
#/で二つ生成？いや、new_dir/sub_dirの生成が正しいかも
#for文で作っているわけではなく、一気に
#もし、new_dirが被っていたとしても、sub2_dirが変わっていたら
#その中に新しく生成することができる。



