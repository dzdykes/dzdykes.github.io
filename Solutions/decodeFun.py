import string

#pass decoded message returns a encoded message
def encode(message, n):
    newMessage = ''
    mesArr = message.split(' ')
    for w in mesArr:
        for l in w:
            if ord(l) > 96 and ord(l) < 123:
                if ord(l) <= (96+n):
                    lnew = ord(l)+(26-n)
                else:
                    lnew = ord(l)-n
                newMessage += chr(lnew)
            else:
                newMessage += l
        newMessage += ' '
    return newMessage

#pass encoded message returns a decoded message
def decode(message, n):
    newMessage = ''
    mesArr = message.split(' ')
    #iterate through each word in the message and decode one by one
    for w in mesArr:
        #iterate through each letter in each word and decode one by one
        for l in w:
            if ord(l) > 96 and ord(l) < 123:
                if ord(l) >= (122-n):
                    lnew = ord(l)-(26-n)
                else:
                    lnew = ord(l)+n
                newMessage += chr(lnew)
            else:
                newMessage += l
        newMessage += ' '
    return newMessage
            
s = '''
Welcome to the jungle
We've got fun 'n' games
We got everything you want
Honey, we know the names
We are the people that can find
Whatever you may need
If you got the money, honey
We got your disease

[CHORUS:]

In the jungle
Welcome to the jungle
Watch it bring you to your
knees, knees
I wanna watch you bleed

Welcome to the jungle
We take it day by day
If you want it you're gonna bleed
But it's the price you pay
And you're a very sexy girl
That's very hard to please
You can taste the bright lights
But you won't get them for free
In the jungle
Welcome to the jungle
Feel my, my, my serpentine
I, I wanna hear you scream

Welcome to the jungle
It gets worse here everyday
Ya learn ta live like an animal
In the jungle where we play
If you got a hunger for what you see
You'll take it eventually
You can have anything you want
But you better not take it from me

[CHORUS]

And when you're high you never
Ever want to come down, YEAH!

You know where you are
You're in the jungle baby
You're gonna die
In the jungle
Welcome to the jungle
Watch it bring you to your
knees, knees
In the jungle
Welcome to the jungle
Feel my, my, my serpentine
In the jungle
Welcome to the jungle
Watch it bring you to your
knees, knees
In the jungle
Welcome to the jungle
Watch it bring you to your
It' gonna bring you down-HA!'''

