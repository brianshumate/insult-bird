#!/usr/bin/env python2
# -*- coding: utf-8 -*- #

import json
import sys
import re
import random
from twitterbot import TwitterBot


class InsultBird(TwitterBot):

    def bot_init(self):
        """
        Initialize and configure your bot!

        Use this function to set options and initialize your own custom bot
        state (if any).
        """

        ############################
        # REQUIRED: LOGIN DETAILS! #
        ############################

        with open("etc/access.json", 'r') as access:
            authdb = json.load(access)

        self.config['api_key'] = authdb["API_Key"]
        self.config['api_secret'] = authdb["API_Secret"]
        self.config['access_key'] = authdb["Access_Token"]
        self.config['access_secret'] = authdb["Access_Token_Secret"]

        access.close()

        ######################################
        # SEMI-OPTIONAL: OTHER CONFIG STUFF! #
        ######################################

        # how often to tweet, in seconds
        self.config['tweet_interval'] = 15 * 60     # 15 minutes

        # use this to define a (min, max) random range of how often to tweet
        # e.g., self.config['tweet_interval_range'] = (5*60, 10*60) # tweets every 5-10 minutes
        self.config['tweet_interval_range'] = None

        # only reply to tweets that specifically mention the bot
        self.config['reply_direct_mention_only'] = False

        # only include bot followers (and original tweeter) in @-replies
        self.config['reply_followers_only'] = False

        # fav any tweets that mention this bot?
        self.config['autofav_mentions'] = False

        # fav any tweets containing these keywords?
        self.config['autofav_keywords'] = ['pirate', 'robot pirate', 'yarrr']

        # follow back all followers?
        self.config['autofollow'] = True


        ###########################################
        # CUSTOM: your bot's own state variables! #
        ###########################################

        # If you'd like to save variables with the bot's state, use the
        # self.state dictionary. These will only be initialized if the bot is
        # not loading a previous saved state.

        # self.state['butt_counter'] = 0

        # You can also add custom functions that run at regular intervals
        # using self.register_custom_handler(function, interval).
        #
        # For instance, if your normal timeline tweet interval is every 30
        # minutes, but you'd also like to post something different every 24
        # hours, you would implement self.my_function and add the following
        # line here:

        # self.register_custom_handler(self.my_function, 60 * 60 * 24)

    def get_insult(self):
        starters = ['You are nothing but', 'You are uglier than',
            'You smell worse than', 'Your mother is', 'You remind me of',
            'You have the consistency of', 'You look worse than',
            'You are more foul than', 'You are more repulsive than' ]
        nouns = ['Stimpy-drool', 'Sun IPC manuals', 'anal warts', 'apple-johns', 'armadillo snouts', 'assclowns', 'assfaces', 'asshats', 'assholes', 'assmunches', 'asswipes', 'baggage', 'barnacles', 'bastards', 'bastiges', 'bat toenails', 'bitches', 'bladders', 'boar-pigs', 'bubbas', 'bug spit', 'bugbears', 'bum-bailies', 'buzzard gizzards', 'canker-blossums', 'cat bladders', 'cat hair', 'cat-hair-balls', 'chicken piss', 'city-slickers', 'clack-dishes', 'clotpoles', 'codpieces', 'cold sores', 'corksuckers', 'coxcomb', 'craptacular carpet droppings', 'cunnies', 'cunts', 'dandies', 'dbags', 'death-tokens', 'dewberries', 'dillholes', 'dillweeds', 'dog balls', 'dog vomit', 'donkey farts', 'douchebags', 'dung', 'eel ooze', 'entrails', 'fancypants', 'fart trains', 'fart-blossoms', 'fart-quaffers', 'fart-willows', 'fart-winkles', 'fartfaces', "fat woman's stomach-bile", 'ferret barf', 'fish heads', 'flap-dragons', 'flax-wenches', 'flirt-gills', 'foot-lickers', 'fuckers', 'fuckfaces', 'fuckheads', 'fucktards', 'fuckwits', 'geeks', 'genital warts', 'giglets', 'guano', 'gudgeons', 'gunk', 'haggards', 'harpies', 'hedge-pigs', 'hillbillies', 'hippies', 'horn-beasts', 'hugger-muggers', 'iceholes', 'jizzum', 'joitheads', 'lewdsters', 'lizard farts', 'louts', 'maggot-pies', 'maggots', 'malt-worms', 'mammers', 'measles', 'meatheads', 'metrosexuals', 'minnows', 'miscreants', 'moldwarps', 'monkey crabs', 'monkey dandruff', 'monkeyasses', 'nerds', 'nut-hooks', 'pantywastes', 'pigeon-eggs', 'pignuts', 'pods', 'pond scum', 'poons', 'poop', 'poopy', 'pumpkins', 'pus', 'puttocks', 'rat retch', 'rat-farts', 'ratsbanes', 'red dye number-9', 'rednecks', 'scabs', 'schmucks', 'scuts', 'seagull puke', 'shit for brains', 'shit-snorts', 'shit-stains', 'shit-sticks', 'shitheads', 'shits', 'skainsmates', 'sleestaks', 'slurpee-backwash', 'snake assholes', 'snake bait', 'snake snot', 'squirrel guts', 'strumpets', 'sumbitches', 'taints', 'thumb-suckers', 'tit-willows', 'tits', 'toxic waste', 'troll nuggets', 'urine samples', 'varlots', 'vassals', 'waffle-house grits', 'wagtails', 'whey-faces', 'wig-flippers', 'yokels', 'yoo-hoo']
        amounts = ['accumulation', 'ass-full', 'assload', 'bag', 'bucket', 'coagulation', 'cubic fuck', 'doggy-bag', 'dumptruck load', 'enema-bucketful', 'gallon', 'glop', 'gob', 'half-mouthful', 'handful', 'heap', 'hectacre', 'mason jar full', 'mass', 'metric ass ton', 'metric fuck ton', 'metric shite tonne', 'mound', 'ooze', 'petrification', 'pile', 'plate', 'puddle', 'quart', 'shit ton', 'stack', 'thimbleful', 'tongueful', 'wheelbarrow load']
        adjectives = ['Microsoft-loving', 'acidic', 'antique', 'artless', 'bawdy', 'beef-witted', 'beslubbering', 'boil-brained', 'bootless', 'churlish', 'clapper-clawed', 'clouted', 'cockered', 'common-kissing', 'contemptible', 'coughed-up', 'craven', 'crook-pated', 'culturally-unsound', 'currish', 'dankish', 'decayed', 'despicable', 'dizzy-eyed', 'dread-bolted', 'droning', 'egg-sucking', 'elf-skinned', 'evil', 'fawning', 'fen-sucked', 'fermented', 'festering', 'flap-mouthed', 'fly-bitten', 'fobbing', 'folly-fallen', 'fool-born', 'foul', 'frothy', 'full-gorged', 'fulminating', 'gleeking', 'goatish', 'gorbellied', 'hacked-up', 'half-faced', 'halfbaked', 'hasty-witted', 'headless', 'hedge-born', 'horn-beat', 'hugger-muggered', 'humid', 'ill-borne', 'imp-bladdereddle-headed', 'impertinent', 'impure', 'industrial', 'inept', 'infected', 'inferior', 'it-fowling', 'jarring', 'knotty-pated', 'left-over', 'lewd-minded', 'loggerheaded', 'low-quality', 'lumpish', 'malodorous', 'malt-wormy', 'mammering', 'mangled', 'measled', 'milk-livered', 'motley-mind', 'off-color', 'onion-eyed', 'penguin-molesting', 'petrified', 'pickled', 'pignutted', 'plume-plucked', 'pointy-nosed', 'porous', 'pox-marked', 'pribbling', 'puny', 'rank', 'reeky', 'rude-snouted', 'rump-fed', 'ruttish', 'salty', 'saucyspleened', 'sausage-snorfling', 'sheep-biting', 'spam-sucking', 'spongy', 'spur-galled', 'squishy', 'surly', 'swag-bellied', 'tasteless', 'tempestuous', 'tepid', 'thick', 'tickle-brained', 'toad-spotted', 'tofu-nibbling', 'tottering', 'uninspiring', 'unintelligent', 'unmuzzled', 'unoriginal', 'vain', 'vapid', 'vassal-willed', 'villainous', 'warped', 'wayward', 'weasel-smelling', 'weather-bitten', 'weedy', 'wretched', 'yeasty']
        starter = starters[random.randint(0, len(starters) - 1)]
        adj1 = adjectives[random.randint(0, len(adjectives) - 1)]
        adj2 = adjectives[random.randint(0, len(adjectives) - 1)]
        noun = nouns[random.randint(0, len(nouns) - 1)]
        amount = amounts[random.randint(0, len(amounts) - 1)]
        if adj1 == adj2:
            adj2 = adjectives[random.randint(0, len(adjectives) - 1)]
        if not adj1[0] in 'aeiou':
            an = 'a'
        else:
            an = 'an'
        return '%s %s %s %s of %s %s.' % (starter, an, adj1, amount, adj2, noun)


    def on_scheduled_tweet(self):
        text = self.get_insult()
        self.post_tweet(text)

    def on_mention(self, tweet, prefix):

        text = self.get_insult()
        prefixed_text = prefix + ' ' + text
        self.post_tweet(prefix + ' ' + text, reply_to=tweet)


    def on_timeline(self, tweet, prefix):
        pass

if __name__ == '__main__':
    bot = InsultBird()
    bot.run()
