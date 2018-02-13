# Import statements: 
from os.path import dirname
import requests
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Patrick B. Bjerregaard and Malthe Dalgaard Jensen'

LOGGER = getLogger(__name__)

class CryptoSkill(MycroftSkill):

#--------------------------------INITIALIZER------------------------------

    def __init__(self):
        super(CryptoSkill, self).__init__(name="CryptoSkill")

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

        Bitcoin24HrChange_Intent = IntentBuilder("Bitcoin24HrChangeIntent").\
            require("BitcoinKeyword").require("24HrChangeKeyword").build()
        self.register_intent(Bitcoin24HrChange_Intent, self.handle_Bitcoin24HrChange_Intent)
        
        #LITECOIN SECTION
        LitecoinPrice_Intent = IntentBuilder("LitecoinPriceIntent").\
            require("LitecoinKeyword").require("BitcoinPriceKeyword").build()
        self.register_intent(LitecoinPrice_Intent, self.handle_LitecoinPrice_Intent)

        LitecoinMC_Intent = IntentBuilder("LitecoinMarketCapIntent").\
            require("LitecoinKeyword").require("MCKeyword").build()
        self.register_intent(LitecoinMC_Intent, self.handle_LitecoinMC_Intent)

        Litecoin24HrChange_Intent = IntentBuilder("Litecoin24HrChangeIntent").\
            require("LitecoinKeyword").require("24HrChangeKeyword").build()
        self.register_intent(Litecoin24HrChange_Intent, self.handle_Litecoin24HrChange_Intent)

        #RIPPLE SECTION
        RipplePrice_Intent = IntentBuilder("RipplePriceIntent").\
            require("RippleKeyword").require("BitcoinPriceKeyword").build()
        self.register_intent(RipplePrice_Intent, self.handle_RipplePrice_Intent)

        RippleMC_Intent = IntentBuilder("RippleMarketCapIntent").\
            require("RippleKeyword").require("MCKeyword").build()
        self.register_intent(RippleMC_Intent, self.handle_RippleMC_Intent)

        Ripple24HrChange_Intent = IntentBuilder("Ripple24HrChangeIntent").\
            require("RippleKeyword").require("24HrChangeKeyword").build()
        self.register_intent(Ripple24HrChange_Intent, self.handle_Ripple24HrChange_Intent)

        #ETHEREUM SECTION
        EthereumPrice_Intent = IntentBuilder("EthereumPriceIntent").\
            require("EthereumKeyword").require("BitcoinPriceKeyword").build()
        self.register_intent(EthereumPrice_Intent, self.handle_EthereumPrice_Intent)

        EthereumMC_Intent = IntentBuilder("EthereumMarketCapIntent").\
            require("EthereumKeyword").require("MCKeyword").build()
        self.register_intent(EthereumMC_Intent, self.handle_EthereumMC_Intent)

        Ethereum24HrChange_Intent = IntentBuilder("Ethereum24HrChangeIntent").\
            require("EthereumKeyword").require("24HrChangeKeyword").build()
        self.register_intent(Ethereum24HrChange_Intent, self.handle_Ethereum24HrChange_Intent)

		#CARDANO SECTION
        CardanoPrice_Intent = IntentBuilder("CardanoPriceIntent").\
            require("CardanoKeyword").require("BitcoinPriceKeyword").build()
        self.register_intent(CardanoPrice_Intent, self.handle_CardanoPrice_Intent)

        CardanoMC_Intent = IntentBuilder("CardanoMarketCapIntent").\
            require("CardanoKeyword").require("MCKeyword").build()
        self.register_intent(CardanoMC_Intent, self.handle_CardanoMC_Intent)

        Cardano24HrChange_Intent = IntentBuilder("Cardano24HrChangeIntent").\
            require("CardanoKeyword").require("24HrChangeKeyword").build()
        self.register_intent(Cardano24HrChange_Intent, self.handle_Cardano24HrChange_Intent)

        #MONERO SECTION
        MoneroPrice_Intent = IntentBuilder("MoneroPriceIntent").\
            require("MoneroKeyword").require("BitcoinPriceKeyword").build()
        self.register_intent(MoneroPrice_Intent, self.handle_MoneroPrice_Intent)

        MoneroMC_Intent = IntentBuilder("MoneroMarketCapIntent").\
            require("MoneroKeyword").require("MCKeyword").build()
        self.register_intent(MoneroMC_Intent, self.handle_MoneroMC_Intent)

        Monero24HrChange_Intent = IntentBuilder("Monero24HrChangeIntent").\
            require("MoneroKeyword").require("24HrChangeKeyword").build()
        self.register_intent(Monero24HrChange_Intent, self.handle_Monero24HrChange_Intent)
