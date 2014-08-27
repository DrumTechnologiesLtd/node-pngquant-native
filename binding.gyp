{
    'variables': { 'target_arch%': 'x64' },

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

            'src/libpng-1.6.12/pngerror.c',
            'src/libpng-1.6.12/pngget.c',
            'src/libpng-1.6.12/pngmem.c',
            'src/libpng-1.6.12/pngpread.c',
            'src/libpng-1.6.12/pngread.c',
            'src/libpng-1.6.12/pngrio.c',
            'src/libpng-1.6.12/pngrtran.c',
            'src/libpng-1.6.12/pngrutil.c',
            'src/libpng-1.6.12/pngset.c',
            'src/libpng-1.6.12/pngtrans.c',
            'src/libpng-1.6.12/pngwio.c',
            'src/libpng-1.6.12/pngwrite.c',
            'src/libpng-1.6.12/pngwtran.c',
            'src/libpng-1.6.12/pngwutil.c',
            'src/libpng-1.6.12/png.c',

            'src/zlib-1.2.8/adler32.c',
            'src/zlib-1.2.8/compress.c',
            'src/zlib-1.2.8/crc32.c',
            'src/zlib-1.2.8/gzclose.c',
            'src/zlib-1.2.8/gzlib.c',
            'src/zlib-1.2.8/gzread.c',
            'src/zlib-1.2.8/gzwrite.c',
            'src/zlib-1.2.8/infback.c',
            'src/zlib-1.2.8/inffast.c',
            'src/zlib-1.2.8/inflate.c',
            'src/zlib-1.2.8/inftrees.c',
            'src/zlib-1.2.8/trees.c',
            'src/zlib-1.2.8/uncompr.c',
            'src/zlib-1.2.8/zutil.c'
        ],
        'include_dirs': [
            'src/zlib-1.2.8',
            'src/libpng-1.6.12',
            # platform and arch-specific headers
            'src/zlib-1.2.8/config/<(OS)/<(target_arch)'
        ],
        'conditions': [
            ['OS == "win"', {
                'variables': { 'target_arch%': '<!(echo %PROCESSOR_ARCHITECTURE%)' },
            }],
            ['OS == "mac"', {
                'variables': { 'target_arch%': '<!(uname -m)' },
            }]
        ],
    }]
}
