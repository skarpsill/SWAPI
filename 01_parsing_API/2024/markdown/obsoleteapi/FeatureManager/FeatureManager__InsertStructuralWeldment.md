---
title: "FeatureManager::InsertStructuralWeldment"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertStructuralWeldment.htm"
---

# FeatureManager::InsertStructuralWeldment

This method is obsolete and has been superseded
by[FeatureManager::InsertStructuralWeldment2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertStructuralWeldment2.htm).

Description

This method inserts a structural
weldment feature using the selected sketch segment.

Syntax (OLE Automation)

retval = FeatureManager.InsertStructuralWeldment
( path, endCond, angle)

(Table)=========================================================

| Input: | (BSTR) path | Path, filename, and name of the
type of structural member to insert |
| --- | --- | --- |
| Input: | (long) endCond | End condition as defined in swSolidWorksWeldmentEndCondOptions_e |
| Input: | (double) angle | Angle of rotation of the sketch
about the sketch segment |
| Output: | (LPFEATURE*) retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->InsertStructuralWeldment
( path, endCond, angle, &retval)

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) path | Path, filename, and name of the
type of structural member to insert |
| --- | --- | --- |
| Input: | (long) endCond | End condition as defined in swSolidWorksWeldmentEndCondOptions_e |
| Input: | (double) angle | Angle of rotation of the sketch
about the sketch segment |
| Output: | (LPFEATURE*) retval | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\FeatureManager\FeatureManager__InsertStructuralWeldment.htm" >
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
<param name="Items" value="FeatureManager_Object$$**$$ZGetWeldments$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\FeatureManager\FeatureManager__InsertStructuralWeldment.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
