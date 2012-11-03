##
# Base64 Piracy Helper Script (bpirate.rb)
# The goal is to share binary files via base64 encoding. Upload your mp3s and tars to blogspot, pastebin,
# whatever and share links with everyone. Grab the base64, decode, ???, profit.
#
# TODO: Support for multiple files at url
# TODO: Specify file header/suffix
# TODO: Support for other encoding options

require 'open-uri'
require 'base64'
require 'optparse'

options = {}

optparse = OptionParser.new do |opts|
	opts.banner = "Usage:\nbpirate.rb [options] -p FILE\nbpirate.rb [options] -g URL"
	
	options[:get] = nil
	opts.on( '-g', '--get URL', 'Extracts BPirate files in the target URL' ) do |url|
		options[:get] = url
	end
	
	options[:put] = nil
	opts.on( '-p', '--put FILE', 'Encodes local file into BPirate format' ) do |file|
		options[:put] = file
	end
	
	options[:info] = false
	opts.on( '-i', '--info', 'Use with -g, only read file info' ) do
		options[:info] = true
	end
 
	opts.on( '-h', '--help', 'Display this screen' ) do
		puts opts
		exit
	end
end

optparse.parse!

if options[:get]
	html = open(options[:get]).read
	carved = html.match(/---BEGIN:?(.*?)---(.*?)---END---/im)
	outName = carved[1].gsub(/\s+/, "")
	outFile = carved[2].gsub(/\s+/, "")

	if options[:info]
		print "File info: #{outName}"
	else
		print "Creating file: #{outName}"
		open(outName, "wb") do |file|  
			file.print Base64.decode64(outFile.strip)
		end
	end
end

if options[:put]
	print "\n---BEGIN: #{options[:put]}---\n"
	print Base64.encode64(File.read(options[:put]))
	print "---END---\n"
end
