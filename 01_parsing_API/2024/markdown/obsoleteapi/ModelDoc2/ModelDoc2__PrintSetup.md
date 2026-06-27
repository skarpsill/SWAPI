---
title: "ModelDoc2::PrintSetup"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__PrintSetup.htm"
---

# ModelDoc2::PrintSetup

This
method is obsolete and has been superseded by ModelDoc2::SetUserPreferenceDoubleValue , ModelDoc2::SetUserPreferenceIntegerValue ,
and ModelDoc2::SetUserPreferenceToggle .

Description

This property gets and sets various parameters
for the current SolidWorks printer.

Syntax (OLE Automation)

setupValue = ModelDoc2.PrintSetup(setupType) (VB
Get property)

ModelDoc2.PrintSetup(setupType) = setupValue (VB
Set property)

setupValue = ModelDoc2.GetPrintSetup
( setupType ) (C++ Get property)

ModelDoc2.SetPrintSetup ( setupType,
setupValue ) (C++ Set property)

(Table)=========================================================

| Input: | (long)setupType | Type of property to set as defined in swPrintProperties_e |
| --- | --- | --- |
| Property: | (int) setupValue | Value for property |

Syntax (Com)

status = ModelDoc2->get_PrintSetup(
setupType, &setupValue )

status = ModelDoc2->put_PrintSetup(
setupType, setupValue )

(Table)=========================================================

| Input: | (long)setupType | Type of property to set as defined in swPrintProperties_e |
| --- | --- | --- |
| Property: | (int) setupValue | Value for property |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can use SldWorks::ActivePrinter
to determine or change the current SolidWorks printer.

For information about values for the argument setupValue, see the MSDEV
or Visual Basic Help.

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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc2\ModelDoc2__PrintSetup.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc2\ModelDoc2__PrintSetup.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
