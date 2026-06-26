---
title: "Dimension::SetSystemValue2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__SetSystemValue2.htm"
---

# Dimension::SetSystemValue2

This method is obsolete and has been superseded
by[Dimension::SetSytemValue3](sldworksAPI.chm::/Dimension/Dimension__SetSystemValue3.htm).

Description

This method sets the dimension value in system
units (meters) in the specified configurations.

Syntax (OLE Automation)

retval = Dimension.SetSystemValue2 ( newValue, allConfigs
)

(Table)=========================================================

| Input: | (double) newValue | Dimension value in meters |
| --- | --- | --- |
| Input: | (long) whichConfigs | Configurations in which to set this value as
defined in swSetValueInConfiguration_e |
| Return: | (long) retval | Success indicator value as defined in swSetValueReturnStatus_e |

Syntax (COM)

status = Dimension->SetSystemValue2 ( newValue,
allConfigs, retval, &retval )

(Table)=========================================================

| Input: | (double) newValue | Dimension value in meters |
| --- | --- | --- |
| Input: | (long) whichConfigs | Configurations in which to set this value as
defined in swSetValueInConfiguration_e |
| Output: | (long) retval | Success indicator value as defined in swSetValueReturnStatus_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The whichConfigs argument is equivalent to theChange Parameterdialog in the
SolidWorks user interface, which gives the user the option of having the
value set in all configurations or the current configuration. If there
is one configuration in the part, SolidWorks ignores this argument.

This method allows you to change the value of a
read-only dimension. You can use Dimension::ReadOnly to determine if a
dimension is read-only.

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
<param name="Items" value="Dimension_Object$$**$$ZGetInfoDimension$$**$$ZModifyDimension$$**$$ZGetDimension$$**$$ZGetParameter$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Dimension\Dimension__SetSystemValue2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic4
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
<param name="Items" value="EXDimMidTolerance$$**$$EXGearMateDimensions$$**$$EXModifyPlaneSystemValue$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Dimension\Dimension__SetSystemValue2.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
