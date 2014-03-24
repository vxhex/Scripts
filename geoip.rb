require 'net/http'
require 'nokogiri'
url = URI.parse('http://geoip.ubuntu.com/lookup?ip=' + ARGV[0])
req = Net::HTTP::Get.new(url.to_s)
res = Net::HTTP.start(url.host, url.port) { |http|
    http.request(req)
}
data = Nokogiri::XML(res.body)
data.xpath('//Response/*').each { |node|
    print "#{node.name}:#{' ' * (15 - node.name.length)}#{node.content}\n"
}
