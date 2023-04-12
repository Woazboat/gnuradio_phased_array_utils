find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_PHASED_ARRAY_2D gnuradio-phased_array_2d)

FIND_PATH(
    GR_PHASED_ARRAY_2D_INCLUDE_DIRS
    NAMES gnuradio/phased_array_2d/api.h
    HINTS $ENV{PHASED_ARRAY_2D_DIR}/include
        ${PC_PHASED_ARRAY_2D_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_PHASED_ARRAY_2D_LIBRARIES
    NAMES gnuradio-phased_array_2d
    HINTS $ENV{PHASED_ARRAY_2D_DIR}/lib
        ${PC_PHASED_ARRAY_2D_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-phased_array_2dTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_PHASED_ARRAY_2D DEFAULT_MSG GR_PHASED_ARRAY_2D_LIBRARIES GR_PHASED_ARRAY_2D_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_PHASED_ARRAY_2D_LIBRARIES GR_PHASED_ARRAY_2D_INCLUDE_DIRS)
