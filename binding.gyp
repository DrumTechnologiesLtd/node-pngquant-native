{
    'conditions': [
        ['OS=="win"', {
            'variables': {
                'THIRD_PATH%': 'third'
            }
        }]
    ],
    'targets': [{

        'target_name': 'pngquant_native',
        'cflags': [
            '-g',
            '-DNO_ALONE',
            '-DDEBUG',
            '-fno-inline',
            '-O0',
            '-fstrict-aliasing', 
            '-ffast-math',
            '-funroll-loops', 
            '-fomit-frame-pointer', 
            '-ffinite-math-only',
            '-std=c99'

        ],
        'sources': [
            'src/pngquant_native.cpp',
            'src/pngquant/pngquant.cpp',
            'src/pngquant/getopt.c',
            'src/pngquant/rwpng.cpp',
            'src/pngquant/pam.cpp',
            'src/pngquant/mediancut.cpp',
            'src/pngquant/blur.cpp',
            'src/pngquant/mempool.cpp',
            'src/pngquant/viter.cpp',
            'src/pngquant/nearest.cpp', 

            'third/libpng/pngerror.c',
            'third/libpng/pngget.c',
            'third/libpng/pngmem.c',
            'third/libpng/pngpread.c',
            'third/libpng/pngread.c',
            'third/libpng/pngrio.c',
            'third/libpng/pngrtran.c',
            'third/libpng/pngrutil.c',
            'third/libpng/pngset.c',
            'third/libpng/pngtrans.c',
            'third/libpng/pngwio.c',
            'third/libpng/pngwrite.c',
            'third/libpng/pngwtran.c',
            'third/libpng/pngwutil.c',
            'third/libpng/png.c',

            'third/zlib/adler32.c',
            'third/zlib/compress.c',
            'third/zlib/crc32.c',
            'third/zlib/gzclose.c',
            'third/zlib/gzlib.c',
            'third/zlib/gzread.c',
            'third/zlib/gzwrite.c',
            'third/zlib/infback.c',
            'third/zlib/inffast.c',
            'third/zlib/inflate.c',
            'third/zlib/inftrees.c',
            'third/zlib/deflate.c',
            'third/zlib/trees.c',
            'third/zlib/uncompr.c',
            'third/zlib/zutil.c'
        ],
        'conditions': [
            ['OS == "win"', {
                'include_dirs': [
                    '<(THIRD_PATH)/libpng',
                    '<(THIRD_PATH)/zlib']
            }]
        ],
    }]
}
