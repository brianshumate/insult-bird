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
        self.config['reply_direct_mention_only'] = True

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
    nouns = ['bat toenails', 'bug spit', 'cat hair', 'fish heads', 'gunk',
        'pond scum', 'rat retch', 'red dye number-9', 'Sun IPC manuals',
        'waffle-house grits', 'yoo-hoo', 'squirrel guts', 'snake bait',
        'buzzard gizzards', 'cat-hair-balls', 'pods', 'armadillo snouts',
        'entrails', 'snake snot', 'eel ooze', 'toxic waste', 'Stimpy-drool',
        'poopy', 'poop', 'craptacular carpet droppings', 'cold sores',
        'chicken piss', 'dog vomit', 'dung', 'fat woman\'s stomach-bile',
        'guano', 'dog balls', 'seagull puke', 'cat bladders', 'pus',
        'urine samples', 'snake assholes', 'rat-farts', 'slurpee-backwash',
        'jizzum', 'anal warts', 'ferret barf', 'troll nuggets', 'apple-johns',
        'baggage', 'barnacles', 'bladders', 'boar-pigs', 'bugbears',
        'bum-bailies', 'canker-blossums', 'clack-dishes', 'clotpoles',
        'coxcomb', 'codpieces', 'death-tokens', 'dewberries', 'flap-dragons',
        'flax-wenches', 'flirt-gills', 'foot-lickers', 'giglets', 'gudgeons',
        'haggards', 'harpies', 'hedge-pigs', 'horn-beasts', 'hugger-muggers',
        'joitheads', 'lewdsters', 'louts', 'maggot-pies', 'malt-worms',
        'mammers', 'measles', 'minnows', 'miscreants', 'moldwarps',
        'nut-hooks', 'pigeon-eggs', 'puttocks', 'pignuts', 'pumpkins',
        'ratsbanes', 'scuts', 'skainsmates', 'strumpets', 'varlots',
        'vassals', 'whey-faces', 'wagtails', 'bastiges', 'corksuckers',
        'iceholes', 'dillholes', 'assfaces', 'asshats', 'assmunches',
        'assclowns', 'asswipes', 'assholes', 'douchebags', 'dbags',
        'pantywastes', 'schmucks', 'dillweeds', 'sleestaks', 'fuckfaces',
        'fuckheads', 'fuckwits', 'fucktards', 'fuckers', 'bastards',
        'sumbitches', 'bitches', 'fancypants', 'scabs', 'maggots',
        'monkeyasses', 'monkey dandruff', 'monkey crabs', 'tits',
        'tit-willows', 'taints', 'thumb-suckers', 'genital warts',
        'donkey farts', 'lizard farts', 'fart trains', 'fartfaces',
        'fart-quaffers', 'fart-blossoms', 'fart-willows', 'fart-winkles',
        'shits', 'shit-stains', 'shitheads', 'shit for brains', 'shit-snorts',
        'shit-sticks', 'cunts', 'cunnies', 'poons', 'meatheads', 'hippies',
        'rednecks', 'yokels', 'hillbillies', 'city-slickers',
        'metrosexuals', 'bubbas', 'nerds', 'geeks', 'dandies',
        'wig-flippers',
        ]
    amounts = ['accumulation', 'bucket', 'gob', 'coagulation',
        'half-mouthful', 'heap', 'mass', 'mound', 'petrification', 'pile',
        'puddle', 'stack', 'thimbleful', 'tongueful', 'ooze', 'quart', 'bag',
        'plate', 'enema-bucketful', 'ass-full', 'assload', 'shit ton',
        'metric ass ton', 'metric fuck ton', 'metric shite tonne',
        'cubic fuck', 'hectacre', 'doggy-bag', 'handful', 'dumptruck load',
        'wheelbarrow load', 'glop', 'mason jar full', 'gallon',]
    adjectives = ['acidic', 'antique', 'contemptible', 'culturally-unsound',
        'despicable', 'evil', 'fermented', 'festering', 'foul', 'fulminating',
        'humid', 'impure', 'inept', 'inferior', 'industrial', 'left-over',
        'low-quality', 'off-color', 'petrified', 'pointy-nosed', 'salty',
        'sausage-snorfling', 'tasteless', 'tempestuous', 'tepid',
        'tofu-nibbling', 'unintelligent', 'unoriginal', 'uninspiring',
        'weasel-smelling', 'wretched', 'spam-sucking', 'egg-sucking',
        'decayed', 'halfbaked', 'infected', 'squishy', 'porous',
        'pickled', 'thick', 'vapid', 'unmuzzled', 'bawdy', 'vain', 'lumpish',
        'churlish', 'fobbing', 'craven', 'jarring', 'fly-bitten',
        'fen-sucked', 'spongy', 'droning', 'gleeking', 'warped', 'currish',
        'milk-livered', 'surly', 'mammering', 'ill-borne', 'beef-witted',
        'tickle-brained', 'half-faced', 'headless', 'wayward', 'onion-eyed',
        'beslubbering', 'villainous', 'lewd-minded', 'cockered',
        'full-gorged', 'rude-snouted', 'crook-pated', 'pribbling',
        'dread-bolted', 'fool-born', 'puny', 'fawning', 'sheep-biting',
        'dankish', 'goatish', 'weather-bitten', 'knotty-pated', 'malt-wormy',
        'saucyspleened', 'motley-mind', 'it-fowling', 'vassal-willed',
        'loggerheaded', 'clapper-clawed', 'frothy', 'ruttish', 'clouted',
        'common-kissing', 'folly-fallen', 'plume-plucked', 'flap-mouthed',
        'swag-bellied', 'dizzy-eyed', 'gorbellied', 'weedy', 'reeky',
        'measled', 'spur-galled', 'mangled', 'impertinent', 'bootless',
        'toad-spotted', 'hasty-witted', 'horn-beat', 'yeasty', 'hedge-born',
        'imp-bladdereddle-headed', 'tottering', 'hugger-muggered',
        'elf-skinned', 'Microsoft-loving', 'pignutted', 'pox-marked', 'rank',
        'malodorous', 'penguin-molesting', 'coughed-up', 'hacked-up',
        'rump-fed', 'boil-brained', 'artless',]
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
        """
        Make a public tweet to the bot's own timeline.

        It's up to you to ensure that it's less than 140 characters.

        Set tweet frequency in seconds with TWEET_INTERVAL in config.py.
        """
        text = self.get_insult()
        self.post_tweet(text)

    def on_mention(self, tweet, prefix):
        """
        Defines actions to take when a mention is received.

        tweet - a tweepy.Status object. You can access the text with
        tweet.text

        prefix - the @-mentions for this reply. No need to include this in the
        reply string; it's provided so you can use it to make sure the value
        you return is within the 140 character limit with this.

        It's up to you to ensure that the prefix and tweet are less than 140
        characters.

        When calling post_tweet, you MUST include reply_to=tweet, or
        Twitter won't count it as a reply.
        """
        text = self.get_insult()
        prefixed_text = prefix + ' ' + text
        self.post_tweet(prefix + ' ' + text, reply_to=tweet)

        # call this to fav the tweet!
        # if something:
        #     self.favorite_tweet(tweet)

    def on_timeline(self, tweet, prefix):
        """
        Defines actions to take on a timeline tweet.

        tweet - a tweepy.Status object. You can access the text with
        tweet.text

        prefix - the @-mentions for this reply. No need to include this in the
        reply string; it's provided so you can use it to make sure the value
        you return is within the 140 character limit with this.

        It's up to you to ensure that the prefix and tweet are less than 140
        characters.

        When calling post_tweet, you MUST include reply_to=tweet, or
        Twitter won't count it as a reply.
        """

        """
        text = self.get_insult()
        prefixed_text = prefix + ' ' + text

        # let's only reply 70% of the time, otherwise fave the twutt
        def lucky(percent=70):
            return random.randrange(100) < percent

        if lucky():
            self.post_tweet(prefix + ' ' + text, reply_to=tweet)
        else:
            self.favorite_tweet(tweet)
        """
        pass

if __name__ == '__main__':
    bot = InsultBird()
    bot.run()
