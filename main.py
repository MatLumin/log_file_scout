import os;
from typing import *;
import os.path;


def is_log_file(file_name:str)->bool:
    file_pure_name, file_extension = os.path.splitext(file_name)
    cond1:bool = file_extension.lower() ==".log";
    cond2:bool = False;
    return cond1 or cond2;

def get_root_path()->str:
    return os.getcwd().split("\\")[0];

def cd_to_root()->None:
    os.chdir(get_root_path()+"//");


if __name__ == "__main__":
    with open("output.txt", "w") as output_file:
        output:str = "";

        cd_to_root();
        print("current dir", os.getcwd());
        walker:Generator[str,List[str],List[str]] = os.walk(".");
        for current_path, current_sub_folders, current_sub_files in walker:
            for file_name in current_sub_files:
                if is_log_file(file_name):
                    print(current_path+"\\"+file_name);
                    output += (current_path+"\\"+file_name) + "\n";

        output_file.write(output);


