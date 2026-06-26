---
title: "ModelDoc::GetCoordinateSystemXformByName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetCoordinateSystemXformByName.htm"
---

# ModelDoc::GetCoordinateSystemXformByName

This
method is obsolete and has been superseded by[ModelDoc2::GetCoordinateSystemXformByName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetCoordinateSystemXformByName.htm).

Description

This method gets the transform of the specified coordinate
system.

Syntax (OLE Automation)

retval
=ModelDoc.GetCoordinateSystemXformByName(nameIn)

(Table)=========================================================

| Input: | (BSTR) nameIn | N ame of the coordinate system |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT containing a SafeArray of 16 doubles |

Syntax (COM)

status
= ModelDoc->IGetCoordinateSystemXformByName( nameIn, xform )

(Table)=========================================================

| Input: | (BSTR) nameIn | Name of the coordinate system |
| --- | --- | --- |
| Output: | (double*) xform | P ointer to an array of 16 doubles |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The transform is returned as an array of 16 elements.
The first 9 are elements of 3x3 matrix, the next 3 define translation,
the next 1 is scaling. The last 3 elements are unused.

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZCoordinateSystem$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetCoordinateSystemXformByName.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
