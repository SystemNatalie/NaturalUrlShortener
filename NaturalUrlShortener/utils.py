from datetime import timedelta

from .models import ShortURL
import random
import datetime
random.seed(datetime.datetime.now().timestamp())
words = [
        # === NOUNS ===
        "ace", "act", "add", "ado", "aim", "air", "ale", "ant", "ark",
        "arm", "art", "ash", "axe", "bad", "bag", "ban", "bar", "bat", "bay",
        "bed", "bet", "bib", "bin", "bit", "bog", "boo", "bow", "box", "bud",
        "bug", "bun", "bus", "cab", "can", "cap", "car", "cat", "cob", "cod",
        "cog", "con", "cop", "cot", "cow", "cub", "cup", "dab", "dam", "day",
        "den", "dew", "dig", "dog", "dot", "dub", "dun", "dye", "ear", "eel",
        "egg", "elf", "elk", "elm", "emu", "end", "era", "eve", "eye",
        "fan", "fat", "fen", "fig", "fin", "fir", "fix", "flu", "fly", "fog",
        "fox", "fry", "fun", "fur", "gap", "gas", "gem", "gig", "gin", "gob",
        "god", "gum", "gun", "gut", "guy", "hag", "ham", "hat", "hay", "hem",
        "hen", "hip", "hog", "hub", "hue", "hug", "hum", "hut", "ice", "imp",
        "ink", "ion", "ire", "jam", "jar", "jaw", "jig", "job", "jug",
        "keg", "ken", "key", "kid", "kin", "kit", "lab", "lad", "lap", "law",
        "leg", "lid", "lip", "log", "lot", "lug", "lye", "man", "map", "mat",
        "maw", "men", "mob", "mop", "mud", "mug", "nag", "nap", "net", "nib",
        "nip", "nit", "nod", "nut", "oar", "oat", "oil", "orb", "ore", "owl",
        "pad", "pal", "pan", "pat", "paw", "peg", "pen",

        # === VERBS ===
        "ask", "axe", "beg", "bid", "bow", "box", "buy", "can", "cap", "cut",
        "dam", "dig", "dip", "dry", "due", "dye", "eat", "ebb", "end", "fan",
        "fit", "fix", "fly", "fry", "get", "gig", "got", "had", "has", "hat",
        "hew", "hid", "hit", "hop", "how", "hug", "jut", "ken", "key", "kid",
        "lay", "led", "let", "lie", "lit", "log", "lot", "low", "mix",
        "mow", "nab", "nap", "nod", "not", "now", "owe", "own", "pay", "peg",
        "pen", "pet", "pop", "put", "run", "say", "see", "set", "sit", "sob",
        "sow", "tan", "tap", "tie", "tip", "top", "tug", "use", "wag", "win",
        "wow", "yap", "yaw", "yell", "zap", "zip",

        # === ADJECTIVES ===
        "apt", "bad", "big", "bold", "calm", "cool", "coy", "dim", "dry", "dull",
        "fat", "few", "fit", "hot", "ill", "jolly", "keen", "kind", "lame", "lean",
        "long", "loud", "low", "mad", "mean", "new", "odd", "old", "pale", "poor",
        "proud", "quick", "rare", "real", "ripe", "rude", "sad", "safe", "sane", "shy",
        "sly", "soft", "sore", "sour", "tall", "tame", "tart", "tidy", "tiny", "ugly",
        "vain", "vast", "warm", "weak", "wet", "wide", "wild", "wise", "wry", "young",
        "zany",

        # === ADVERBS ===
        "ago", "all", "as", "down", "even", "far", "fast", "how", "just", "late",
        "less", "more", "most", "much", "near", "now", "off", "once", "only", "out",
        "over", "quite", "so", "then", "thus", "too", "up", "very", "well", "yet",
    ]
def generate_urls(urlLen=3, tries=10):                                                                                  # Try to generate a URL OR return false after a number of  tries.
    shortURL= "".join([x.title() for x in random.sample(words, urlLen)])
    tries=tries
    while ShortURL.objects.filter(short_URL=shortURL).exists():                                                         # Keep generating short URLs until we get an unused one
        shortURL = "".join([x.title() for x in random.sample(words, urlLen)])
        tries=tries-1
        if tries==0:                                                                                                    # Failed after "tries" number of attempts to generate
                return False
    return shortURL

def wipe_old_short_urls(wipeDays=7):                                                                                    # Does what it says on the tin. Gets all ShortURLs older than 7 day and wipes them.
        for i in ShortURL.objects.filter(date_modified__lte=datetime.datetime.now()-timedelta(days=wipeDays)):
                i.delete()