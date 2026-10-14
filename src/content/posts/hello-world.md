---
title: "Getting your books out of Audible"
date: 2026-10-14
description: "Why it's so painful and how to make it less so"
---

As I was growing up, audio book were a fun way to make myself feel like I'm
learning English, and with my conscience quieted, embark on an afternoon of Call
of Duty. Now more than ten years later, audiobooks are a fun way of telling
myself I still "read" books (I forgot when was the last time when I spent more
than 30 minutes with an actual physical book).

## Audible

As almost every other audiobook fan, I have a love/hate relationship with
Audible. 

### Pros

* It exists
* It is fairly convenient for getting your poison of choice

### Cons

* You have to pay a subscription AND you have to buy the books that you have to
  buy beyond your free monthly credit
* You can download your books, but they don't make it obvious how to do that
* You can convert your books from the non-playable `.aax` format to something
  like `.m4b` , but it's not simple.

## Getting your books out of Audible

There are a number of ways to get your books out of Audible. Command line tools
such as `audible-rs` and `audible-cli` are one way, assuming you want to paste
your Amazon password into a command line tool, which I declined. Libation is
another alternative, assuming you're willing to put up with a horrendous UI and
UX that clearly doesn't care about you as a person. I managed to download and
export a few books after watching a YouTube tutorial, but who wants to deal with
that in 2026.

## Loudible

![Screenshot](<Screenshot 2026-10-14 at 23.13.34.png>)

Needless to say I had a yak to shave: creating a native macOS app that lets you
download books from Audible and export them, so that you can play them with an
audio player that's not Audible. That became [Loudible](https://github.com/bkrmendy/Loudible).

Loudible is still in development - signed app builds, a nice-looking `.dmg` and
basics like sorting and filtering are still to me implemented. It's only a few days away from release though! Famous last words.

Stay tuned!
