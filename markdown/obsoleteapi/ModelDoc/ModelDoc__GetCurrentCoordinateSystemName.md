---
title: "ModelDoc::GetCurrentCoordinateSystemName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetCurrentCoordinateSystemName.htm"
---

# ModelDoc::GetCurrentCoordinateSystemName

This
method is obsolete and has been superseded by[ModelDoc2::GetCurrentCoordinateSystemName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetCurrentCoordinateSystemName.htm).

Description

This method returns the name of the current coordinate
system or an empty string for the default coordinate system.

Syntax (OLE Automation)

Name
=ModelDoc.GetCurrentCoordinateSystemName(
)

(Table)=========================================================

| Return: | (BSTR) Name | Name of the current coordinate system |
| --- | --- | --- |

Syntax (COM)

status
= ModelDoc->GetCurrentCoordinateSystemName( &Name )

(Table)=========================================================

| Output: | (BSTR) Name | Name of the current coordinate system |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The current coordinate system may be set by the user in theSave
Asdialog and in theTools, Measuredialog.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetCurrentCoordinateSystemName.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
