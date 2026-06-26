---
title: "Dimension::SetToleranceFitValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/Dimension__SetToleranceFitValues.htm"
---

# Dimension::SetToleranceFitValues

This method is obsolete and has been superseded
by[DimensionTolerance::SetFitValues](sldworksAPI.chm::/DimensionTolerance/DimensionTolerance__SetFitValues.htm).

Description

This
method sets the tolerance values for fit tolerances.

Syntax (OLE Automation)

retval
= Dimension.SetToleranceFitValues ( newLValue, newUValue )

(Table)=========================================================

| Input: | (BSTR)
newLValue | Lower
tolerance value (a single character) |
| --- | --- | --- |
| Input: | (BSTR)
newUValue | Upper
tolerance value (a single character) |
| Return: | (BOOL)
retval | TRUE
if the values were set successfully, FALSE if they were not |

Syntax (COM)

status
= Dimension->SetToleranceFitValues ( newLValue, newUValue, &retval
)

(Table)=========================================================

| Input: | (BSTR)
newLValue | Lower
tolerance value (a single character) |
| --- | --- | --- |
| Input: | (BSTR)
newUValue | Upper
tolerance value (a single character) |
| Output: | (VARIANT_BOOL)
retval | TRUE
if the values were set successfully, FALSE if they were not |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

You cannot set the tolerance values if the tolerance type is swTolNONE.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\DisplayDimension\Dimension__SetToleranceFitValues.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
