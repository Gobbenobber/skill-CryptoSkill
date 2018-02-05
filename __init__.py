# Import statements: 
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import requests

__author__ = 'Patrick B. Bjerregaard and Malthe Dalgaard Jensen'

# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
LOGGER = getLogger(__name__)

# The logic of each skill is contained within its own class, which inherits
# base methods from the MycroftSkill class with the syntax you can see below:
# "class ____Skill(MycroftSkill)"
class CryptoSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(CryptoSkill, self).__init__(name="CryptoSkill")

#--------------------------------INITIALIZER------------------------------

    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))
        
        #GLOBAL SECTION
        TotalMarketCap_Intent = IntentBuilder("TotalMarketCapIntent").\
            require("CryptoKeyword").require("MCKeyword").build()
        self.register_intent(TotalMarketCap_Intent, self.handle_TotalMarketCap_Intent)
        
        TopThreeCoins_Intent = IntentBuilder("TopThreeCoinsIntent").\
            require("CryptoKeyword").require("TopThreeKeyword").build()
        self.register_intent(TopThreeCoins_Intent, self.handle_TopThreeCoins_Intent)
        
        #BITCOIN SECTION
        BitcoinPrice_Intent = IntentBuilder("BitcoinPriceIntent").\
            require("BitcoinKeyword").require("BitcoinPriceKeyword").build()
        self.register_intent(BitcoinPrice_Intent, self.handle_BitcoinPrice_Intent)
        
        BitcoinMC_Intent = IntentBuilder("BitcoinMarketCapIntent").\
            require("BitcoinKeyword").require("MCKeyword").build()
        self.register_intent(BitcoinMC_Intent, self.handle_BitcoinMC_Intent)
        
        #LITECOIN SECTION
        LitecoinPrice_Intent = IntentBuilder("LitecoinPriceIntent").\
            require("LitecoinKeyword").require("BitcoinPriceKeyword").build()
        self.register_intent(LitecoinPrice_Intent, self.handle_LitecoinPrice_Intent)

        LitecoinMC_Intent = IntentBuilder("LitecoinMarketCapIntent").\
            require("LitecoinKeyword").require("MCKeyword").build()
        self.register_intent(LitecoinMC_Intent, self.handle_LitecoinMC_Intent)

        #RIPPLE SECTION
        RipplePrice_Intent = IntentBuilder("RipplePriceIntent").\
            require("RippleKeyword").require("BitcoinPriceKeyword").build()
        self.register_intent(RipplePrice_Intent, self.handle_RipplePrice_Intent)

        RippleMC_Intent = IntentBuilder("RippleMarketCapIntent").\
            require("RippleKeyword").require("MCKeyword").build()
        self.register_intent(RippleMC_Intent, self.handle_RippleMC_Intent)

		#CARDANO SECTION
        CardanoPrice_Intent = IntentBuilder("CardanoPriceIntent").\
            require("CardanoKeyword").require("BitcoinPriceKeyword").build()
        self.register_intent(CardanoPrice_Intent, self.handle_CardanoPrice_Intent)

        CardanoMC_Intent = IntentBuilder("CardanoMarketCapIntent").\
            require("CardanoKeyword").require("MCKeyword").build()
        self.register_intent(CardanoMC_Intent, self.handle_CardanoMC_Intent)

#--------------------------------HANDLERS------------------------------

    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered.
    
    #GLOBAL SECTION
    def handle_TotalMarketCap_Intent(self, message):
        self.speak_dialog("MarketCap")
        data = requests.get("https://api.coinmarketcap.com/v1/global/").json()
        self.speak(data["total_market_cap_usd"])
        self.speak("US dollars.")
    
    def handle_TopThreeCoins_Intent(self, message):
        self.speak_dialog("TopThreeCoins")
        TopThreeCoins = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=3").json()
        for x in TopThreeCoins:
            for idx in x:
                x[idx] = int(x[idx])
                sproken = "The %d. most valuable coin is: " % (x[idx])
                LOGGER.error("{0}".format(sproken))
                self.speak(sproken)
                self.speak(TopThreeCoins[x]["name"])
                self.speak("Which currently has a market value of:")
                self.speak(TopThreeCoins[x]["price_usd"])
                self.speak("US dollars per coin.")
       
    #BITCOIN SECTION
    def handle_BitcoinPrice_Intent(self, message):
        self.speak_dialog("BitcoinPrice")
        data = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin/").json()[0]["price_usd"]
        self.speak(data)
        self.speak("US dollars.")
        
    def handle_BitcoinMC_Intent(self, message):
        self.speak_dialog("MarketCap")
        data = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin/").json()[0]["market_cap_usd"]
        self.speak(data)
        self.speak("US dollars.")    
        
    #LITECOIN SECTION
    def handle_LitecoinPrice_Intent(self, message):
        self.speak_dialog("LitecoinPrice")
        data = requests.get("https://api.coinmarketcap.com/v1/ticker/litecoin/").json()[0]["price_usd"]
        self.speak(data)
        self.speak("US dollars.")
        
    def handle_LitecoinMC_Intent(self, message):
        self.speak_dialog("MarketCap")
        data = requests.get("https://api.coinmarketcap.com/v1/ticker/litecoin/").json()[0]["market_cap_usd"]
        self.speak(data)
        self.speak("US dollars.")

    #RIPPLE SECTION
    def handle_RipplePrice_Intent(self, message):
        self.speak_dialog("RipplePrice")
        data = requests.get("https://api.coinmarketcap.com/v1/ticker/ripple/").json()[0]["price_usd"]
        self.speak(data)
        self.speak("US dollars.")
        
    def handle_RippleMC_Intent(self, message):
        self.speak_dialog("MarketCap")
        data = requests.get("https://api.coinmarketcap.com/v1/ticker/ripple/").json()[0]["market_cap_usd"]
        self.speak(data)
        self.speak("US dollars.")

    #CARDANO SECTION
    def handle_CardanoPrice_Intent(self, message):
        self.speak_dialog("CardanoPrice")
        data = requests.get("https://api.coinmarketcap.com/v1/ticker/cardano/").json()[0]["price_usd"]
        self.speak(data)
        self.speak("US dollars.")
        
    def handle_CardanoMC_Intent(self, message):
        self.speak_dialog("MarketCap")
        data = requests.get("https://api.coinmarketcap.com/v1/ticker/cardano/").json()[0]["market_cap_usd"]
        self.speak(data)
        self.speak("US dollars.")
        
    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return CryptoSkill()