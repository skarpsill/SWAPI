---
title: "Dimension::SetValue2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__SetValue2.htm"
---

# Dimension::SetValue2

This method is obsolete and has been superseded
by[Dimension::SetValue3](sldworksAPI.chm::/Dimension/Dimension__SetValue3.htm).

Description

This method sets the value of the current dimension.

Syntax (OLE Automation)

retval = Dimension.SetValue2
( newValue, whichConfigs )

(Table)=========================================================

| Input: | (double) newValue | Value for this dimension in the units of owning
document |
| --- | --- | --- |
| Input: | (long) whichConfigs | Configurations in which to set this value as
defined in swSetValueInConfiguration_e |
| Return: | (long) retval | Success indicator as defined in swSetValueReturnStatus_e |

Syntax (COM)

status = Dimension->SetValue2 (newValue, whichConfigs,&retval )

(Table)=========================================================

| Input: | (double) newValue | Value for this dimension in the units of the
owning document |
| --- | --- | --- |
| Input: | (long) whichConfigs | Configurations in which to set this value in
as defined swSetValueInConfiguration_e |
| Output: | (long) retval | Success indicator as defined in swSetValueReturnStatus_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You must specify the value in the user units taken
from the document in which the dimension was created.

When you use this method to create a dimension
in a part, you must specify the new value in the units of the original
part. For example, if the part is in millimeters, then you must specify
millimeters in any call to this method. If that part is brought into a
drawing which is in inches and the model dimension is inserted into one
of the drawing views, then you must still specify the dimension value
in millimeters. If the original part is changed to inches, then calls
to this method must specify the dimension in inches. Use Dimension::SetSystemValue2
to determine avoid this issue.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Dimension\Dimension__SetValue2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
