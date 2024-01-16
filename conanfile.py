from conan import ConanFile
from conan.tools.files import update_conandata, copy, chdir, mkdir, collect_libs, download
from conan.tools.layout import basic_layout
from conan.tools.env import Environment
from conan.tools.env import VirtualRunEnv

import os, sys
import sysconfig
from io import StringIO


class GasPreprocessorConan(ConanFile):
    name = "gas-preprocessor"
    version = "cci9309c67"
    license = "bsd"
    url = "https://github.com/FFmpeg/gas-preprocessor"
    settings = "os"
    description="Helper for FFmpeg building on Windows UWP."
    package_type = "application"


    def validate(self):
        if self.settings.os != "Windows" and self.settings.os != "WindowsStore":
            raise ConanInvalidConfiguration("Only windows supported for nuget")


    def generate(self):
        env = Environment()
        return env

    def layout(self):
        basic_layout(self)

    def build(self):
        download(self, "https://raw.githubusercontent.com/FFmpeg/gas-preprocessor/9309c67acb535ca6248f092e96131d8eb07eefc1/gas-preprocessor.pl", 
            os.path.join(self.build_folder, "gas-preprocessor.pl"))

    def package(self):
        copy(self, "*.pl", src=self.build_folder, dst=os.path.join(self.package_folder, "bin"))

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))