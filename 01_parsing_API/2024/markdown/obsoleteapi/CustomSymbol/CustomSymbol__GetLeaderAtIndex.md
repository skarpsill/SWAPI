---
title: "CustomSymbol::GetLeaderAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetLeaderAtIndex.htm"
---

# CustomSymbol::GetLeaderAtIndex

This method is obsolete and has been superseded
by[Note::GetLeaderAtIndex](sldworksAPI.chm::/Note/Note__GetLineAtIndex.htm).

Description

This
method gets information about the specified leader on this symbol.

Syntax (OLE Automation)

retval
= CustomSymbol.GetLeaderAtIndex ( index )

(Table)=========================================================

| Input: | (long)
index | Index
of leader |
| --- | --- | --- |
| Return: | (VARIANT)
retval | VARIANT
of type SafeArray (see below) |

Syntax (COM)

status
= CustomSymbol->IGetLeaderAtIndex ( index, &PointCount, retval
)

(Table)=========================================================

| Input: | (long)
index | Index
of leader |
| --- | --- | --- |
| Output: | (long)
PointCount | Number
of (x,y,z) points being returned in the array |
| Output: | (double*)
retval | Pointer
to array of doubles (see below) |
| Return: | (HRESULT)
status | S_OK
if Successful |

Remarks

The leader line might use 0, 1 or 2 lines. If the CustomSymbol is not
attached, there are 0 lines; a straight leaderline is 1 line, and a bent
leaderline is 2 lines. You must infer the number of leader lines based
on IsAttached() and HasExtraLeader().

IsAttached() == FALSE implies no leaderline
and there are therefore no leaderline points (PointCount=0).

HasExtraLeader() == FALSE means that this
is a straight leaderline and there will therefore be 1 line (PointCount=2)

HasExtraLeader() == TRUE means that this
is a bent leaderline and there will therefore be 2 lines (PointCount=3)

The return value uses the following format:

retval[0]
= X-coord of first leader point

retval[1]
= Y-coord of first leader point

retval[2]
= Z-coord of first leader point

retval[3]
= X-coord of second leader point

retval[4]
= Y-coord of second leader point

retval[5]
= Z-coord of second leader point

retval[6]
= X-coord of third leader point

retval[7]
= Y-coord of third leader point

retval[8]
= Z-coord of third leader point

Use[CustomSymbol::GetLeaderCount](CustomSymbol__GetLeaderCount.htm)to determine how many leaders are on the CustomSymbol object.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="CustomSymbol_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\CustomSymbol\CustomSymbol__GetLeaderAtIndex.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
