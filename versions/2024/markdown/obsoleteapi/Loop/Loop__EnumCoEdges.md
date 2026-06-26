---
title: "Loop::EnumCoEdges"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Loop/Loop__EnumCoEdges.htm"
---

# Loop::EnumCoEdges

This
method is obsolete and has been superseded by[Loop2::EnumCoEdges](sldworksAPI.chm::/Loop2/Loop2__EnumCoEdges.htm).

Description

This method enumerates the coedges in a loop.

Syntax (OLE Automation)

See Loop::GetFirstCoEdge.

Syntax (COM)

status
= Loop->EnumCoEdges ( &retval )

(Table)=========================================================

| Output: | (LPENUMCOEDGES)
retval | Pointer
to the enumerated list of coedges |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

The CoEdge objects are returned in a CW or CCW manner based on the direction
of the loop.

The loop direction is determined as follows: if a loop is viewed along
its direction with the face normal pointing upwards, then the face that
owns the loop is to the left. This means that inner loops are CW and outer
loops are CCW. To determine if a loop is an outer loop, use Loop::IsOuter.

The coedge direction
always aligns with the direction of the loop.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Loop_Object$$**$$ZGetCoEdge$$**$$ZGetEnumCoEdges$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Loop\Loop__EnumCoEdges.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
