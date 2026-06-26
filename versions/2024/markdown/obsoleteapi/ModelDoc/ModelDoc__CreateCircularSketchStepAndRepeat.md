---
title: "ModelDoc::CreateCircularSketchStepAndRepeat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateCircularSketchStepAndRepeat.htm"
---

# ModelDoc::CreateCircularSketchStepAndRepeat

This
method is obsolete and has been superseded by[ModelDoc2::CreateCircularSketchStepAndRepeat](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreateCircularSketchStepAndRepeat.htm).

Description

This method creates circular sketch step and
repeat.

Syntax (OLE Automation)

retval = ModelDoc.CreateCircularSketchStepAndRepeat
(arcRadius, arcAngle, patternNum, patternSpacing,
patternRotate, deleteInstances)

(Table)=========================================================

| Input: | (double) arcRadius | Radius to be used in the circular sketch pattern |
| --- | --- | --- |
| Input: | (double) arcAngle | Angle relative to the sketch entities being patterned |
| Input: | (long) patternNum | Total number of instances, including the seed
geometry |
| Input: | (double) patternSpacing | Spacing between pattern elements (in radians) |
| Input: | (BOOL) patternRotate | Rotate the pattern |
| Input: | (BSTR) deleteInstances | Instance numbers to delete passed as a string
in the format: "( a ) ( b ) ( c )
" |
| Return: | (BOOL) retval | TRUE if the sketch pattern was created successfully,
FALSE otherwise |

Syntax (COM)

status = ModelDoc->CreateCircularSketchStepAndRepeat
(arcRadius, arcAngle, patternNum, patternSpacing,
patternRotate, deleteInstances, &retval )

(Table)=========================================================

| Input: | (double) arcRadius | Radius to be used in the circular sketch pattern |
| --- | --- | --- |
| Input: | (double) arcAngle | Angle relative to the sketch entities being patterned |
| Input: | (long) patternNum | Total number of instances, including the seed
geometry |
| Input: | (double) patternSpacing | Spacing between pattern elements (in radians) |
| Input: | (VARIANT_BOOL) patternRotate | Rotate the pattern |
| Input: | (BSTR) deleteInstances | Instance numbers to delete passed as a string
in the format: "( a ) ( b ) ( c )
" |
| Output: | (VARIANT_BOOL) retval | TRUE if the sketch pattern was created successfully,
FALSE otherwise |
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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__CreateCircularSketchStepAndRepeat.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
