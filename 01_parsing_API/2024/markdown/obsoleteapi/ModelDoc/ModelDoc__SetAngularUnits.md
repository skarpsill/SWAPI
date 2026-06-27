---
title: "ModelDoc::SetAngularUnits"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetAngularUnits.htm"
---

# ModelDoc::SetAngularUnits

This
method is obsolete and has been superseded by[ModelDoc2::SetAngularUnits](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetAngularUnits.htm).

Description

This method sets the current angular units.

Syntax (OLE Automation)

void ModelDoc.SetAngularUnits ( uType,
fractBase, fractDenom, sigDigits)

(Table)=========================================================

| Input: | (short) uType | Angular units as defined in swAngleUnit_e |
| --- | --- | --- |
| Input: | (short) fractBase | Not used; input to this field is required, but is not used |
| Input: | (short) fractDenom | Not used; input to this field is required but is not used |
| Input: | (short) sigDigits | Significant digits if using decimal units |

Syntax (COM)

status = ModelDoc->SetAngularUnits
( uType, fractBase, fractDenom, sigDigits )

(Table)=========================================================

| Input: | (short) uType | Angular units as defined in swAngleUnit_e |
| --- | --- | --- |
| Input: | (short) fractBase | Not used; input to this field is required but is not used |
| Input: | (short) fractDenom | Not used; input to this field is required but is not used |
| Input: | (short) sigDigits | Significant digits if using decimal units |
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZSetInfoUserPreference$$**$$ZGetSetAngularUnits$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetAngularUnits.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
