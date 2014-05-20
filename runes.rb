# encoding: utf-8

runes_to_show = 3

runes = ['ᚠ', 'ᚢ', 'ᚦ', 'ᚨ', 'ᚱ', 'ᚲ', 'ᚷ', 'ᚹ', 'ᚺ', 'ᚾ', 'ᛁ', 'ᛃ', 'ᛇ', 'ᛈ', 'ᛉ', 'ᛊ', 'ᛏ', 'ᛒ', 'ᛖ', 'ᛗ', 'ᛚ', 'ᛝ', 'ᛟ', 'ᛞ']

print "
+------------------+
| Runes of the Day |
+------------------+\n"

(1 .. runes_to_show).each do
	print "#{runes.delete_at(rand(runes.length))}  "
end
print "\n"
