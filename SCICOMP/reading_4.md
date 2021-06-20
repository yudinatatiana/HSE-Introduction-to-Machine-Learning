# Collaboration I

## Communications channels

### E-mail

#### Exercise: Write a simple RFC561-compliant e-mail.

```
From: tayudina_2@edu.hse.ru 
To: tayudina_2@edu.hse.ru
Date: 17 JUN 2021 1812-MSK 
Subject: Exercise
Hi!
```

#### Exercise: Send yourself an e-mail with non-ASCII characters. (E.g., "привет!") Download the raw message and open with a text editor. What are the contents? How is the message encoded, and where is the encoding specified? (Sometimes you need to select "view message source" or "view original message" to do this.)

Subject looks like "=?UTF-8?B?0J/RgNC40LzQtdGA?=" although I wrote "Пример"

Content-Type: text/html; charset=utf-8

Content-Transfer-Encoding: base64

#### Exercise: How are attachments handled? Refer to the Wikipedia article on MIME; send yourself an e-mail with a (very small!) attachment, and download the raw e-mail message and open with a text editor. What are the contents? Show and explain each MIME part. Can you recover the attachment from the raw message?

**MIME-Version: 1.0** - an indicator of MIME formatting

**Content-Type: image/jpeg; name="IMG_20210617_201001_resized_20210617_101054977.jpg"** - indicates the media type of the message content

**Content-Transfer-Encoding: base64** - Values 'quoted-printable' and 'base64' tell the email client that a binary-to-text encoding scheme was used and that appropriate initial decoding is necessary before the message can be read with its original encoding (e.g. UTF-8). 

**Content-Disposition: attachment; filename="IMG_20210617_201001_resized_20210617_101054977.jpg"; size=353900** - describes the attachment

### IRC

#### Exercise: Install an IRC client, log in to freenode.net, join #apertium and write a message "begiak: tell nlhowell hi". It will instruct the bot managing #apertium to forward me the message next time it sees me.

```
* Now talking on #apertium
<yudina> begiak: tell nlhowell hi
```

#### Exercise: Find a piece of software that you use which has an IRC channel for support. Ask a question there about the software. Include your conversation, and a brief description of your experiences.

For Ubuntu there are Ubuntu support channels. For example #ubuntu - Ubuntu help channel

### Matrix

#### Exercise: together with a friend, try out the Riot.im web client. How does it compare to IRC? To Telegram?

## Quality control

### Bug reports

#### Exercise: Both Python and the Linux kernel have considered in the past moving from bugzilla- and e-mail-based systems to forges. Read both articles, and summarise the advantages and disadvantages of forge-based systems and e-mail, and the results of each.

Advantages: Independace from large solution-providers and more flexible and suitable for big projects.

Disadvantages: It could be a very complicated for new users and it needs a lot of resources to work.

### Continuous integration

#### Exercise: Suppose your project is not software. What kinds of quality control tests might you implement? Give examples for written articles, web sites, musical compositions, and graphics.

written articles: checking the structure of the article, checking grammar and spelling errors, plagiarism check

web-sites: access verification, testing for the web-site's ability to withstand many users

musical compositions: plagiarism check, music genre check

graphics: checking for the presence of legend on the graphics

### Documentation

#### Exercise: install and run pandoc. (The dependencies are hefty.)

```
pandoc --version
pandoc 2.14.0.2
Compiled with pandoc-types 1.22, texmath 0.12.3, skylighting 0.10.5.1,
citeproc 0.4.0.1, ipynb 0.1.0.1
User data directory: C:\Users\yudin\AppData\Roaming\pandoc
Copyright (C) 2006-2021 John MacFarlane. Web:  https://pandoc.org
This is free software; see the source for copying conditions. There is no
warranty, not even for merchantability or fitness for a particular purpose.
```

```
pandoc --mathml
$x = y^2$
^D<p><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>x</mi><mo>=</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><annotation encoding="application/x-tex">x = y^2</annotation></semantics></math></p>
```
