# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


# Visit https://docs.mycroft.ai/skill.creation for more detailed information
# on the structure of this skill and its containing folder, as well as
# instructions for designing your own skill based on this template.


# Import statements: 
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import requests

__author__ = 'Patrick Bjerregaard and Malthe Dalgaard Jensen'

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
        LitecoinMC_Intent = IntentBuilder("LitecoinMarketCapIntent").\
            require("LitecoinKeyword").require("MCKeyword").build()
        self.register_intent(LitecoinMC_Intent, self.handle_LitecoinMC_Intent)

        LitecoinPrice_Intent = IntentBuilder("LitecoinPriceIntent").\
            require("LitecoinKeyword").require("BitcoinPriceKeyword").build()
        self.register_intent(LitecoinPrice_Intent, self.handle_LitecoinPrice_Intent)
        
    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered.
    
    #GLOBAL SECTION
    def handle_TotalMarketCap_Intent(self, message):
        self.speak_dialog("MarketCap")
        data = requests.get("https://api.coinmarketcap.com/v1/global/").json()[0]["total_market_cap_usd"]
        self.speak(data)
        self.speak("US dollars.")
    
    def handle_TopThreeCoins_Intent
        self.speak_dialog("TopThreeCoins")
        TopThreeCoins = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=3").json()
        TopCoin = TopThreeCoins[0]["name"]
        TopCoinVal = TopThreeCoins[0]["price_usd"]
        SecondCoin = TopThreeCoins[1]["name"]
        SecondCoinVal = TopThreeCoins[1]["price_usd"]
        ThirdCoin = TopThreeCoins[2]["name"]
        ThirdCoinVal = TopThreeCoins[2]["price_usd"]
        self.speak("The most valuable coin is:")
        self.speak(TopCoin)
        self.speak("Which currently has a market value of:")
        self.speak(TopCoinVal)
        self.speak("per coin.")
        self.speak("The second most valuable coin is:")
        self.speak(SecondCoin)
        self.speak("Which currently has a market value of:")
        self.speak(SecondCoinVal)
        self.speak("per coin.")
        self.speak("The third most valuable coin is:")
        self.speak(ThirdCoin)
        self.speak("Which currently has a market value of:")
        self.speak(ThirdCoinVal)
        self.speak("per coin.")
       
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
    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return CryptoSkill()
