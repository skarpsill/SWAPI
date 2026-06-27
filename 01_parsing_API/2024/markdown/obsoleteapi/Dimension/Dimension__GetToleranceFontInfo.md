---
title: "Dimension::GetToleranceFontInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__GetToleranceFontInfo.htm"
---

# Dimension::GetToleranceFontInfo

This method is obsolete and has been superseded
by[DimensionTolerance::GetFontUseDimension](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__GetFontUseDimension.htm),[DimensionTolerance::GetFontUseScale](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__GetFontUseScale.htm),[DimensionTolerance::GetFontScale](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__GetFontScale.htm),
and[DimensionTolerance::GetFontHeight](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__GetFontHeight.htm).

Description

This method gets the tolerance font information for this dimension.

Syntax (OLE Automation)

retval = Dimension.GetToleranceFontInfo
( )

(Table)=========================================================

| Return: | (VARIANT) retval | SafeArray of 3 doubles (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Dimension->IGetToleranceFontInfo
( retval )

(Table)=========================================================

| Output: | (double*) retval | Pointer to array of 3 doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns font information that contains
three values packed into an array of doubles:

[longuseFontScale, doubletolScale, doubletolHeight]

(Table)=========================================================

| useFontScale | TRUE if the tolerance font size is a scaled value of the dimension font
size |
| --- | --- |
| TolScale | Tolerance font size scale factor based on the dimension font size if useFontScale is TRUE |
| TolHeight | Tolerance height in meters if useFontScale is FALSE |

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
<param name="Items" value="Dimension_Object$$**$$ZDimTolerances$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Dimension\Dimension__GetToleranceFontInfo.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
