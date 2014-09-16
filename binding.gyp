{
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
            'src/libpng-1.6.12/png.c'

        ],
        'include_dirs': [
            'src/libpng-1.6.12'
        ],
        'conditions': [
            ['OS == "win"', {
            }, {
                'libraries': [
                    '-lz',
                    '-lm'
                ]
            }]
        ],
    }]
}
