
```
 **                           **   **         **      **             **
//                           /**  /**        /**     //             /**
 ** *******   ****** **   ** /** ******      /**      ** ******     /**
/**//**///** **//// /**  /** /**///**/       /****** /**//**//*  ******
/** /**  /**//***** /**  /** /**  /**        /**///**/** /** /  **///**
/** /**  /** /////**/**  /** /**  /**        /**  /**/** /**   /**  /**
/** ***  /** ****** //****** ***  //**  *****/****** /**/***   //******
// ///   // //////   ////// ///    //  ///// /////   // ///     ////// 

```

This is the source for [@insult-bird](https://twitter.com/insult_bird/with_replies), a Twitter
bot whose one sole purpose is to insult Twitter users in a particularly
pirate-y manner:



## Setup

### Note

Replace all instances of *insult-bird* in this project with the name of
your own bot to begin making use of this code for yourself.

Use `virtualenv` and `virtualenvwrapper` because Python is more fun with them.

Clone this repository, the change into its top level directory:

```
git clone https://github.com/brianshumate/insult-bird.git
cd insult-bird
```

Then, to quote the venerable @densoneold,

> commands

```
mkvirtualenv insult-bird
pip install -r requirements.txt
cp insult-bird/etc/access.json-dist insult-bird/etc/access.json
```

Finally, edit `etc/access.json` and plug in your Twitter API keys, tokens,
and secrets.

## Usage

Run it like this:

```
./insult-bird.py
```

## Thank You

- [Brent Woodruff](https://twitter.com/fprimex): Long time friend, Twitter bot collaborator and influence
- [@thricedotted](https://twitter.com/thricedotted): For their cool [twitterbot](https://github.com/thricedotted/twitterbot) framework that Robo Pirate uses! <3
- [Darius Kazemi](https://twitter.com/tinysubversions): Twitter bot artiste extraordinaire and constant inspiration
