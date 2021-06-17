# Computer Architecture I

## Ideas of electronics

### Interlude: review of logic

#### Exercise: Compute the truth table for NOT:

X | NOT X
--|-------
0 |1
1 |0

#### Exercise: Compute the truth table table for AND.

X | Y | X AND Y
--|---|--------
0 | 0 |   0
0 | 1 |   0
1 | 0 |   0
1 | 1 |   1

#### Exercise: Compute the truth table for exclusive-or, defined by the formula:

XOR(X, Y) = (X OR Y) AND NOT (X AND Y)

X | Y | A = X AND Y | B = X OR Y | NOT A | XOR(X, Y) = B AND NOT A
--|---|-------------|------------|-------|-------------------------
0 | 0 |      0      |      0     |   1   |     0
0 | 1 |      0      |      1     |   1   |     1
1 | 0 |      0      |      1     |   1   |     1
1 | 1 |      1      |      1     |   0   |     0

#### Exercise: Prove De Morgan's theorem, NOT(X OR Y) = NOT(X) AND NOT(Y), by completing the table and checking the last two columns are the same.

X | Y | A = X OR Y | B = NOT X | C = NOT Y | NOT A | B AND C
--|---|------------|-----------|-----------|-------|---------
0 | 0 |      0     |     1     |     1     |   1   |    1
0 | 1 |      1     |     1     |     0     |   0   |    0
1 | 0 |      1     |     0     |     1     |   0   |    0
1 | 1 |      1     |     0     |     0     |   0   |    0

#### Exercise: using truth tables, check these three equations

NOT(X) = NAND(1, X) = NOT(1 AND X)

X | Y | NOT(X) | A = 1 AND X | NOT A = NAND(1, X)
--|---|--------|-------------|-------------------
0 | 0 |    1   |       0     |         1
0 | 1 |    1   |       0     |         1
1 | 0 |    0   |       1     |         0
1 | 1 |    0   |       1     |         0

AND(X, Y) = NOT(NAND(X, Y)) = NOT(NOT(X AND Y))

X | Y | A = X AND Y | B = NOT A | NOT B = NOT(NAND(X, Y))
--|---|-------------|-----------|------------------------
0 | 0 |      0      |     1     |           0
0 | 1 |      0      |     1     |           0
1 | 0 |      0      |     1     |           0
1 | 1 |      1      |     0     |           1

OR(X, Y) = NAND(NOT(X), NOT(Y))) = NOT(NOT(X) AND NOT(Y))

X | Y | A = NOT X | B = NOT Y | C = A AND B | NOT C = NAND(NOT(X), NOT(Y))) | X OR Y
--|---|-----------|-----------|-------------|-------------------------------|--------
0 | 0 |     1     |     1     |      1      |                0              |   0
0 | 1 |     1     |     0     |      0      |                1              |   1
1 | 0 |     0     |     1     |      0      |                1              |   1
1 | 1 |     0     |     0     |      0      |                1              |   1

#### Exercise: write similar formulas expressing NOT, AND, and OR in terms of NOR

NOT(X) = NOR(0,X)

X | A = 0 OR X | NOT A | NOT X
--|------------|-------|-------
0 |     0      |1      |1
1 |     1      |0      |0

AND(X,Y) = NOR(NOR(0,X),NOR(0,Y)))

X | Y | A = NOR(0,X) | B = NOR(0,Y) | NOR(A,B) | X AND Y
--|---|--------------|--------------|----------|---------
0 | 0 |1             |1             |0         |0
0 | 1 |1             |0             |0         |0
1 | 0 |0             |1             |0         |0
1 | 1 |0             |0             |1         |1

OR(X,Y) = NOR(NOR(0, NOR(0, X)), NOR(0, NOR(0, Y)))

