from conan import ConanFile
from conan.tools.cmake import CMakeToolchain
from conan.tools.files import rmdir, rm, collect_libs
import os


required_conan_version = ">=2.0"


class FmtConan(ConanFile):
    name = "fmt"
    version = "10.2.1"
    python_requires = "aleya-conan-base/1.3.0@aleya/public"
    python_requires_extend = "aleya-conan-base.AleyaCmakeBase"
    ignore_cpp_standard = True

    exports_sources = "source/*"

    options = {
        "shared": [False]
    }

    default_options = {
        "shared": False
    }

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["CMAKE_DEBUG_POSTFIX"] = ''
        tc.variables["FMT_TEST"] = False
        tc.variables["FMT_DOC"] = False
        tc.variables["INSTALL_LIB_DIR"] = "lib"
        tc.variables["INSTALL_INC_DIR"] = "include"
        tc.generate()

    def package(self):
        super().package()

        rmdir(self, os.path.join(self.package_folder, "lib", "cmake"))
        rmdir(self, os.path.join(self.package_folder, "lib", "pkgconfig"))

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "both")
        self.cpp_info.set_property("cmake_file_name", "fmt")
        self.cpp_info.set_property("cmake_target_name", "fmt::fmt")
        self.cpp_info.set_property("pkg_config_name", "fmt")

        self.cpp_info.libs = collect_libs(self)
