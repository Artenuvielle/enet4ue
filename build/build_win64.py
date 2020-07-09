import subprocess
import os
import sys
import shutil
import winreg

vs_intermediate     = "_vs_tmp"
src_path            = "../../enet-source"
out_path            = "../../enet"
prefix_path         = "_prefix"

def create_vs_prj_with_compiler(compiler_version):
    cmd_line = ["cmake", "-G", compiler_version]
    #install prefix
    cmd_line.append("-DCMAKE_INSTALL_PREFIX="+os.path.join(os.getcwd(), prefix_path))
    cmd_line.append("-DCMAKE_CONFIGURATION_TYPES=Release")
    cmd_line.append("-Denet_BUILD_TESTS=false")
    cmd_line.append("-Denet_MSVC_STATIC_RUNTIME=false")
    cmd_line.append(src_path)
    subprocess.call(cmd_line)
    
def get_vs2015_devenv():
    try:
        #get visual studio install path
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\WOW6432Node\\Microsoft\\VisualStudio\\14.0")
        reg_value, reg_type = winreg.QueryValueEx(reg_key, "InstallDir")
        winreg.CloseKey(reg_key);
        if(reg_type != winreg.REG_SZ):
            print(reg_type)
            return None
        return os.path.join(reg_value, "devenv.com")
    except:
        return None

def get_vs2017_devenv():
    try:
        #get visual studio install path
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\WOW6432Node\\Microsoft\\VisualStudio\\SxS\\VS7")
        reg_value, reg_type = winreg.QueryValueEx(reg_key, "15.0")
        winreg.CloseKey(reg_key);
        if(reg_type != winreg.REG_SZ):
            print(reg_type)
            return None
        return os.path.join(reg_value, "Common7", "IDE", "devenv.com")
    except:
        return None

def get_vs2019_devenv():
    try:
        #get visual studio install path
        path = os.path.join("C:\\Program Files (x86)", "Microsoft Visual Studio", "2019", "Community", "Common7", "IDE", "devenv.com")
        if(os.path.isfile(path)):
            return path
        else:
            print(path)
            return none
    except:
        return None
    
def copy_library():
    target_include = os.path.join(out_path, "include");
    if(os.path.exists(target_include)):
        shutil.rmtree(target_include, True)
    shutil.copytree(os.path.join(src_path, "include"), target_include)
    
    #shutil.copy(os.path.join(prefix_path, "bin/protoc.exe"), os.path.join(libprotobuf_path, "bin/protoc.exe"))
    
    target_lib = os.path.join(out_path, "lib/win64");
    if(os.path.exists(target_lib)):
        shutil.rmtree(target_lib, True)
    os.makedirs(target_lib)
    shutil.copy(os.path.join("Release", "enet.lib"), os.path.join(out_path, "lib/win64/enet.lib"))
    
##################################################

#create intermediate path
if os.path.exists(vs_intermediate):
    shutil.rmtree(vs_intermediate, True)
os.mkdir(vs_intermediate)
os.chdir(vs_intermediate)

#get vs version devenv
vs_compiler_version = "Visual Studio 14 2015 Win64"
devenv_path = get_vs2015_devenv()
if(devenv_path == None):
    vs_compiler_version = "Visual Studio 15 2017 Win64"
    devenv_path = get_vs2017_devenv()
    if(devenv_path == None):
        print("Could neither find VS2015 nor VS2017")
        quit()
        vs_compiler_version = "Visual Studio 16 2019"
        devenv_path = get_vs2019_devenv()
        if(devenv_path == None):
            print("Could neither find VS2015, nor VS2017, nor VS2019")
            quit()

#create vs project files
create_vs_prj_with_compiler(vs_compiler_version)

#build vs project 
subprocess.call([devenv_path, "enet.sln", "/Build", "Release|x64", "/Project", "enet"])


#copy library files
copy_library()