X | Y | A = NOR(0,X) | B = NOR(0,Y) | C = NOR(0, A) | D = NOR(0, B) | NOR(C, D)
--|---|--------------|--------------|---------------|---------------|----------
0 | 0 |1             |1             |0              |0              |0
0 | 1 |1             |0             |0              |1              |0
1 | 0 |0             |1             |1              |0              |0
1 | 1 |0             |0             |1              |1              |1

#### Exercise: why NOT and OR can't be expressed in terms of AND? Explain.'

Try:

NOT(X) = AND(0,X) 

NOT(X) = AND(1,X)

X | NOT(X) | AND(0,X)
--|--------|---------
0 |1       |0
1 |0       |0

X | NOT(X) | AND(1,X)
--|--------|---------
0 |1       |0
1 |0       |1

Try:

OR(X,Y) = AND(AND(0, X), AND(0, Y))

OR(X,Y) = AND(AND(0, X), AND(1, Y))

OR(X,Y) = AND(AND(1, X), AND(1, Y))

X | Y | A = AND(0, X) | B = AND(0, Y) | AND(A, B) | OR(X, Y)
--|---|---------------|---------------|-----------|----------
0 | 0 |0              |0              |0          |0
0 | 1 |0              |0              |0          |1
1 | 0 |0              |0              |0          |1
1 | 1 |0              |0              |0          |1

X | Y | A = AND(0, X) | B = AND(1, Y) | AND(A, B) | OR(X, Y)
--|---|---------------|---------------|-----------|----------
0 | 0 |0              |0              |0          |0
0 | 1 |0              |1              |0          |1
1 | 0 |0              |0              |0          |1
1 | 1 |0              |1              |0          |1

X | Y | A = AND(1, X) | B = AND(1, Y) | AND(A, B) | OR(X, Y)
--|---|---------------|---------------|-----------|----------
0 | 0 |0              |0              |0          |0
0 | 1 |0              |1              |0          |1
1 | 0 |1              |0              |0          |1
1 | 1 |1              |1              |1          |1

### Binary numbers as lists of boolean values

#### Exercise: Without listing explicitly, how many possible 8-bit binary numbers are there?

2^7 = 256

#### Exercise: Convert X = 110 to decimal.

0 \* 2^0 + 1 \* 2^1 + 1 \* 2^2 = 2 + 4 = 6

#### Exercise: Convert 11 to binary.

11 / 2 = 5 modulo 1

5 / 2 = 2 modulo 1

2 / 2 = 1 modulo 0

1 / 2 = 0 modulo 1

11 -> 1011

#### Exercise: Convert these powers of 2 into binary: 2, 4, 8, 16, 32. What do you notice?

2 = 10

4 = 100

8 = 1000

16 = 10000

32 = 100000

A new binary bit is added

#### Exercise: Convert these numbers into binary: 1, 3, 7, 15, 31 (they are all 2^n - 1 for some n). What do you notice?

1 = 1

3 = 11

7 = 111

15 = 1111

31 = 11111

These numbers are one less than the nearest greater power of two. They can be obtained by subtracting one from a power of two, or simply remember that there is one less digit in them and all the digits are filled with ones

#### Exercise: check that these numbers all have the same 3-bit representation: 3 = 11 = 17, 0 = 8 = 16, 2 = 10 = 18.

3 = **011**

11 = 1**011**

17 = 10001

3 = 11 != 17



0 = **000**

8 = 1**000**

16 = 10**000**

0 = 8 = 16


2 = **010**

10 = **010**10

18 = 10**010**

2 = 10 = 18

### Binary arithmetic as logical operations

#### Exercise: complete the table by converting 2 into single-bit binary:

X0 | Y0 | Z0
---|----|----
0  | 0  | 0
1  | 0  | 1
0  | 1  | 1
1  | 1  | 0

#### Exercise: do the same for single-bit multiplication: write down the table of binary numbers for X0, Y0, and the binary representation of their product Z0, and find the logical operation which matches. We say this operation implements single-bit multiplication.

