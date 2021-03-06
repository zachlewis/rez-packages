CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


if(${MAYA_MAJOR_VERSION} EQUAL 2015)
    set(arch_maya "")
    set(ADLM_RELEASE R9)
elseif(${MAYA_MAJOR_VERSION} EQUAL 2016)
    set(arch_maya "_64bit")
    if(${MAYA_MINOR_VERSION} EQUAL 5)
        set(ADLM_RELEASE R12)
    else()
        set(ADLM_RELEASE R11)
    endif()
else()
    set(arch_maya "_64bit")
    set(ADLM_RELEASE R12)
endif()


configure_file(config/AdlmThinClientCustomEnv.xml.in AdlmThinClientCustomEnv.xml @ONLY)
configure_file(config/License.env.in License.env @ONLY)
set(syncfg_file Maya${MAYA_MAJOR_VERSION}.${MAYA_MAJOR_VERSION}.${MAYA_MINOR_VERSION}.64.syncfg)
set(MAYA_EXECUTABLE ${CMAKE_INSTALL_PREFIX}/maya/bin/maya.bin)
set(MAYA_WRAPPER ${CMAKE_INSTALL_PREFIX}/maya/bin/maya${MAYA_MAJOR_VERSION})
configure_file(config/synergy.syncfg.in ${syncfg_file} @ONLY)

configure_file(config/bin/maya.in bin/maya @ONLY)
configure_file(config/bin/register_maya.in bin/register_maya @ONLY)


set(url_maya
    ${CMAKE_CURRENT_SOURCE_DIR}/archives/Autodesk_Maya_${MAYA_MAJOR_VERSION}_EXT2_SP2_EN_Linux${arch_maya}.tgz)

set(build_cmd ${CMAKE_CURRENT_SOURCE_DIR}/extract.sh  ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR} ${MAYA_MAJOR_VERSION} )


if(${REZ_BUILD_INSTALL})
    set(install_cmd ${CMAKE_CURRENT_SOURCE_DIR}/install.sh  ${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_INSTALL_PREFIX} ${MAYA_MAJOR_VERSION})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    maya
    URL ${url_maya}
    PREFIX maya
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ${build_cmd}
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 0
)


rez_install_files(
    ${CMAKE_CURRENT_BINARY_DIR}/AdlmThinClientCustomEnv.xml
    ${CMAKE_CURRENT_BINARY_DIR}/${syncfg_file}
    RELATIVE build/platform-linux/arch-x86_64
    DESTINATION .
)


rez_install_files(
    ${CMAKE_CURRENT_BINARY_DIR}/License.env
    RELATIVE build/platform-linux/arch-x86_64
    DESTINATION maya/bin
)


rez_install_files(
    config/license.lic
    RELATIVE config
    DESTINATION .
)


install(PROGRAMS
    ${CMAKE_CURRENT_BINARY_DIR}/bin/maya
    ${CMAKE_CURRENT_BINARY_DIR}/bin/register_maya
    DESTINATION maya/bin
)


rez_install_files(
    cmake/maya.cmake
    DESTINATION .
)


rez_install_files(
    config/MayaNoColorManagement.xml
    RELATIVE config
    DESTINATION .
)
