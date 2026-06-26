---
title: "Bitmasks"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Bitmasks.htm"
---

# Bitmasks

A Bitmask is a set of binary representations of decimal numbers. Some
SOLIDWORKS enumerators are bitmasks that enable you to turn on multiple options
simultaneously. Two or more options in a bitmask are enabled by simply adding
their values together.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For example, if a SOLIDWORKS enumerator has a bitmask like the following:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

(Table)=========================================================

| Decimal | Option | Binary |
| --- | --- | --- |
| 1 | OptionA | 0001 |
| 2 | OptionB | 0010 |
| 4 | OptionC | 0100 |
| 8 | OptionD | 1000 |

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

and you want OptionA and OptionC on, then add their two values together:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

(Table)=========================================================

| Decimal | Option | Binary |
| --- | --- | --- |
| 1 | OptionA | 0001 |
| + 4 | OptionC | 0100 |
| = 5 |  | 0101 |

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}
