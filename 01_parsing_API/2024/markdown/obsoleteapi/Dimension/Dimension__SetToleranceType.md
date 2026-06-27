---
title: "Dimension::SetToleranceType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__SetToleranceType.htm"
---

# Dimension::SetToleranceType

This
method is obsolete and has been superseded by DimensionTolerance::Type .

Description

This
method sets the tolerance type of the dimension.

Syntax (OLE Automation)

retval
= Dimension.SetToleranceType ( newType )

(Table)=========================================================

| Input: | (long)
newType | Tolerance
type as defined in swTolType_e |
| --- | --- | --- |
| Return: | (BOOL)
retval | TRUE
if the tolerance type was set successfully, FALSE if it was not |

Syntax (COM)

status = Dimension->SetToleranceType
( newType, &retval )

(Table)=========================================================

| Input: | (long) newType | Tolerance type as defined in swTolType_e |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the tolerance type was set successfully, FALSE if it was not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\Dimension\Dimension__SetToleranceType.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}
