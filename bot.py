# Natural Language Toolkit 
from nltk_lite.chat import Chat, reflections

pairs = (
    (r'boleh',
     ("namamu siapa ?",
      )),

    (r'nama saya(.*)',
     ("ohh %1, nama mu bagus juga ?he...he...",
      "%1? namanya familiar, kepanjangannya apa ?",)),

    (r'kepanjangannya namaku(.*)',
     ("%1 ? apa nama tersebut merupakan nama ortu mu ?",
      "%1, nama yang keren !!!",)),

    (r'terima kasih|thank|thanks',
     ("sama - sama",)),

    (r'benar|betul',
     (" nama yang bagus",
      )),

    (r'senang berkenalan dengan anda',
     ("terima kasih sudah bergabung dengan saya",
      )),

    (r'sampai jumpa lagi',
     ("terima kasih",
      )),

    (r'(.*)',
     (" bisa katakan yang lainnya ?",
      "maaf, saya tidak mengerti apa yang anda katakan ! apa jenis makanan lainnya yang anda sukai ?",
      ))
    )

rizky = Chat(pairs, reflections)

def demo():
    print "Program chat tentang masakan"
    print 'Tekan "quit" untuk mengakhiri chat'
    print '=' *72
    print "Hai, kenalan donk ?"
    s = ""
    while s != "quit":
        s = "quit"
        try: s = raw_input(">")
        except EOFError:
            print s
        if s:
            while s[-1] in "!.": s = s[:-1]
            print rizky.respond(s)

if __name__ == "__main__":
    demo()
