---
title: "ModelDoc2::InsertScale"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertScale.htm"
---

# ModelDoc2::InsertScale

This method is obsolete and has been superseded
by[FeatureManager::InsertScale](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertScale.htm).

Description

This method applies a scaling factor to the
model.

Syntax (OLE Automation)

void ModelDoc2.InsertScale (scaleFactor_x, scaleFactor_y, scaleFactor_z, isUniform, scaleType)

(Table)=========================================================

| Input: | (double) scaleFactor_x | X component of the scale factor |
| --- | --- | --- |
| Input: | (double) scaleFactor_y | Y component of the scale factor |
| Input: | (double) scaleFactor_z | Z component of the scale factor |
| Input: | (BOOL) isUniform | TRUE if the scaling should be uniform, FALSE
otherwise |
| Input: | (int) scaleType | Type of scale as defined in swScaleType_e |

Syntax (COM)

status = ModelDoc2->InsertScale ( scaleFactor_x,
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

(Table)=========================================================

| If isUniform is... | Then... |
| --- | --- |
| TRUE | scaleFactor_x is used as the uniform scaling factor. |
| FALSE | all three scaling factors are used. |

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__InsertScale.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__InsertScale.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
