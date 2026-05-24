on darkos-re, retroarch32 is saving its main configuration to /home/ark/.config/retroarch/retroarch.cfg , but loads from /home/ark/.config/retroarch32/retroarch.cfg , effectively overriding 64 bits configs and not saving their own.

this path is probably baked into binary, but autosaving's isn't, so this is the fix:
echo 'config_directory = "~/.config/retroarch32"' >> /home/ark/.config/retroarch32/retroarch.cfg