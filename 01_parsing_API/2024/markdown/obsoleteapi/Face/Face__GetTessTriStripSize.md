---
title: "Face::GetTessTriStripSize"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTessTriStripSize.htm"
---

# Face::GetTessTriStripSize

This
method is obsolete and has been superseded by[Face2::GetTessTriStripSize](sldworksAPI.chm::/Face2/Face2__GetTessTriStripSize.htm).

Description

This method gets the necessary array size for allocation with Face::GetTessTriStrips.

Syntax (OLE Automation)

retval
= Face.GetTessTriStripSize ()

(Table)=========================================================

| Return: | (long)
retval | Size of the array returned by Face::GetTessTriStrips |
| --- | --- | --- |

Syntax (COM)

status
= Face->GetTessTriStripSize ( &retval )

(Table)=========================================================

| Output: | (long)
retval | Size
of the array returned by Face::GetTessTriStrips |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

The return value from this method is the number of floats returned by
Face::GetTessTriStrips, which is (1 + NumStrips + 3 * VertexCount).

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Face\Face__GetTessTriStripSize.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
