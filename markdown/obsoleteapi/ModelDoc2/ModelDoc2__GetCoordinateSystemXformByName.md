---
title: "ModelDoc2::GetCoordinateSystemXformByName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetCoordinateSystemXformByName.htm"
---

# ModelDoc2::GetCoordinateSystemXformByName

This
method is obsolete and has been superseded by[ModelDocExtension::GetCoordinateSystemTransformByName](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__GetCoordinateSystemTransformByName.htm).

Description

This method returns the inverse transform of the
specified coordinate system.

Syntax (OLE Automation)

retval
=ModelDoc2.GetCoordinateSystemXformByName(nameIn)

(Table)=========================================================

| Input: | (BSTR) nameIn | N ame of the coordinate system |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT containing a SafeArray of 16 doubles (see Remarks ) |

Syntax (COM)

status = ModelDoc2->IGetCoordinateSystemXformByName(
nameIn, xform )

(Table)=========================================================

| Input: | (BSTR) nameIn | Name of the coordinate system |
| --- | --- | --- |
| Output: | (double*) xform | Pointer to an array of 16 doubles (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The inverse transform is returned as an array of 16 elements:

- First 9 are elements of 3x3 matrix
- Next 3 define translation
- Next 1 is scaling
- Last 3 elements are not used

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__GetCoordinateSystemXformByName.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__GetCoordinateSystemXformByName.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
