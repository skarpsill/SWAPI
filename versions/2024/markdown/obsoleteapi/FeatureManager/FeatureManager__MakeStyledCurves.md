---
title: "FeatureManager::MakeStyledCurves"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__MakeStyledCurves.htm"
---

# FeatureManager::MakeStyledCurves

This method is obsolete and has been superseded
by[FeatureManager::MakeStyledCurves2](sldworksAPI.chm::/FeatureManager/FeatureManager__MakeStyledCurves2.htm).

Description

This method fits a spline to sketch segments
to make a smooth edge on the model.

Syntax (OLE Automation)

void = FeatureManager.MakeStyledCurves ( tol, mode
)

(Table)=========================================================

| Input: | (double) tol | Deviation permitted from the selected geometry |
| --- | --- | --- |
| Input: | (long) mode | 1
= Convert the selected geometry to construction geometry 11
= delete the selected geometry |

Syntax (COM)

status = FeatureManager->MakeStyledCurves ( tol,
mode )

Parameters Table Start

(Table)=========================================================

| Input: | (double) tol | Deviation permitted from the selected geometry |
| --- | --- | --- |
| Input: | (long) mode | 1
= Convert the selected geometry to construction geometry 11
= delete the selected geometry |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

All of the selected sketch
segments must be connected or this method will fail.

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\FeatureManager\FeatureManager__MakeStyledCurves.htm" >
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
<param name="Items" value="FeatureManager_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\FeatureManager\FeatureManager__MakeStyledCurves.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
