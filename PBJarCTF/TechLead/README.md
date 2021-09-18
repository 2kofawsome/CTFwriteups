# misc/TechLead

>misc/TechLead

> Points\
>Infamous YouTuber, and ex-Google / ex-Facebook TechLead found a quick way to make a few million dollars of a crypto scam (as a millionare). He created the ERC-20 token Million (MM), and started promoting it on his social media platforms. The deployer address of the Million token smart contract is the personal address of TechLead, what is the highest historical Ethereum balance of his personal address? Million Token: https://coinmarketcap.com/currencies/million/ Flag format: flag{0.006942069420}

***

Going to https://coinmarketcap.com/currencies/million/, I found the address of the largest holder 0x5922b0bbae5182f2b70609f5dfd08f7da561f5a4

In addition, these reddit posts https://www.reddit.com/r/milliontoken/comments/ocefgi/haha_would_i_dump_17_of_total_supply_that_i_have/ and https://www.reddit.com/r/CryptoCurrency/comments/odusa6/techlead_youtuber_with_11_million_subscribers_is/ seemed to confirm my view that this is techlead

Now searching this address up on https://etherscan.io/balancecheck-tool, and zooming in to the maximum possible I wrote down 1.4625790953780384 as the maximum

Giving the desired flag,

```
flag{1.4625790953780384}
```
