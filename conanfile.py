from conans import ConanFile, CMake, tools


class UcaConan(ConanFile):
    name = "uca-net"
    version = "9906e95"
    license = "MIT"
    author = "Marius Elvert marius.elvert@softwareschneiderei.de"
    url = "https://github.com/ufo-kit/libuca"
    description = "TCP-based network bridge for libuca."
    topics = ("utilities",)
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake"
    exports_sources = "*.h", "*.c", "include/*", "test/*", "bin/*", "CMakeLists.txt", "config.h.in", "package.sh.in"
    requires = "libuca/2.3.0",

    def _configured_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        return cmake

    def build(self):
        self._configured_cmake().build()

    def package(self):
        self._configured_cmake().install()

    def imports(self):
        self.copy("*.dll", "bin", "bin")
        self.copy("*.dylib", "lib", "lib")
        
    def deploy(self):
        self.copy("*.exe")
        self.copy("*.dll")
        self.copy_deps("*.dll")
