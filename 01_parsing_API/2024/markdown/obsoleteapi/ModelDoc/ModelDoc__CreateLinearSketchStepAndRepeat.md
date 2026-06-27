---
title: "ModelDoc::CreateLinearSketchStepAndRepeat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateLinearSketchStepAndRepeat.htm"
---

# ModelDoc::CreateLinearSketchStepAndRepeat

This
method is obsolete and has been superseded by[ModelDoc2::CreateLinearSketchStepAndRepeat](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreateLinearSketchStepAndRepeat.htm).

Description

This method creates linear sketch step-and-repeat.

Syntax (OLE Automation)

retval = ModelDoc.CreateLinearSketchStepAndRepeat
( num1, num2, spacing1, spacing2, angle1, angle2, deleteInstances )

(Table)=========================================================

| Input: | (long) num1 | Total number of instances along Direction1, including
the seed |
| --- | --- | --- |
| Input: | (long) num2 | Total number of instances along Direction2, including
the seed |
| Input: | (double) spacing1 | Spacing between elements along Direction1 |
| Input: | (double) spacing2 | Spacing between elements along Direction2 |
| Input: | (double) angle1 | Relative to the X axis, the angle for Direction1 |
| Input: | (double) angle2 | Relative to the X axis, the angle for Direction2 |
| Input: | (BSTR) deleteInstances | Instance numbers to delete passed as a string
in the format: "( a ) ( b ) ( c )
" |
| Return: | (BOOL) retval | TRUE if the sketch pattern was created successfully,
FALSE otherwise |

Syntax (COM)

status = ModelDoc->CreateLinearSketchStepAndRepeat
(num1, num2, spacing1, spacing2, angle1, angle2, deleteInstances, &retval
)

(Table)=========================================================

| Input: | (long) num1 | Total number of instances along Direction1, including
the seed |
| --- | --- | --- |
| Input: | (long) num2 | Total number of instances along Direction2, including
the seed |
| Input: | (double) spacing1 | Spacing between elements along Direction1 |
| Input: | (double) spacing2 | Spacing between elements along Direction2 |
| Input: | (double) angle1 | Relative to the X axis, the angle for Direction1 |
| Input: | (double) angle2 | Relative to the X axis, the angle for Direction2 |
| Input: | (BSTR) deleteInstances | Instance numbers to delete passed as a string
in the format: "( a ) ( b ) ( c )
" |
| Output: | (VARIANT_BOOL) retval | TRUE if the sketch pattern was created successfully,
FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__CreateLinearSketchStepAndRepeat.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
