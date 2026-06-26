---
title: "Dimension::SetToleranceFontInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__SetToleranceFontInfo.htm"
---

# Dimension::SetToleranceFontInfo

This method is obsolete and has been superseded
by[DimensionTolerance::SetFont](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__SetFont.htm).

Description

This
method sets the tolerance font information.

Syntax (OLE Automation)

retval
= Dimension.SetToleranceFontInfo ( useFontScale, tolScale, tolHeight )

(Table)=========================================================

| Input: | (long)
useFontScale | TRUE
if the tolerance font size is a scaled value of the dimension font size |
| --- | --- | --- |
| Input: | (double)
tolScale | Tolerance
font size scale factor based on the dimension font size if useFontScale
is TRUE |
| Input: | (double)
tolHeight | Tolerance
height in meters if useFontScale is FALSE |
| Return: | (BOOL)
retval | TRUE if the values were set successfully, FALSE if they were not |

Syntax (COM)

status
= Dimension->SetToleranceFontInfo ( useFontScale, tolScale, tolHeight,
&retval )

(Table)=========================================================

| Input: | (long)
useFontScale | TRUE
if the tolerance font size is a scaled value of the dimension font size |
| --- | --- | --- |
| Input: | (double)
tolScale | Tolerance
font size scale factor based on the dimension font size if useFontScale
is TRUE |
| Input: | (double)
tolHeight | Tolerance
height in meters if useFontScale is FALSE |
| Output: | (VARIANT_BOOL)
retval | TRUE
if the values were set successfully, FALSE if they were not |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

For example, to use the dimension font size, set useFontScale to TRUE
and tolScale to 1.0

You cannot set tolerance values if the tolerance type is swTolNONE.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Dimension\Dimension__SetToleranceFontInfo.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
