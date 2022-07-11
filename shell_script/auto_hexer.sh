nasm -felf64 asm.asm -o asm.o
ld asm.o -o asm
objcopy -O binary asm call
hexdump -v -e ' 1/1 "%02x"""' call
rm asm asm.o call