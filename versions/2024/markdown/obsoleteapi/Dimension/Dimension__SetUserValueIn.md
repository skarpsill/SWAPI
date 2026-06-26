---
title: "Dimension::SetUserValueIn"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__SetUserValueIn.htm"
---

# Dimension::SetUserValueIn

This
method is obsolete and has been superseded by[Dimension.SetUserValueIn2](sldworksAPI.chm::/Dimension/Dimension_SetUserValueIn2.htm).

Description

This method sets the value of this dimension in the units of the specified
document.

Syntax (OLE Automation)

void
Dimension.SetUserValueIn ( doc, newValue)

(Table)=========================================================

| Input: | (LPDISPATCH)
doc | Dispatch
pointer to the document whose units you want to use |
| --- | --- | --- |
| Input: | (double)
newValue | Dimension
value in the units of the specified document, doc |

Syntax (COM)

status
= Dimension->ISetUserValueIn ( doc, newValue )

(Table)=========================================================

| Input: | (LPMODELDOC)
doc | Pointer to the document whose units you want to use |
| --- | --- | --- |
| Input: | (double)
newValue | Dimension
value in the units of the specified document, doc |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

This method allows you to change the value of a read-only dimension.
Use Dimension::ReadOnly to determine if a dimension is read-only.

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
<param name="Items" value="Dimension_Object$$**$$ZGetInfoDimension$$**$$ZModifyDimension$$**$$ZGetDimension$$**$$ZGetParameter$$**$$ZGetNames$$**$$ZModifyNames$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Dimension\Dimension__SetUserValueIn.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
