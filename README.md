# CryptoSkill

This skill utilizes the CoinMarketCap API found on <https://api.coinmarketcap.com> to deliver cryptocurrency-related functionality for Mycroft.

## Current state

### Working features

The following coins have been implemented:
- Bitcoin
- Cardano
- Ethereum
- Litecoin
- Monero
- Ripple

The following features have been implemented:
- Price
- Market cap
- 24 hour change

To make use of a given functionality, simply say a given coin's name or ticker (e.g. XRP for Ripple) and one of the implemented features in the same sentence. E.g. "Hey Mycroft, what's the market cap of Litecoin?" or "Hey Mycroft, what's the 24 hour change of Monero?".

Additionally, this skill provides the following features related to the cryptocurrency market in general:
- Total market cap (say "cryptocurrency/-coin" and "market cap" in the same sentence)
- Top three cryptocurrencies (say "top three" and "cryptocurrencies/-coins" in the same sentence)

### Untested features

None at this moment.

### Known issues

None at this moment.

### TODO

- Crypto top 10
  - Price
    - 1 hour percent change
    - 24 hour percent change
    - 7 day percent change
  - Market cap
    - Total market cap
    - 24 hour percent change
- Smarter implementation
- More to come...
