---
title: "Edge::GetTwoAdjacentFaces"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Edge/Edge__GetTwoAdjacentFaces.htm"
---

# Edge::GetTwoAdjacentFaces

This method is obsolete and has been superseded by[Edge::GetTwoAdjacentFaces2](sldworksAPI.chm::/Edge/Edge__IGetTwoAdjacentFaces2.htm).

Description

This method returns the two adjacent faces to an edge.

Syntax (OLE Automation)

retval
= Edge.GetTwoAdjacentFaces ()

(Table)=========================================================

| Return: | (VARIANT)
retval | VARIANT
containing a SafeArray of two Dispatch pointers to the two faces |
| --- | --- | --- |

Syntax (COM)

status
= Edge->IGetTwoAdjacentFaces ( &face1, &face2 )

(Table)=========================================================

| Output: | (LPFACE)
face1 | Pointer
to the first adjacent face |
| --- | --- | --- |
| Output: | (LPFACE)
face2 | Pointer
to the second adjacent face |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

Call this method for body-related edges, not reference
curve or sketch edges.

This method returns two faces only if the body
is a solid body. If it is not, then the Dispatch version returns VT_EMPTY
and the COM version returns S_FALSE.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Edge_Object$$**$$ZGetFac$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Edge\Edge__GetTwoAdjacentFaces.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