X0 | Y0 | Z0
---|----|----
0  | 0  | 0
1  | 0  | 0
0  | 1  | 0
1  | 1  | 1

AND = implements single-bit multiplication

### Digital Logic

#### Exercise: Using A and B as the inputs, and OUT as the output, explain how this circuit acts as NAND(A,B); for each entry in the truth table, follow the explanation above. True is "high energy" and False is "low energy".

A | B | NAND(A,B)
--|---|----------
0 | 0 | 1
0 | 1 | 1
1 | 0 | 1
1 | 1 | 0

### Exercise: Using A and B as the inputs, and OUT as the output, explain how this circuit acts as NAND(A,B); for each entry in the truth table, follow the explanation above. True is "high energy" and False is "low energy".

 A |  B | NAND(A,B) |
---|----|-----------|
0  | 0  | 1         | both gates were unpowered, so electrons lost a lot of energy
1  | 0  | 1         | one of the gates was unpowered, so electrons lost energy
0  | 1  | 1         | one of the gates was unpowered, so electrons lost energy
1  | 1  | 0         | both gates were powered, so electrons didn't lose any energy

## Networking

### Name resolution and Routing

#### Exercise: show that every IPv4 can be represented by four 8bit unsigned integers, and that every 8bit unsigned integer is between 0 and 255.

IPv4 = XXXXXXXX.XXXXXXXX.XXXXXXXX.XXXXXXXX is 32-bit number = 4 \* 8

Every XXXXXXXX could be from 00000000 to 11111111 (form 0 to 255)

#### Exercise: how many IPv4 addresses are there? Is it enough? Explain.

2^32 = 4294967296 addresses. I think this is not enough given how fast the Internet is growing.

#### Exercise: use ping in a terminal to resolve a domain name. Copy-paste the command you used, and the result.

**Command:** ping yandex.ru

**Result:** Обмен пакетами с yandex.ru [77.88.55.88] с 32 байтами данных:

Ответ от 77.88.55.88: число байт=32 время=10мс TTL=247

Ответ от 77.88.55.88: число байт=32 время=12мс TTL=247

Ответ от 77.88.55.88: число байт=32 время=11мс TTL=247

Ответ от 77.88.55.88: число байт=32 время=11мс TTL=247


Статистика Ping для 77.88.55.88:

    Пакетов: отправлено = 4, получено = 4, потеряно = 0
    
    (0% потерь)
    
Приблизительное время приема-передачи в мс:

    Минимальное = 10мсек, Максимальное = 12 мсек, Среднее = 11 мсек

### Bandwidth, latency, reliability

#### Exercise: The Multipath TCP project aims to allow TCP packets to be split across multiple network links and reassembled at the destination. For example, if you were uploading a 100 megabyte file to a server from your phone, it would allow you to send 75 megabytes by WiFi and 25 megabytes by cellular automatically. How should the ratio be chosen if you want to minimise transmission time? Minimise cellular bandwidth use? Explain.

You need to look at the ratio of the data transfer rate through Wi-Fi and through the mobile Internet. If the transmission speed of Wi-Fi is 2 times higher than the transmission speed over the mobile Internet, then using Wi-Fi you need to transfer 2 times more data than using the mobile Internet.

To minimize the mobile network, you either need to send nothing through it, or send data less than 1/3, as I suggested above

#### Exercise: UDP is popular for streaming media; explain why.

UDP is faster and offers lower latency, which is important for streaming media.

#### Exercise: Read the Wikipedia articles on multicast and anycast routing. Why is anycast good for content delivery networks, and why is multicast good for live-streaming? What are some other uses for these?

Anycast sends data to the closest recipients, which allows for fast data transfers, which is why it is good for content delivery networks.

Multicast requires the source to send a packet once, which allows for more efficient use of the network infrastructure. Therefore, this type of data transfer is good for real-time streaming. 
