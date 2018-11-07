#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostUuidConan(base.BoostBaseConan):
    name = "boost_uuid"
    url = "https://github.com/bincrafters/conan-boost_uuid"
    lib_short_names = ["uuid"]
    header_only_libs = ["uuid"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_io",
        "boost_numeric_conversion",
        "boost_predef",
        "boost_random",
        "boost_serialization",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_tti",
        "boost_type_traits",
        "boost_winapi"
    ]

    def package_info_additional(self):
        if self.settings.os == "Windows":
            self.cpp_info.libs.append("Bcrypt")

    def package_id_additional(self):
        self.info.header_only()
        self.info.settings.os = str(self.settings.os)

