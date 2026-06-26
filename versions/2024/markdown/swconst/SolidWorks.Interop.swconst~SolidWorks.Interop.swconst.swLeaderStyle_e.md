---
title: "swLeaderStyle_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swLeaderStyle_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLeaderStyle_e.html"
---

# swLeaderStyle_e Enumeration

Leader styles.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swLeaderStyle_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swLeaderStyle_e
```

### C#

```csharp
public enum swLeaderStyle_e : System.Enum
```

### C++/CLI

```cpp
public enum class swLeaderStyle_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAlwaysAttachToBalloon | 0x1004 or 4100 = Bitmask ; applies only to balloon annotations; specifies that the balloon's Always Attach to Balloon leader option is enabled and the leader is always attached to the balloon when quantity is specified, and the balloon's Break Around leader option is disabled; if not specified, then the balloon's Always Attach to Balloon leader option is disabled, and the balloon's Break Around leader option is enabled and the balloon's leader is set to break around quantity; AND with one of the following options: swBENT swSTRAIGHT swUNDERLINED (parts only) swSPLINE (drawings only) swVDA |
| swAttachLeaderBottom | 0x400 or 1024 = Bitmask; in part's multiline note, attaches leader to bottom of note; AND with one of the following options: swBENT swSTRAIGHT swUNDERLINED |
| swAttachLeaderCenter | 0x200 or 512 = Bitmask; in a part's multiline note, attaches leader to center of note; AND with one of the following options: swBENT swSTRAIGHT swUNDERLINED |
| swAttachLeaderNearest | 0x800 or 2048 = Bitmask; in a part's multiline note, left leader attaches to the top of note and right leader attaches to the bottom of note; AND with one of the following options: swBENT swSTRAIGHT swUNDERLINED |
| swAttachLeaderTop | 0x100 or 256 = Bitmask; in a part's multiline note, attaches leader to top of note; AND with one of the following options: swBENT swSTRAIGHT swUNDERLINED |
| swBENT | 2 = Creates a bent leader |
| swNO_LEADER | 0 = No leader |
| swSPLINE | 4 = Creates a spline leader from a note; for drawings only |
| swSTRAIGHT | 1 = Creates a straight leader |
| swUNDERLINED | 3 = Creates an underlined leader; for parts only |
| swVDA | 8 = Creates an inspection leader |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
