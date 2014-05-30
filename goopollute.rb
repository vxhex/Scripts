require 'watir'

class Goopollute

    # Constructor
    def initialize()
        @debug = true
        @words = File.readlines '/usr/share/dict/words'
        @browser = Watir::Browser.new :firefox
    end

    # Get words to search for
    def getWords()
        out = ''
        num_of_words = rand(3)
        (0..num_of_words).each do
            out += @words.sample.strip + ' '
        end
        return out
    end

    # Navigate to the login page and wait for creds to be entered
    def doLogin()
        print "Please enter your login credentials\n" if @debug
        @browser.link(:id, 'gb_70').click
        @browser.text_field(:name, 'q').wait_until_present
    end

    # Picks a random action to take
    def chooseAction()
        case rand 100
        when 0..19
            # New search
            self.newSearch()
        when 20..49
            # Next page
            self.nextPage()
        when 50..99
            # Click random link
            self.clickLink()
        else
            print 'Herp derp'
        end
        sleep 3
    end

    # Go to the search homepage
    def goHome()
        @browser.goto 'http://www.google.com/'
    end

    # Clicks a random search result link
    def clickLink()
        print "Click link\n" if @debug
        @browser.div(:id, 'resultStats').wait_until_present
        results = []
        @browser.h3s(:class, 'r').each do |h3|
            a = h3.link
            if a.href !~ /http(?:s)?:\/\/(?:www\.)?google.com/
                results << a
            end
        end
        result = results.sample
        result.click
        sleep rand 15..90
        @browser.back
    end

    # Do a new search
    def newSearch()
        print "New search\n" if @debug
        self.goHome()
        @browser.text_field(:name, 'q').set self.getWords()
        @browser.button(:name, 'btnG').click
        sleep rand 3..10
    end

    # Clicks next page button
    def nextPage()
        print "Next page\n" if @debug
        if @browser.link(:id, 'pnnext').exists?
            @browser.link(:id, 'pnnext').click
        end
        sleep rand 3..15
    end

    # Main loop
    def run()
        self.goHome()
        self.doLogin()
        self.newSearch()
        loop do
            self.chooseAction()
        end
    end
end

p = Goopollute.new()
p.run()
