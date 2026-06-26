---
title: "ModelDoc::InsertScale"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertScale.htm"
---

# ModelDoc::InsertScale

This
method is obsolete and has been superseded by[ModelDoc2::InsertScale](../ModelDoc2/ModelDoc2__InsertScale.htm).

Description

This method applies a scaling factor to the
model.

Syntax (OLE Automation)

void ModelDoc.InsertScale (scaleFactor_x, scaleFactor_y, scaleFactor_z, isUniform, scaleType)

(Table)=========================================================

| Input: | (double) scaleFactor_x | X component of the scale factor |
| --- | --- | --- |
| Input: | (double) scaleFactor_y | Y component of the scale factor |
| Input: | (double) scaleFactor_z | Z component of the scale factor |
| Input: | (BOOL) isUniform | TRUE if the scaling should be uniform, FALSE
otherwise. |
| Input: | (int) scaleType | Type of scale as defined in swScaleType_e |

Syntax (COM)

status = ModelDoc->InsertScale ( scaleFactor_x,
scaleFactor_y, scaleFactor_z, isUniform, scaleType )

(Table)=========================================================

| Input: | (double) scaleFactor_x | X component of the scale factor |
| --- | --- | --- |
| Input: | (double) scaleFactor_y | Y component of the scale factor |
| Input: | (double) scaleFactor_z | Z component of the scale factor |
| Input: | (BOOL) isUniform | TRUE if the scaling should be uniform, FALSE
otherwise |
| Input: | (int) scaleType | Type of scale as defined in swScaleType_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If isUniform is TRUE, then scaleFactor_xkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}is
used as the uniform scaling factor. If isUniform is FALSE, then all three
scaling factors are used.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="16777215" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__InsertScale.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
