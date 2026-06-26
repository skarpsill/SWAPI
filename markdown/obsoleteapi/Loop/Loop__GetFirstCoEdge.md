---
title: "Loop::GetFirstCoEdge"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Loop/Loop__GetFirstCoEdge.htm"
---

# Loop::GetFirstCoEdge

This method is obsolete and has been superseded by[Loop2::GetFirstCoEdge](sldworksAPI.chm::/Loop2/Loop2__GetFirstCoEdge.htm).

Description

This method returns the first coedge of the loop.

Syntax (OLE Automation)

retval = Loop.GetFirstCoEdge ()

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the coedge |
| --- | --- | --- |

Syntax (COM)

status = Loop->IGetFirstCoEdge (
&retval )

(Table)=========================================================

| Output: | (LPCOEDGE) retval | Pointer to the coedge |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The CoEdge objects are returned in a CW or CCW manner based on the direction
of the loop.

The loop direction is determined as follows: if a loop is viewed along
its direction, with the face normal pointing upwards, then the face that
owns the loop is to the left. This means that inner loops are CW and outer
loops are CCW. To determine if a loop is an outer loop, see[Loop::IsOuter](Loop__IsOuter.htm).

The coedge direction always aligns with the direction
of the loop.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Loop_Object$$**$$ZGetCoEdge$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Loop\Loop__GetFirstCoEdge.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
