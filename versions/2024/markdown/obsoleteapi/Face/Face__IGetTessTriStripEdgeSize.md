---
title: "Face::IGetTessTriStripEdgeSize"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__IGetTessTriStripEdgeSize.htm"
---

# Face::IGetTessTriStripEdgeSize

This
method is obsolete and has been superseded by[Face2::IGetTessTriStripEdgeSize](sldworksAPI.chm::/Face2/Face2__IGetTessTriStripEdgeSize.htm).

Description

This method gets the size of the array returned
by Face::GetTessTriStripEdges.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Face->IGetTessTriStripEdgeSize ( &retval
)

(Table)=========================================================

| Output: | (long) retval | Size of the array returned by Face::GetTessTriStripEdges |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value from this method is the number of longs returned from
Face::GetTessTriStripEdges, which is (1 + NumStrips + EdgeCount).

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
<param name="Items" value="Face_Object$$**$$ZTessellation$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Face\Face__IGetTessTriStripEdgeSize.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
