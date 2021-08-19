from lightmatchingengine.lightmatchingengine import LightMatchingEngine, Side

lme = LightMatchingEngine()
order, trades = lme.add_order("EUR/USD", 1.10, 1000, Side.BUY)
