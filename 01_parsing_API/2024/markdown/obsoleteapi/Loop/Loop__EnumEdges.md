---
title: "Loop::EnumEdges"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Loop/Loop__EnumEdges.htm"
---

# Loop::EnumEdges

This method is obsolete and has been superseded by[Loop2::EnumEdges](sldworksAPI.chm::/Loop2/Loop2__EnumEdges.htm).

Description

This method enumerates the edges in a face.

Syntax (OLE Automation)

See Loop::GetEdges.

Syntax (COM)

status = Loop->EnumEdges ( &retval
)

(Table)=========================================================

| Output: | (LPENUMEDGES) retval | Pointer to the enumerated list of edges |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The edge objects are returned in a CW or CCW manner based on the direction
of the loop.

The loop direction is determined as follows: if a loop is viewed along
its direction with the face normal pointing upwards, then the face that
owns the loop is to the left. This means that inner loops are CW and outer
loops are CCW. To determine if a loop is an outer loop, see Loop::IsOuter.

Because an edge is shared by multiple loops, the edge direction might
be opposite to the direction of the loop. To check this, use Edge::EdgeInFaceSense.

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
<param name="Items" value="Loop_Object$$**$$ZGetEdge$$**$$ZGetEnumEdges$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\sw2003\Loop\Loop__EnumEdges.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
