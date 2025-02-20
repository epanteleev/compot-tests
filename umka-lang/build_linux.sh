#!/bin/sh

gccwflags="-Wall -Wno-format-security"
gccflags="-s -g -malign-double -fno-strict-aliasing -fPIC -DUMKA_BUILD -DUMKA_EXT_LIBS $gccwflags"
sourcefiles="umka_vm.c umka_expr.c umka_const.c umka_ident.c umka_common.c umka_decl.c umka_compiler.c umka_stmt.c umka_lexer.c umka_gen.c umka_types.c umka_runtime.c umka_api.c"

rm umka_linux -rf && # remove previous build

cd src &&

$CC $gccflags -O1 -c $sourcefiles &&

$CC $gccflags -c umka.c &&
gcc *.o -o umka -static-libgcc -L$PWD -lm -Wl,-rpath,'$ORIGIN' &&
ar rcs libumka_static.a *.o &&

rm -f *.o &&
rm -f *.a &&

cd .. &&

mkdir umka_linux/examples/3dcam -p &&
mkdir umka_linux/examples/fractal -p &&
mkdir umka_linux/examples/lisp -p &&
mkdir umka_linux/examples/raytracer -p &&
mkdir umka_linux/doc &&

mv src/umka umka_linux/ &&
cp src/umka_api.h Umka.sublime-syntax LICENSE umka_linux/ &&

cp examples/* umka_linux/examples -r &&
cp doc/* umka_linux/doc

echo Build successful
