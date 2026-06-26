---
title: "ModelDoc::PrintSetup"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__PrintSetup.htm"
---

# ModelDoc::PrintSetup

This
method is obsolete. Use ModelDoc2::SetUserPreferenceDoubleValue , ModelDoc2::SetUserPreferenceIntegerValue ,
and ModelDoc2::SetUserPreferenceToggle .

Description

This property gets and sets various parameters for the current SolidWorks
printer. The current SolidWorks printer can be determined or changed by
calling ModelDoc::ActivePrinter.

Syntax (OLE Automation)

setupValue = ModelDoc.PrintSetup(setupType) (VB
Get property)

ModelDoc.PrintSetup(setupType) = setupValue (VB
Set property)

setupValue = ModelDoc.GetPrintSetup
( setupType ) (C++ Get property)

ModelDoc.SetPrintSetup ( setupType,
setupValue ) (C++ Set property)

(Table)=========================================================

| Input: | (long)setupType | Type of property to set as defined in swPrintProperties_e |
| --- | --- | --- |
| Property: | (int) setupValue | Value for property |

Syntax (Com)

status = ModelDoc->get_PrintSetup(
setupType, &setupValue )

status = ModelDoc->put_PrintSetup(
setupType, setupValue )

(Table)=========================================================

| Input: | (long)setupType | Type of property to set as defined in swPrintProperties_e. |
| --- | --- | --- |
| Property: | (int) setupValue | Value for property |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

For information about values for the argument setupValue, see Visual
Basic online Help topics about printer object constraints.

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
<param name="Items" value="ModelDoc_Object$$**$$Zprinting$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__PrintSetup.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="PrintOut2_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__PrintSetup.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
