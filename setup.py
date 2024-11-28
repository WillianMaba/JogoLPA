import os
from cx_Freeze import Executable, setup

path = "./asset"
asset_list= os.listdir(path)
asset_list_completa = [os.path.join(path, asset).replace("\\", "/") for asset in asset_list]
print(asset_list_completa)

executables = [Executable("master.py")]
files = {"include_files": asset_list_completa, "packages": ["pygame"]}

setup(
    name="MountainShooter",
    version="1.0",
    description="Mountain Shooter app",
    options={"build_exe": files},
    executables=executables
)