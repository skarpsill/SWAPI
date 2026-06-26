---
title: "View::GetDimensionString2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionString2.htm"
---

# View::GetDimensionString2

This method is obsolete and has been superseded
by[View::GetDimensionString3](View__GetDimensionString3.htm).

Description

This method returns an array of strings containing the text associated
with each dimension in the view. Use View::GetDimensionCount2 to determine
the number of strings to be returned.

Syntax (OLE Automation)

retval = View.GetDimensionString2 ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing the text associated with each dimension |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionString2
( retval )

(Table)=========================================================

| Output: | (BSTR*) retval | Text associated with each dimension |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is identical to View::GetDimensionString except when a base
ordinate is not visible, the subordinates were not previously output,
whether they were visible or not. With this method, the output of each
visbile subordinate occurs whether or not its base ordinate is visible.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="View_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\View\View__GetDimensionString2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
