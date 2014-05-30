require 'open-uri'
require 'json'

text = open('https://api.github.com/users/vxhex/repos').read
json = JSON.parse text
json.each do |repo|
    `git clone  #{repo['clone_url']} #{repo['name']}`
end