#--------------------------------HANDLERS------------------------------
    
    #GLOBAL SECTION
    def handle_TotalMarketCap_Intent(self, message):
        self.speak_dialog("MarketCap")
        data = requests.get("https://api.coinmarketcap.com/v1/global/").json()["total_market_cap_usd"]/1000000000
        self.speak(str(data)[:5])
        self.speak("billion US dollars.")
    
    def handle_TopThreeCoins_Intent(self, message):
        self.speak_dialog("TopThreeCoins")
        TopThreeCoins = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=3").json()
        for x in range(0,3):
            list = ['','second','third']
            sproken = "The %s most valuable cryptocurrency is: " % (list[x])
            self.speak(sproken)
            self.speak(TopThreeCoins[x]["name"])
            self.speak("Which currently has a market value of:")
            self.speak(TopThreeCoins[x]["price_usd"])
            self.speak("US dollars per coin.")
       
    #BITCOIN SECTION
    btcurl = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"

    def handle_BitcoinPrice_Intent(self, message):
        self.speak_dialog("BitcoinPrice")
        data = requests.get(self.btcurl).json()[0]["price_usd"]
        self.speak(data)
        self.speak("US dollars.")
        
    def handle_BitcoinMC_Intent(self, message):
        self.speak_dialog("MarketCap")
        data = requests.get(self.btcurl).json()[0]["market_cap_usd"]
        self.speak(data)
        self.speak("US dollars.")
        
    def handle_Bitcoin24HrChange_Intent(self, message):
        self.speak_dialog("24HrChange")
        data = requests.get(self.btcurl).json()[0]
        self.speak(data["name"])
        if data["percent_change_24h"][0] > 0:
            self.speak("has risen by:")
            self.speak(data["percent_change_24h"] + " percent")
        elif data["percent_change_24h"][0] < 0:
            self.speak("has fallen by:")
            self.speak(data["percent_change_24h"] + " percent")
            
    #LITECOIN SECTION
    ltcurl = "https://api.coinmarketcap.com/v1/ticker/litecoin/"

    def handle_LitecoinPrice_Intent(self, message):
        self.speak_dialog("LitecoinPrice")
        data = requests.get(self.ltcurl).json()[0]["price_usd"]
        self.speak(data)
        self.speak("US dollars.")
        
    def handle_LitecoinMC_Intent(self, message):
        self.speak_dialog("MarketCap")
        data = requests.get(self.ltcurl).json()[0]["market_cap_usd"]
        self.speak(data)
        self.speak("US dollars.")

    def handle_Litecoin24HrChange_Intent(self, message):
        self.speak_dialog("24HrChange")
        data = requests.get(self.ltcurl).json()[0]
        self.speak(data["name"])
        if data["percent_change_24h"][0] > 0:
            self.speak("has risen by:")
            self.speak(data["percent_change_24h"] + " percent")
        elif data["percent_change_24h"][0] < 0:
            self.speak("has fallen by:")
            self.speak(data["percent_change_24h"] + " percent")

    #RIPPLE SECTION
    xrpurl = "https://api.coinmarketcap.com/v1/ticker/ripple/"

    def handle_RipplePrice_Intent(self, message):
        self.speak_dialog("RipplePrice")
        data = requests.get(self.xrpurl).json()[0]["price_usd"]
        self.speak(data)
        self.speak("US dollars.")
        
    def handle_RippleMC_Intent(self, message):
        self.speak_dialog("MarketCap")
        data = requests.get(self.xrpurl).json()[0]["market_cap_usd"]
        self.speak(data)
        self.speak("US dollars.")

    def handle_Ripple24HrChange_Intent(self, message):
        self.speak_dialog("24HrChange")
        data = requests.get(self.xrpurl).json()[0]
        self.speak(data["name"])
        if data["percent_change_24h"][0] > 0:
            self.speak("has risen by:")
            self.speak(data["percent_change_24h"] + " percent")
        elif data["percent_change_24h"][0] < 0:
            self.speak("has fallen by:")
            self.speak(data["percent_change_24h"] + " percent")

    #ETHEREUM SECTION
    ethurl = "https://api.coinmarketcap.com/v1/ticker/ethereum/"

    def handle_EthereumPrice_Intent(self, message):
        self.speak_dialog("EthereumPrice")
        data = requests.get(self.ethurl).json()[0]["price_usd"]
        self.speak(data)
        self.speak("US dollars.")
        
    def handle_EthereumMC_Intent(self, message):
        self.speak_dialog("MarketCap")
        data = requests.get(self.ethurl).json()[0]["market_cap_usd"]
        self.speak(data)
        self.speak("US dollars.")

    def handle_Ethereum24HrChange_Intent(self, message):
        self.speak_dialog("24HrChange")
        data = requests.get(self.ethurl).json()[0]
        self.speak(data["name"])
        if data["percent_change_24h"][0] > 0:
            self.speak("has risen by:")
            self.speak(data["percent_change_24h"] + " percent")
        elif data["percent_change_24h"][0] < 0:
            self.speak("has fallen by:")
            self.speak(data["percent_change_24h"] + " percent")

    #CARDANO SECTION
    adaurl = "https://api.coinmarketcap.com/v1/ticker/cardano/"

    def handle_CardanoPrice_Intent(self, message):
        self.speak_dialog("CardanoPrice")
        data = requests.get(self.adaurl).json()[0]["price_usd"]
        self.speak(data)
        self.speak("US dollars.")
        
    def handle_CardanoMC_Intent(self, message):
        self.speak_dialog("MarketCap")
        data = requests.get(self.adaurl).json()[0]["market_cap_usd"]
        self.speak(data)
        self.speak("US dollars.")

    def handle_Cardano24HrChange_Intent(self, message):
        self.speak_dialog("24HrChange")
        data = requests.get(self.adaurl).json()[0]
        self.speak(data["name"])
        if data["percent_change_24h"][0] > 0:
            self.speak("has risen by:")
            self.speak(data["percent_change_24h"] + " percent")
        elif data["percent_change_24h"][0] < 0:
            self.speak("has fallen by:")
            self.speak(data["percent_change_24h"] + " percent")
        
    #MONERO SECTION
    xmrurl = "https://api.coinmarketcap.com/v1/ticker/monero/"

    def handle_MoneroPrice_Intent(self, message):
        self.speak_dialog("MoneroPrice")
        data = requests.get(self.xmrurl).json()[0]["price_usd"]
        self.speak(data)
        self.speak("US dollars.")
        
    def handle_MoneroMC_Intent(self, message):
        self.speak_dialog("MarketCap")
        data = requests.get(self.xmrurl).json()[0]["market_cap_usd"]
        self.speak(data)
        self.speak("US dollars.")

    def handle_Monero24HrChange_Intent(self, message):
        self.speak_dialog("24HrChange")
        data = requests.get(self.xmrurl).json()[0]
        self.speak(data["name"])
        if data["percent_change_24h"][0] > 0:
            self.speak("has risen by:")
            self.speak(data["percent_change_24h"] + " percent")
        elif data["percent_change_24h"][0] < 0:
            self.speak("has fallen by:")
            self.speak(data["percent_change_24h"] + " percent")
    
    #OTHER FUNCTIONS

    def stop(self):
        pass

def create_skill():
    return CryptoSkill()