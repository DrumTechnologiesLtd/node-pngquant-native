{
    'variables': {
        'THIRD_PATH%': 'third'
    },
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
            'src/pngquant/pngquant.c',
            'src/pngquant/rwpng.c',
            'src/pngquant/lib/pam.c',
            'src/pngquant/lib/mediancut.c',
            'src/pngquant/lib/blur.c',
            'src/pngquant/lib/mempool.c',
            'src/pngquant/lib/viter.c',
            'src/pngquant/lib/nearest.c',
            'src/pngquant/lib/libimagequant.c',

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
        'include_dirs': [
            '<(THIRD_PATH)/libpng',
            '<(THIRD_PATH)/zlib'
        ]
    }]
}
