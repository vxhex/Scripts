require 'mongo'

connection = Mongo::Connection.new(ARGV[0])
connection.database_names.each do |name|
  db = connection.db(name)
  db.collections.each do |collection|
    puts "#{name} - #{collection.name}"
  end
end
