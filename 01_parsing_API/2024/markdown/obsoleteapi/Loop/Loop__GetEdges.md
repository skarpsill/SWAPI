---
title: "Loop::GetEdges"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Loop/Loop__GetEdges.htm"
---

# Loop::GetEdges

This method is obsolete and has been superseded by[Loop2::GetEdges](sldworksAPI.chm::/Loop2/Loop2__GetEdges.htm).

Description

This method returns all of the edges in the loop.

Syntax (OLE Automation)

retval = Loop.GetEdges ()

(Table)=========================================================

| Return: | (VARIANT) retval | SafeArray of dispatch pointers to all the edges that make up the loop |
| --- | --- | --- |

Syntax (COM)

status = Loop->IGetEdges ( &EdgeList
)

(Table)=========================================================

| Output: | (LPEDGE*) EdgeList | Pointer to the list of edges which make up the loop |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The edge objects are returned in a CW or CCW manner based on the direction
of the loop.

The loop direction is determined as follows: if a loop is viewed along
its direction, with the face normal pointing upwards, then the face that
owns the loop is to the left. This means that inner loops are CW and outer
loops are CCW. To determine if a loop is an outer loop, see[Loop::IsOuter](Loop__IsOuter.htm).

Because an edge is shared by multiple loops, the edge direction may
be opposite to the direction of the loop. To check this, see Edge::EdgeInFaceSense.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Loop_Object$$**$$ZGetEdge$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Loop\Loop__GetEdges.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZExample_Get_Circular_Holes_In_Face_Count$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Loop\Loop__GetEdges.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
